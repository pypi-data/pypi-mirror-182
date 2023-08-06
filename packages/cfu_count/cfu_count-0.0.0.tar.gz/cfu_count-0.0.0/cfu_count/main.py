"""\
Infer the density of cells growing in a culture from the number of colonies 
observed in each spot of a serial dilution.

Usage:
    cfu-count <counts> [-o <csv> | -O] [-p <img> | -P] [-v]

Arguments:
    <counts>
        The path to a NestedText file describing each of the cultures to 
        analyze.  Refer to <http://nestedtext.org> for a general description of 
        this file format.  The file should have the following structure:

            defaults:
                spot_volume_uL: <number, optional>
                total_volume_mL: <number, optional>
                library_size: <number, optional>

            cultures:
                <culture name 1>:
                    spot_volume_uL: <number>
                    total_volume_mL: <number, optional>
                    library_size: <number, optional>
                    colony_counts:
                        <dilution 1>:
                            [<count 1>, <count 2>, ...]
                        <dilution 2>:
                            [<count 1>, <count 2>, ...]
                        ...

                <culture name 2>: ...

        The values specified in the "defaults" section will be applied to each 
        individual culture in the "cultures" section.  If you have no default 
        values, you can omit both of these sections and just specify the 
        culture names at the top-level of the file.

        Below are more details on each of the parameters you can specify:

            colony_counts:
                A mapping where the keys are dilution factors (e.g. "1e4") and 
                the values are lists of observed colony counts (e.g. [1,2,3]).  
                The dilution factors must be in the format of python floating 
                point numbers, and are typically given in scientific notation.  
                The colony counts are given as a list to accommodate multiple 
                replicates of each dilution.  Every culture must specify this 
                parameter.
                
            spot_volume_uL:
                The volume of culture corresponding to each CFU count, in µL.  
                This is typically 5-10 µL.  Every culture must specify this 
                parameter (either via a default or not), because otherwise 
                there will not enough information to calculate the culture 
                density.

            total_volume_mL:
                The total volume of the culture, in mL.  If specified, the 
                output will include the total population of the culture, i.e. 
                the density times the volume.

            library_size:
                A common application of this program is to calculate the 
                fraction of a library that was successfully transformed into 
                cells.  In this case, use this parameter to specify the number 
                of unique sequences the library is expected to contain.  The 
                output will then include an estimate of how many of those 
                sequences were successfully transformed.

                Note that this estimate assumes that each of the original 
                sequences were present in exactly equal proportions, which is a 
                best-case scenario.  The true number of unique transformants 
                is probably slightly below this estimate.

Options:
    -o --output <csv>
        Output the results to the given CSV file.  Otherwise, the results will 
        just be written to stdout.  Any '%' characters in the given path will 
        be replaced with the base name of the `<counts>` input file.

    -O --output-default
        An alias for `--output %.csv`.

    -p --plot <img>
        Plot the cell density distributions calculated for each of the 
        specified cultures, then save the plots to the given file.  The file 
        can have any extension that is understood by matplotlib, e.g. '.svg', 
        '.png', etc.  Any '%' characters in the given path will be replaced 
        with the base name of the `<counts>` input file.

    -P --plot-default
        An alias for `--plot %.svg`.

    -v --view-plot
        Open the plots that would be created by the `--plot` argument in an 
        interactive GUI window.

Example:
    Here is an example input file:

        # counts.nt
        neomycin sensor:
          spot_volume_uL: 20
          library_size: 4**10
          total_volume_mL: 4.156
          colony_counts:
            {1e3: [68], 1e4: [10], 1e5: [2]}

    Here is the command to analyze these data:

        $ cfu-count counts.nt
        Culture          Density (cfu/mL)    Population (cfu)    Unique (cfu)      Library Size  Coverage (%)    Coverage (x)
        ---------------  ------------------  ------------------  --------------  --------------  --------------  --------------
        neomycin sensor  3.6(4)e+06          1.5(2)e+07          1.0(0.0)e+06       1.04858e+06  100.00(0.00)    14.46(1.61)

This program works by calculating the probability of observing the specified 
colony counts for every possible culture density.  This probability is closely 
related to the Poisson distribution, with some modifications to account for the 
fact that the density is unknown and that we might have measurements for 
different dilutions of the stock culture.  The reported culture density is the 
mean (±standard deviation) of the resulting probability distribution.  All of 
the other reported values are directly calculated from this density, with error 
propagation accounted for.  

This might seem overly complicated, given that we could estimate culture 
densities by simply multiplying observed colony counts by dilution factors.  
For a single observation, this simple approach does in fact give the most 
likely density, but the "complicated" approach has two major advantages: (i) it 
combines the information from multiple observations in a seamless and 
principled manner and (ii) it provides an estimate of uncertainty.

Some miscellaneous caveats and recommendations:

- When interpreting the standard deviations reported by this program, keep in 
  mind that the predicted cell density distributions are not normal.  That 
  said, the more counts that are observed, the more normal the distributions 
  become.  If you have more than ≈5 colonies, it's probably safe to pretend 
  that the distributions are normal.

- Serial dilutions are notoriously inaccurate, but this potential source of 
  error is not accounted for at all by this program.  If you want to make 
  accurate measurements, use direct dilutions to the maximum extent possible.

- I recommend using reverse-pipetting when plating spots.  This technique 
  avoids blowing air out the end of the pipet tip, which in turn avoids 
  microscopic droplets from being spattered all over the plate.
"""

import docopt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nestedtext as nt
import tidyexc
import sys

from .culture import Culture
from pydantic import BaseModel, ValidationError, validator, parse_obj_as
from typing import Dict, List, Optional
from byoc import arithmetic_eval
from tabulate import tabulate
from pathlib import Path
from math import floor, ceil

class DefaultConfig(BaseModel, extra='forbid'):
    spot_volume_uL: Optional[float]
    total_volume_mL: Optional[float]
    library_size: Optional[float]

    @validator('spot_volume_uL', 'total_volume_mL', 'library_size', pre=True)
    def arithmetic(cls, v):
        return arithmetic_eval(v)

class CultureConfig(DefaultConfig):
    colony_counts: Dict[float, List[int]]

class UsageError(tidyexc.Error):
    pass

def main():
    args = docopt.docopt(__doc__)
    input_path = args['<counts>']
    csv_path = pick_output_path(
            input_path, 
            args['--output'],
            args['--output-default'],
            '%.csv',
    )
    plot_path = pick_output_path(
            input_path,
            args['--plot'],
            args['--plot-default'],
            '%.svg',
    )
    view_plot = args['--view-plot']

    try:
        cultures = parse_cultures_from_nt(input_path)

        df = tabulate_results(cultures)
        if csv_path:
            df.to_csv(csv_path, index=False)
        else:
            print(tabulate(df, headers='keys', showindex=False))

        if plot_path or view_plot:
            plot_density_estimates(cultures)

            if view_plot:
                plt.gcf().canvas.set_window_title(input_path)
                plt.show()
            if plot_path:
                plt.savefig(plot_path)

    except KeyboardInterrupt:
        pass
    except UsageError as err:
        print(err, file=sys.stderr)
        sys.exit(1)

def parse_cultures_from_nt(path):
    with UsageError.add_info("input path: {path}", path=path):
        try:
            config = nt.load(path)

        except nt.NestedTextError as err1:
            err2 = UsageError(err=err1)
            err2.brief = "formatting error in input file"
            err2.info += "line: {err.lineno}"
            err2.blame += lambda e: e.err.get_message()
            raise err2 from None

        except FileNotFoundError:
            raise UsageError("input file not found") from None

        return parse_cultures_from_dict(config)

def parse_cultures_from_dict(config):
    configs, defaults = extract_defaults(config)
    configs = validate_cultures(configs)
    defaults = validate_defaults(defaults)
    configs = apply_defaults(configs, defaults)
    require_spot_volume(configs)
    return make_cultures(configs)

def tabulate_results(cultures):

    def have_volume(culture):
        return culture.total_volume_mL

    def have_library(culture):
        return culture.total_volume_mL and culture.library_size and culture.library_size > 1

    col_filters = {
            'Culture': lambda _: True,
            'Density (cfu/mL)': lambda _: True,
            'Population (cfu)': have_volume,
            'Unique (cfu)': have_library,
            'Library Size': have_library,
            'Coverage (%)': have_library,
            'Coverage (x)': have_library,
    }
    col_getters = {
            'Culture': lambda k, _: k,
            'Density (cfu/mL)': lambda _, v: f'{v.density_cfu_mL:.2gS}',
            'Population (cfu)': lambda _, v: f'{v.total_population:.2gS}',
            'Unique (cfu)': lambda _, v: f'{v.unique_population:.2gS}',
            'Library Size': lambda _, v: v.library_size,
            'Coverage (%)': lambda _, v: f'{v.percent_coverage:.2fS}',
            'Coverage (x)': lambda _, v: f'{v.fold_coverage:.2fS}',
    }
    col_getters = {
            k: v
            for k, v in col_getters.items()
            if any(col_filters[k](c) for c in cultures.values())
    }

    rows = []

    for name, culture in cultures.items():
        row = {
                k: v(name, culture) if col_filters[k](culture) else ''
                for k, v in col_getters.items()
        }
        rows.append(row)

    return pd.DataFrame(rows)

def plot_density_estimates(cultures):
    n = len(cultures)

    x_min = min(
            (d := culture.density_cfu_mL).n - 3 * d.s
            for culture in cultures.values()
    )
    x_max = max(
            (d := culture.density_cfu_mL).n + 3 * d.s
            for culture in cultures.values()
    )
    x1 = np.logspace(
            floor(np.log10(x_min)),
            ceil(np.log10(x_max)),
            500,
    )[1:]
    y0_ticks = []
    y0_labels = []

    fig, ax = plt.subplots(
            nrows=2,
            ncols=1,
            sharex=True,
            figsize=(5, 5 + n/4),
    )

    for i, (name, culture) in enumerate(cultures.items()):
        d = culture.density_cfu_mL

        y0 = [n - i]
        y0_ticks += y0
        y0_labels.append(name)

        x0 = [d.nominal_value]
        x0_err = [d.std_dev]

        # Because the x-axis is in log-space, distributions with smaller means 
        # will artificially appear to have much greater areas than those with 
        # larger means.  This isn't wrong, but it's distracting and unhelpful,  
        # so here we eliminate the effect by scaling each distribution by its 
        # "apparent" area.
        y1 = culture.density_pdf_cfu_mL(x1)
        y1 /= np.trapz(y1)

        style = dict(
                color=f'C{i}',
        )

        ax[0].plot(x0, y0, marker='|', **style)
        ax[0].errorbar(x0, y0, None, x0_err, **style)

        ax[1].semilogx(x1, y1, **style)

    ax[0].set_yticks(y0_ticks, y0_labels)
    ax[0].grid(which='major', axis='x', linestyle=':', color='xkcd:dark grey')
    ax[0].grid(which='minor', axis='x', linestyle=':', color='xkcd:light grey')

    ax[1].set_yticks([])
    ax[1].set_xlabel("cell density (cfu/mL)")
    ax[1].set_ylabel("probability")

    for axi in ax:
        axi.grid(which='major', axis='x', linestyle=':', color='xkcd:dark grey')
        axi.grid(which='minor', axis='x', linestyle=':', color='xkcd:light grey')

    fig.tight_layout()
    return fig

def extract_defaults(config):
    config = config.copy()

    try:
        cultures = config.pop('cultures')

    except KeyError:
        return config, {}

    else:
        defaults = config.pop('defaults', {})

        if config:
            err = UsageError(keys=list(config.keys()))
            err.brief = "unexpected top-level config key(s): {keys!r}"
            err.blame += "if the 'cultures' key is specified, the only other allowed top-level key is 'defaults'"
            raise err

        return cultures, defaults

def validate_cultures(configs):
    models = validate_pydantic_model(Dict[str, CultureConfig], configs)
    return {
            key: remove_none_values(model.dict())
            for key, model in models.items()
    }

def validate_defaults(defaults):
    obj = validate_pydantic_model(DefaultConfig, defaults)
    return remove_none_values(obj.dict())

def validate_pydantic_model(model, data):
    try:
        return parse_obj_as(model, data)

    except ValidationError as err1:

        def softrepr(x):
            return repr(x) if ' ' in x else str(x)

        def format_errors(e):
            for err in e.errors:
                loc = '.'.join(softrepr(x) for x in err['loc'][1:])
                yield f"{loc}: {err['msg']}"

        err2 = UsageError(errors=err1.errors())
        err2.brief = "unexpected value in input file"
        err2.blame += format_errors
        raise err2

def apply_defaults(configs, defaults):
    return {
            k: {**defaults, **v}
            for k, v in configs.items()
    }

def remove_none_values(dict):
    return {k: v for k, v in dict.items() if v is not None}

def require_spot_volume(configs):
    for name, config in configs.items():
        if 'spot_volume_uL' not in config:
            err = UsageError(culture=name)
            err.brief = "must specify 'spot_volume_uL'"
            err.info += "culture: {culture}"
            raise err

def make_cultures(configs):
    return {
            k: make_culture(v)
            for k, v in configs.items()
    }

def make_culture(kwargs):
    count_dict = kwargs.pop('colony_counts')
    dilutions, counts = expand_colony_counts(count_dict)

    kwargs['dilutions'] = dilutions
    kwargs['colony_counts'] = counts

    return Culture(**kwargs)

def expand_colony_counts(count_dict):
    dilutions = []
    counts = []

    for d, cs in count_dict.items():
        dilutions += [d] * len(cs)
        counts += cs

    return dilutions, counts

def pick_output_path(input_path, output_template, use_default, default_template):
    if use_default:
        output_template = default_template
    if not output_template:
        return None

    base_name = Path(input_path).stem
    output_path = output_template.replace('%', base_name)
    return Path(output_path)

