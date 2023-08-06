import parametrize_from_file as pff

from cfu_count.main import *
from dataclasses import dataclass
from uncertainties import UFloat, ufloat
from re_assert import Matches
from subprocess import run

@dataclass
class MockCulture:
    density_cfu_mL: UFloat

    total_volume_mL: Optional[float] = None
    total_population: Optional[UFloat] = None

    library_size: Optional[float] = None
    unique_population: Optional[UFloat] = None
    percent_coverage: Optional[UFloat] = None
    fold_coverage: Optional[UFloat] = None

with_cfu = pff.Namespace(
        Culture=Culture,
        MockCulture=MockCulture,
        UsageError=UsageError,
        ufloat=ufloat,
)

@pff.parametrize(
        schema=[
            pff.defaults(stdout='^$', stderr='^$', manifest=[]),
        ],
        indirect=['tmp_files'],
)
def test_main(tmp_files, command, stdout, stderr, manifest):
    p = run(command, cwd=tmp_files, capture_output=True, text=True, shell=True)

    Matches(stdout).assert_matches(p.stdout)
    Matches(stderr).assert_matches(p.stderr)

    for path in manifest:
        assert (tmp_files / path).exists()

@pff.parametrize(
        schema=[
            pff.cast(expected=with_cfu.eval),
            with_cfu.error_or('expected')
        ],
)
def test_parse_cultures(given, expected, error):
    with error:
        assert parse_cultures_from_dict(given) == expected

@pff.parametrize(
        schema=pff.cast(cultures=with_cfu.eval),
)
def test_tabulate_results(cultures, expected):
    df = tabulate_results(cultures)
    assert df.to_csv(index=False).strip() == expected

@pff.parametrize
def test_expand_colony_counts(given, expected):
    dilutions, counts = expected
    assert expand_colony_counts(given) == (dilutions, counts)

@pff.parametrize
def test_pick_output_path(input_path, output_template, default_template, use_default, expected):
    output_path = pick_output_path(
            input_path,
            output_template,
            with_cfu.eval(use_default),
            default_template,
    )
    expected = Path(expected) if expected else None
    assert output_path == expected
