#!/usr/bin/env python3

"""
Infer the cell density of a culture from the number of colonies observed in 
each spot of a serial dilution.
"""

__version__ = '0.0.0'

from .poisson import DilutedPoisson, mean_std
from .culture import Culture
