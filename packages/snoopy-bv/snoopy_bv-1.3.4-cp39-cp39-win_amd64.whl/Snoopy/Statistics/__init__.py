import _Statistics
from _Statistics import set_logger_level
import numpy as np
_xmax_log = np.log(np.finfo(float).max)
from .empirical_quantiles import probN , probN_ci
from .dist import DistGen, FrozenDistABC
from .statErrors import StatErrors
from ._longTerm import LongTerm, LongTermSpectral, squashSpectralResponseList, LongTermGen
from ._longTermSD import LongTermSD, LongTermRao, LongTermQuadDamping
from ._impact_velocity import LongTermImpact, LongTermImpactSL
from .powern import Powern
from .maxEntropySolver import MaxEntropySolver
from .distribution_cpp import  weibull_min_c, geneextreme_c, rayleigh_c, gengamma_patched, Rayleigh_n, pearson3_patched
from .returnLevel import ReturnLevel
from .discreteSD import DiscreteSD, rec34_SD, ww_SD

import os
TEST_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Tests", "test_data")


__all__ = [ "weibull_min_c" , "geneextreme_c", "rayleigh_c", "probN" , "gengamma_patched" ,
            "DistGen", "FrozenDistABC", "StatErrors", "longTerm", "longTerm_inv" , "longTermContribution", "Powern",
            "longTermSpectral_inv", "longTermSpectral", "gengamma_patched", "pearson3_patched", "ReturnLevel", "DiscreteSD", "rec34_SD", "ww_SD"]
