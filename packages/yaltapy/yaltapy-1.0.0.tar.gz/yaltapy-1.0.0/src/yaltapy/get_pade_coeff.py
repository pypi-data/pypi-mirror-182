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
from .power_poly import power_poly
from .reduce_deg_poly import reduce_deg_poly

from .decorators.control_inputs import controler_types

#@controler_types(np.ndarray, int, float, np.ndarray, int)
def get_pade_coeff(poly_mat, degree, tau, delay_vect, order):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Get the Pade Fractions.

    [poly_num, poly_den] = get_pade_coeff(poly_mat, degree, tau,
                                          delay_vect, order)
    takes in input an array of polynomials poly_mat, the degree of the
    denominator of the transfer function (degree), the delay tau, the
    delay vector delay_vect, the order of the Pade approximation, and
    returns arrays of numerators and denominators of the Pade approximation
    in poly_num and poly_den respectively.

    See "YALTA: a Matlab toolbox  for the Hinf stability analysis of
    classical and fractionnal systems with commensurate delays." [IFAC TDS 2013]
    for implementation details.

    """

    # den corresponds to the denominator of Rk (in the article).
    # The degree of den is iDegree and the length of den is (iDegree + 1).
    den = np.poly1d(-np.ones(degree), True)
    delay_vect_a = np.concatenate((np.zeros(1), delay_vect))
    poly_num = np.zeros((poly_mat.shape[0], poly_mat.shape[1] + 2 * order))
    # poly_den corresponds to the denominator of S(n)Rk. It is the result
    # of the convolution between aDen and den_factor (vector which is the
    # denominator of Pade development, see article for further details).
    # See below for details on the dimensioning of poly_den.
    poly_den = np.zeros((poly_mat.shape[0], 2*order + degree + 1))

    for i in range(poly_mat.shape[0]):
        num = poly_mat[i, :]
        tau_k = delay_vect_a[i] * tau
        # Pade development
        factor = np.array([tau_k**2, -6*tau_k*order, 12*order**2])

        num_factor = power_poly(factor, order)
        poly_num[i, :] = np.convolve(num, num_factor)
        factor[1] *= -1
        den_factor = power_poly(factor, order)
        # Nb. of columns of poly_den: dim(den) + dim(den_factor) - 1 (see
        # convolve function documentation).
        # Then dim(den) + dim(den_factor) - 1
        #     = degree + 1 + 2*order + 1 - 1
        #     = 2*order + degree + 1
        poly_den[i, :] = np.convolve(den, den_factor)

    # Normalisation
    norm_den = reduce_deg_poly(poly_den[0, :])
    poly_num = poly_num / norm_den[0]
    poly_den = poly_den / norm_den[0]

    return poly_num, poly_den
