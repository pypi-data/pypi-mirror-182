import numpy as np
from .poisson import DilutedPoisson, mean_std
from dataclasses import dataclass
from typing import List, Optional
from functools import cached_property

@dataclass(frozen=True, kw_only=True)
class Culture:
    dilutions: List[float]
    spot_volume_uL: float
    colony_counts: List[int]
    total_volume_mL: Optional[float] = None
    library_size: Optional[float] = None

    @cached_property
    def density_cfu_mL(self):
        return mean_std(self.density_pdf_cfu_mL)

    @cached_property
    def density_pdf_cfu_mL(self):
        d = np.asarray(self.dilutions) * 1000 / self.spot_volume_uL
        return DilutedPoisson(d, self.colony_counts)

    @cached_property
    def total_population(self):
        return self.density_cfu_mL * self.total_volume_mL

    @cached_property
    def unique_population(self):
        return unique_items(self.library_size, self.total_population)

    @cached_property
    def percent_coverage(self):
        return 100 * self.unique_population / self.library_size

    @cached_property
    def fold_coverage(self):
        return self.total_population / self.library_size


def unique_items(num_items, num_picked):
    return num_items * fraction_picked(num_items, num_picked)

def fraction_picked(num_items, num_picked):
    # I'm not sure I'm handling the "fractional" case correctly...
    return 1 - ((num_items - 1) / num_items)**num_picked
