# -*- coding: utf-8 -*-
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
from .reduce_deg_poly import reduce_deg_poly

#@controler_types(ndarray, ndarray, float)
def chain_poles_poly(poly_mat, delay_vect, precision):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Computes the chains of poles polynomial.

    out_poly = chain_poles_poly(poly_mat, delay_vect, precision) takes in
    input the quasi polynomial poly_mat, the delay vector delay_vect and
    a precision precision and returns the chain of poles polynomial.

    Example:

    """

    degree = int(max(delay_vect))
    out_poly = np.zeros(degree+1)
    deg_index = poly_mat.shape[1] - len(reduce_deg_poly(poly_mat[0, :], \
                                                        prec=precision))
    out_poly[degree] = 1
    for i in range(1, poly_mat.shape[0]):
        position = int(degree - delay_vect[i - 1])
        out_poly[position] = poly_mat[i, deg_index] / \
                             float(poly_mat[0, deg_index])

    return out_poly
