#!/usr/bin/env python3

import pytest
from cfu_count import DilutedPoisson

@pytest.mark.parametrize(
        'dilutions, counts', [
            ([1e6], [0]),
            ([1e6], [1]),
            ([1e6], [2]),

            ([1e5, 1e6], [0,0]),
            ([1e5, 1e6], [1,0]),
            ([1e5, 1e6], [2,0]),

            ([1e5, 1e6], [10,0]),
            ([1e5, 1e6], [10,1]),
            ([1e5, 1e6], [10,2]),
        ],
)
def test_diluted_poisson_normalized(dilutions, counts):
    pdf = DilutedPoisson(dilutions, counts)
    assert pdf.integrate(pdf) == pytest.approx(1)
