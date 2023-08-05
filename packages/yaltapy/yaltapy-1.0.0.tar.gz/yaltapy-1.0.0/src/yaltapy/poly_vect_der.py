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
from .extend_poly import extend_poly

@controler_types(np.ndarray)
def poly_vect_der(poly_mat):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Derivation of a vector of polynomials.

    out_poly_mat = poly_vect_der(poly_mat) is the derivation of
    the matrix poly_mat keeping initial matrix dimensions.

    Example:
    if poly_mat = [1 2 3
                   0 1 1
                   2 1 5],

    then the resulting derivative is

    out_poly_mat = [0 2 2
                    0 0 1
                    0 4 1].

    """

    out_poly_mat = np.zeros((poly_mat.shape[0], poly_mat.shape[1]))
    for i in range(poly_mat.shape[0]):
        out_poly_mat[i, :] = extend_poly(np.polyder(poly_mat[i, :]), \
                                         poly_mat.shape[1])

    return out_poly_mat
