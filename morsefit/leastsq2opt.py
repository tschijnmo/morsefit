"""Defines subroutines for converting a leastsq closure to minimize closure

Since the :py:func:`scipy.optimize.leastsq` seems to be limited in terms of its
performance, the more generate :py:func:`scipy.optimize.minimize` function can be
tried to be used. However, they required different kind of closures for
computing the residues and the Jacobian. Here some utility functions are
provided to translate the closures for least square minimization into closures
for general minimizers.

The convention for naming argument is always :math:`N` parameter and :math:`M`
configuration problem.

"""

import numpy as np


def conv_residue(residue_closure, N, M):

    """Converts a residue closure into the residue square closure

    :param func residue_closure: The closure returning the :math:`M` residues.
    :param int N: The number of parameters, not actually used here.
    :param int M: The number of configurations.

    """

    def norm_sq_closure(param):
        residues = residue_closure(param)
        return sum(i_residue ** 2 for i_residue in residues)

    return norm_sq_closure


def conv_jacobi(jacobi_closure, residue_closure, N, M):

    """Converts a Jacobian closure into the Jacobian for minimize

    :param func jacobi_closure: The closure for computing the Jacobian matrix.
    :param func residue_closure: The closure for computing the residue vector.
    :param int N: The number of parameters
    :param int M: The number of residues

    """

    def jacobi_new(param):
        residue = residue_closure(param)
        jacobi = jacobi_closure(param)
        result = np.empty(N, dtype=np.float64)
        for i in xrange(0, N):
            result[i] = sum(
                    2 * residue[j] * jacobi[i][j] for j in xrange(0, M)
                    )
            continue
        return result

    return jacobi_new







