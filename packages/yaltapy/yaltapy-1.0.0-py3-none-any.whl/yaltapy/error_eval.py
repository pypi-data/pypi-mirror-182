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

#@controler_types(np.complex128, np.ndarray, float, float, np.ndarray)
def error_eval(eval_point, poly_mat, tau, alpha, delay_vect):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Computes the error evaluation.

    err = error_eval(eval_point, poly_mat, tau, alpha, delay_vect) takes
    in input the evaluation point eval_point, the quasi polynomial
    poly_mat, the base delay tau, the fractional power alpha and the
    vector delay delay_vect, and returns the absolute error err.
    The absolute error is the evaluation of the quasi polynomial at an
    unstable pole value.

    Example:

    """

    # Initialisation
    delay_vect = np.concatenate((np.zeros(1), delay_vect))
    exp_value = []
    for i in range(len(delay_vect)):
        exp_value.append(np.exp(-tau * eval_point**(1/alpha) * delay_vect[i]))
    tmp_value = np.zeros((poly_mat.shape[0], 1), dtype=np.complex128)
    # Evaluation of all the polynomials then convolution with the
    # exponential factors

    for i in range(poly_mat.shape[0]):
        tmp_value[i] = np.polyval(poly_mat[i, :], eval_point)
    exp_value = np.array(exp_value, dtype=np.complex128)
    #err = np.dot(exp_value, tmp_value)
    #return err[0]
    return sum(exp_value*(tmp_value.reshape(-1))) # do not use np.dot here. TODO: explain why
