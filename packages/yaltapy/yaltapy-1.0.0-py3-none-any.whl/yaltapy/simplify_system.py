# coding: utf-8
"""
YALTApy
Copyright (C) 2022 Inria

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import numpy as np
from math import gcd

from .decorators.control_inputs import controler_types

#@controler_types(np.ndarray, float, np.ndarray)
def simplify_system(poly_mat, tau, delay_vect):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Some simplifying operations on inputs.

    [out_poly_mat, out_tau, out_delay_vect] = simplify_system(poly_mat, tau,
                                                              delay_vect)
    returns the specified inputs poly_mat (N-by-N matrix), the base delay tau
    and the delay vector delay_vect after some simplifying operations on it.
    For inputs poly_mat, tau, delay_vect, outputs are respectively
    out_poly_mat, out_tau and out_delay_vect.

    Simplifying operations consist in removing leading zeros, normalize,
    and factorize the delay vector.

    Example:
    If poly_mat = [0 2 4
                   0 2 2
                   0 3 1],
    tau = 2 and delay_vect = [4 6],

    then out_poly_mat = [1   2
                         1   1
                         1.5 0.5],
    out_tau = 4 and out_delay_vect = [2 3].

    """

    nb_col = poly_mat.shape[1]

    # Remove the leading zeros columns of poly_mat
    out_poly_mat = np.copy(poly_mat)
    for i in range(nb_col):
        if not all(out_poly_mat[:, 0] == 0):
            break
        else:
            out_poly_mat = np.copy(out_poly_mat[:, 1::])

    # Normalise the quasi polynomial with leading term of the first polynomial
    if out_poly_mat[0][0] != 0:
        out_poly_mat = out_poly_mat / float(out_poly_mat[0][0])

    # Check for factorization of delay_vect
    pgcd = delay_vect[0]
    for i in range(1, delay_vect.shape[0]):
        pgcd = gcd(int(pgcd), int(delay_vect[i]))

    out_tau = tau * pgcd
    out_delay_vect = delay_vect / pgcd

    # If there are identical delays in the vector of delays, we need to
    # factorize/simplify the system.
    poly = out_poly_mat[1:, :]
    delay_ind = 0
    while delay_ind < poly.shape[0]:
        delay = out_delay_vect[delay_ind]
        # il y a un pb avec les sélections par indices
        same = (delay == out_delay_vect)
        same_del_idx = [idx for idx, eq in enumerate(same) if eq]
        if len(same_del_idx) > 1: # if the same delay is found in the list
            # we sum per columns
            a_poly = np.sum(poly[same_del_idx], axis=0)
            poly[delay_ind, :] = a_poly; # new summable term
            same_del_idx.remove(delay_ind)
            not_equal_del_idx = [i for i in range(len(out_delay_vect)) \
                                 if i not in same_del_idx]
            poly = poly[not_equal_del_idx, :]
            out_delay_vect = out_delay_vect[not_equal_del_idx]
        delay_ind += 1

    out_poly_mat = np.vstack((out_poly_mat[0, :],  poly))


    return out_poly_mat, out_tau, out_delay_vect
