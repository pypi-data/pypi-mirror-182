import numpy as np

from scipy.stats import poisson
from scipy.integrate import quad
from uncertainties import ufloat
from functools import cached_property

class DilutedPoisson:
    r"""
    Calculate the probability that a particular cell density led to an observed 
    series of colony counts.

    The Poisson distribution gives the probability of observing a particular 
    number of counts (:math:`k`) given a particular density (:math:`\lambda`):

    .. math::

        \mathrm{Pois}(k, \lambda) = \frac{\lambda^k e^{-\lambda}}{k!} \\

    We are interested in a slightly modified form of this distribution.  First, 
    we may have multiple counts (:math:`K`) for multiple different dilutions 
    (:math:`D`) of the initial culture.  We account for this by multiplying all 
    the relevant probabilities and dividing the density as appropriate:

    .. math::

        p(K, D, \lambda) \propto \prod_{\substack{k \in K \\ d \in D}} \mathrm{Pois}(k, \lambda/d)

    Second, we need to normalize this modified distribution.  Unlike the 
    original Poisson distribution, which is normalized over all counts, we want 
    to normalize over all densities, so that we can draw conclusions about 
    which densities best describe the data.  The normalization factor is the 
    above equation integrated over every possible density:

    .. math::

        \int_0^{\infty} p(K, D, \lambda) \, d\lambda

    I was not able to work out the analytical form of this integral, so instead the 
    integration is performed numerically.  The mean and standard deviation of 
    this distribution are also calculated by numerical integration.
    """

    def __init__(self, dilutions, counts):
        self.dilutions = np.asarray(dilutions)
        self.counts = np.asarray(counts)
        assert self.dilutions.shape == self.counts.shape

        # https://stackoverflow.com/questions/19990863/how-to-vectorize-call-method
        self._pdf = np.vectorize(self._pdf)

    def __call__(self, density):
        """
        Return the probability the given cell density would result in the 
        counts provided to the constructor.

        The given density can either be a scalar (in which case the return 
        value will also be a scalar) or an iterable (in which case the return 
        value will be an `np.ndarray` of the same shape).
        """
        return self._pdf(density)

    def integrate(self, f):
        """
        Numerically integrate the given function, in the range where the PDF 
        has non-trivial value.

        Ideally we could integrate functions over the whole domain of the PDF, 
        which is [0, infinity).  However, this would make it hard for the 
        numerical integration algorithm to actually find the non-zero areas of 
        the function, so practically we get much better results by providing a 
        finite range.

        The specific range we use is [0, 10x], where 'x' is the average of the 
        counts multiplied by the dilution factors: a value that should be close 
        to the mean of the distribution.  This range is quite generous, but 
        still seems to give good results empirically.
        """
        center = (self.dilutions * self.counts).mean()
        bounds = 0, 10 * max(center, max(self.dilutions))
        integral, error = quad(f, *bounds, points=[center])
        return integral

    def _pdf(self, density):
        return self._pdf_unnormalized(density) / self._pdf_denominator

    def _pdf_unnormalized(self, density):
        mu = density / self.dilutions
        p = poisson.pmf(k=self.counts, mu=mu)
        return p.prod()

    @cached_property
    def _pdf_denominator(self):
        norm = self.integrate(self._pdf_unnormalized)
        return norm

def mean_std(pdf):
    mu = mean(pdf)
    sig = std(pdf, mu=mu)
    return ufloat(mu, sig)

def mean(pdf):
    return pdf.integrate(lambda x: x * pdf(x))

def var(pdf, mu=None):
    if mu is None:
        mu = mean(pdf)

    var = pdf.integrate(lambda x: x**2 * pdf(x))
    return var - mu**2

def std(pdf, sig2=None, mu=None):
    if sig2 is None:
        sig2 = var(pdf, mu)
    return np.sqrt(sig2)

