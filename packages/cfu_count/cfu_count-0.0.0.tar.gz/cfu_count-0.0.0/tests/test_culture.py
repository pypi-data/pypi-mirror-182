#!/usr/bin/env python3

import parametrize_from_file as pff

from cfu_count.culture import *
from fractions import Fraction
from pytest import approx

def test_culture():
    # The purpose of this test is mostly to make sure that the Culture API is 
    # implemented correctly.  Most of these values I can't calculate by hand, 
    # so I just chose some arbitrary parameters and checked that the results 
    # looked about right.  There are other tests that more carefully assess the 
    # correctness of the underlying functions.
    # 
    # Note that expected culture density is 10% greater than what you'd get if 
    # you were just to calculate: colony count × dilution ÷ spot volume.  This 
    # value is actually the mode of the distribution, but the mean (which is 
    # what's being tested here) is slightly greater because the distribution is 
    # asymmetric, with a longer tail on the right.

    culture = Culture(
            dilutions=[1e3],
            colony_counts=[10],
            spot_volume_uL=5,
            total_volume_mL=2,
            library_size=1e6,
    )
    assert culture.density_cfu_mL.n == approx(2.2e6)
    assert culture.density_cfu_mL.s == approx(6.6e5, abs=0.1e5)
    assert culture.total_population.n == approx(4.4e6)
    assert culture.unique_population.n == approx(9.88e5, abs=0.01e5)
    assert culture.percent_coverage.n == approx(98.8, abs=0.1)
    assert culture.fold_coverage.n == approx(4.4)

@pff.parametrize(
        schema=[
            pff.cast(
                num_items=int,
                num_picked=int,
                expected_fraction=Fraction,
                expected_unique=Fraction,
            ),
            pff.error_or('expected_fraction', 'expected_unique'),
        ],
)
def test_unique_items(num_items, num_picked, expected_fraction, expected_unique, error):
    with error:
        assert fraction_picked(num_items, num_picked) == expected_fraction
        assert unique_items(num_items, num_picked) == expected_unique
