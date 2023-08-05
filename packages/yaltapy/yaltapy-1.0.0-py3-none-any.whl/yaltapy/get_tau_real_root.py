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
from .decorators.control_inputs import controler_types

#@controler_types(complex, np.ndarray, np.ndarray)
def get_tau_real_root(root, poly_mat, delay_vect):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """TO COMMENT.

    """
    #import pdb;pdb.set_trace()
    vect_a = np.concatenate((np.zeros(1), delay_vect)).astype("int64")
    deg_k = int(delay_vect[-1])
    poly_a = np.zeros(deg_k, dtype=np.complex128)
    out_tau = 0

    for i in range(len(vect_a)):
        poly_a[deg_k - vect_a[i] - 1] = np.polyval(poly_mat[i, :], root)
    roots_a = np.roots(poly_a)
    for i in range(len(roots_a)):
        tmp = roots_a[i]
        if np.imag(tmp) != 0 or np.real(tmp) <= 0 or np.real(tmp) >= 1:
            roots_a[i] = 0
    try:
        out_tau = np.log(max(roots_a))/root
    except ValueError: # arg of max() function is an empty sequence
        return -np.inf - np.inf * 1j
    else:
        return out_tau
