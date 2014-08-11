"""Defines the residue and Jacobian function generators"""

import sys

import numpy as np

from .morse import *

def get_mp_base_idx(morse, elem_pair):

    """Gets the base index for the Morse parameters for a given element pair

    Since the Morse parameters for all the element pairs are stored in a big
    vector, we need to compute the base index for the Morse parameters for a
    given element pair. The protocol is fairly simple, just the De, a, and r0
    parameters of each pair in the Morse potential list are stored consecutively
    in the same order as the list for the initial guess.

    :param morse: The list of initial guesses for the Morse potential, as
        returned from the :py:func:`read_morse_inp` function.
    :param elem_pair: A pair of element symbols.

    .. warning.. 

      It will abort the program if the initial guess for the element pair is not
      given.

    """

    elem_pair_s = tuple(sorted(elem_pair))
    idx_found = [ i for i, v in enumerate(morse) if v[0] == elem_pair_s ]

    if len(idx_found) < 1:
        print "Morse potential guess for %s and %s is not given!" % elem_pair
        sys.exit(1)
    elif len(idx_found) > 1:
        print "Multiple guesses are given for %s and %s!" % elem_pair
    else:
        pair_idx = idx_found[0]

    return pair_idx * 3



def gen_rj_func(confs, morse):

    """Generate the residue and Jacobian function for a list of configurations

    It returns two functions that is able to return the residue and the Jacobian
    respectively when called with the grand vector of Morse parameters of the
    protocol as defined in the function :py:func:`get_mp_base_idx`. For a N
    parameter and M configuration problem, the residue function is going to
    return a 1-D array of length M for the residues. For the Jacobian, the
    return value is going to be an NxM matrix.

    :param confs: The list of configurations.
    :param morse: The list of initial guesses for the Morse potential.

    """

    # The vector of ab-initio energies
    ab_initio_e = np.array([i.ab_initio_e for i in confs ])

    # For each configuration, a list of (base index for Morse parameters,
    # distance) pairs for all the interactions that is accounted.
    interactions_w_base_idx = [
            [
                (get_mp_base_idx(morse, i[0]), i[1]) 
                for i in i_conf.interactions ]
            for i_conf in confs ]
    # For each configuration, a list of distances for each Morse parameters, in
    # the same order as given in the list ``morse``.
    base_idx_w_dist = [
            [
                [ i[1] for i in i_conf if i[0] == i_pot * 3 ]
                for i_pot in xrange(0, len(morse)) ]
            for i_conf in interactions_w_base_idx ]

    # n parameter, m residue, as the convention in the documentation of leastsq
    # of scipy
    n = 3 * len(morse)
    m = len(confs)

    # The residue closure to be returned
    def residue(mp):
        # Use iteration to boost performance
        res = np.empty(m, dtype=np.float64)
        for i in xrange(0, m):
            # Use iterator
            res[i] = sum(
                    morse_e(i_term[1], mp[i_term[0]:(i_term[0] + 3)])
                    for i_term in interactions_w_base_idx[i] ) - ab_initio_e[i]
            continue
        return res

    def jacobi(mp):
        res = np.empty((n, m), dtype = np.float64)
        # Column major iteration
        for i_conf in xrange(0, m):
            for i_pot in xrange(0, len(morse)):
                dists = base_idx_w_dist[i_conf][i_pot]
                cur_param = mp[i_pot * 3:(i_pot + 1) * 3]
                partial_de = sum(morse_d_de(i_r, cur_param) for i_r in dists)
                partial_a = sum(morse_d_a(i_r, cur_param) for i_r in dists)
                partial_r0 = sum(morse_d_r0(i_r, cur_param) for i_r in dists)
                res[i_pot * 3, i_conf] = partial_de
                res[i_pot * 3 + 1, i_conf] = partial_a
                res[i_pot * 3 + 2, i_conf] = partial_r0
                continue
            continue
        return res

    return residue, jacobi


                



