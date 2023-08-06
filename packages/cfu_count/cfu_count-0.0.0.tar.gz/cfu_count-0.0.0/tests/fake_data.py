#!/usr/bin/env python3

"""
Test whether accurate cell densities can be recovered from synthetic 
dilution/colony count data.

Usage:
    fake_data.py [-n <trials>] [-o <path>]

Options:
    -n --num-trials <int>           [default: 100]
        The number of different fake data sets to generate for each set of 
        "true" parameters.  

    -o --output <path>              [default: fake_data.svg]
        Save the resulting plot to the given file.

The purpose of this script is to verify that the statistics implemented by this 
package are correct, without having any analytical examples with known 
solutions to compare to.  The idea behind the test is to generate fake count 
data given some "true" density, then to see how often the interval predicted 
from those counts includes that density.  If the calculated means and standard 
deviations are accurate (and the predicted distribution is approximately 
normal), the 1σ and 2σ intervals should include the true density ≈68% and ≈95% 
of the time, respectively.  The intervals should also get narrower as more 
counts are provided.

A few comments on the specific parameters tested by this script:

- I focused on conditions having no more than 30 counts per spot.  This is 
  because, in my experience, it's not really possible to accurately count more 
  than ≈30 colonies in a single 5 µL spot.

- The intervals are noticeably less accurate for the condition where only 1 
  count per observation is expected.  I believe that this is because the 
  predicted distribution becomes noticeably not normal when fewer than ≈2 
  counts are observed.
"""

import numpy as np
import matplotlib.pyplot as plt

from cfu_count import DilutedPoisson, mean_std
from scipy.stats import poisson
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
from tqdm.contrib.itertools import product

def plot_prediction_matrix(n):
    true_densities = [1e2, 1e5, 1e8]
    expected_counts = [
            [1],
            [10],
            [1, 10],
            [1, 1, 10, 10],
            [0.3, 0.3, 3, 3],
            [3, 3, 30, 30],
    ]

    fig, axes = plt.subplots(
            nrows=len(true_densities),
            ncols=len(expected_counts),
            sharey='row',
            sharex='all',
            figsize=(20, 10),
    )

    for (i, true_density), (j, counts) in product(
            list(enumerate(true_densities)),
            list(enumerate(expected_counts)),
    ):
        dilutions = [true_density / x for x in counts]
        plot_predictions(axes[i,j], true_density, dilutions, n=n)

    fig.tight_layout()

def plot_predictions(ax, true_density, dilutions, *, n):
    within_1_std = 0
    within_2_std = 0

    with ProcessPoolExecutor() as pool:
        futures = []

        for i in range(n):
            counts = fake_counts(true_density, dilutions)
            pdf = DilutedPoisson(dilutions, counts)
            future = pool.submit(mean_std, pdf)
            futures.append(future)

        for i, future in tqdm(
                enumerate(as_completed(futures)),
                total=n,
                leave=False,
        ):
            y_predict = future.result()

            x = [i]
            y = [y_predict.nominal_value]
            y_err = [y_predict.std_dev]

            ax.errorbar(x, y, y_err, color='tab:blue')

            within_1_std += within_std(true_density, y_predict, 1)  # ≈68%
            within_2_std += within_std(true_density, y_predict, 2)  # ≈95%

    ax.axhline(true_density, linestyle='--', color='k')

    ax.set_title(
            f'expected counts: {[true_density / d for d in dilutions]}\n'
            f'within 1σ: {100 * within_1_std / n}%\n'
            f'within 2σ: {100 * within_2_std / n}%'
    )
    ax.set_xticks([])
    ax.set_xlim(-1, n)

def fake_counts(true_density, dilutions):
    return [
            poisson.rvs(mu=true_density / dilution)
            for dilution in dilutions
    ]

def within_std(x, x_predict, factor):
    mu = x_predict.nominal_value
    sig = x_predict.std_dev
    return (mu - sig * factor) <= x <= (mu + sig * factor)

if __name__ == '__main__':
    import docopt

    args = docopt.docopt(__doc__)
    n = int(args['--num-trials'])

    plot_prediction_matrix(n)

    plt.savefig(args['--output'])
    plt.show()

