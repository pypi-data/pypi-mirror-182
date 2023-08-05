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
import cmath

from .decorators.control_inputs import controler_types

@controler_types(float, complex, np.ndarray, np.ndarray, float, np.ndarray)
def eval_diff(tau, ev_point, poly_mat, poly_mat_der, alpha, delay_vect):
    # pylint: disable=E1101,R0913
    # ignoring warnings concerning numpy module.
    # ignoring warnings concerning too manya args for func eval_diff.
    """Evaluation of the derivative of a quasi polynomial.

    out_diff = eval_diff(tau, ev_point, poly_mat, poly_mat_der,
                         alpha, delay_vect)
    takes in input the delay tau, the evaluation point, the quasi polynomial,
    its derivative, the fractional power, the delay vector, and returns
    the evaluation of the derivative of the polynomial iPolyMatrix at the
    evaluation point iEvPoint.

    See also eval_compare_func_min

    """

    dim = poly_mat.shape[0] - 1
    ev_exp = -tau * ev_point * delay_vect
    ev_exp = [cmath.exp(x) for x in ev_exp]
    poly_tmp = np.zeros(dim, dtype=np.complex128)
    poly_tmp_diff = np.zeros(dim, dtype=np.complex128)
    alpha_ev_point = ev_point ** alpha

    for i in range(dim):
        poly_tmp[i] = np.polyval(poly_mat[i+1, :], alpha_ev_point)
        poly_tmp_diff[i] = np.polyval(poly_mat_der[i+1, :], alpha_ev_point)

    num = ev_point * sum(delay_vect * poly_tmp * ev_exp)

    den = ev_point**(alpha-1) * np.polyval(poly_mat_der[0, :], alpha_ev_point) + \
          sum((ev_point**(alpha-1) * poly_tmp_diff - \
               tau * delay_vect * poly_tmp) * ev_exp)

    out_diff = num / den

    return out_diff

