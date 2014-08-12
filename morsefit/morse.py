"""Defines utility functions for the Morse potential"""

from math import exp

def morse_e(r, mp):

    """Compute the energy according to Morse potential

    :param float r: The distance between atoms.
    :param mp: An iterator, mostly a numpy 1-D array, holding the :math:`D_e`,
      :math:`a`, and :math:`r_0` parameters for the Morse potential.
    :return: The energy according to the Morse potential.
    :rtype: float

    """

    de, a, r0 = mp
    return de * ((
            exp(a * (r0 - r)) - 1
            ) ** 2 - 1.0)

def morse_d_de(r, mp):

    """Compute the partial derivative of Morse energy wrt :math:`D_e`."""

    de, a, r0 = mp
    return (( exp(a * (r0 - r)) - 1 ) ** 2 - 1.0)

def morse_d_a(r, mp):

    """Compute the partial derivative of Morse energy wrt :math:`a`."""

    de, a, r0 = mp
    return -2 * de * (r - r0) * exp(a * (r0 - r)) * (
            exp(a * (r0 - r)) - 1 )

def morse_d_r0(r, mp):

    """Compute the partial derivative of Morse energy wrt :math:`r_0`."""

    de, a, r0 = mp
    return 2 * a * de * exp(a * (r0 - r)) * (
            exp(a * (r0 - r)) - 1 )

