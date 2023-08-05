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
from .error_eval import error_eval

EPS = np.finfo(float).eps

def _pow(nb, pw):
    if pw or not np.isnan(nb):
        return nb**pw
    return np.nan


#@controler_types(np.ndarray, np.ndarray, float, float, int, int)
def norm_inf(poly_mat, delay_vect, tau, alpha, order, degree):
    # pylint: disable=E1101, R0913
    # ignoring warnings concerning numpy module.
    """TO COMMENT.

    """

    max_im_value = 100
    nb_pts = 10_000
    step = 2 * max_im_value / nb_pts
    norm = 0.
    norm_ref = 0.
    poly_den = np.poly1d(-np.ones(degree), True)
    tmp_norm = np.zeros(nb_pts + 1)
    tmp_ref_norm = np.zeros(nb_pts + 1)
    delay_vect_a = np.concatenate((np.zeros(1), delay_vect))
    tau_k = delay_vect_a * tau

    for i in range(int(nb_pts) + 1):
        eval_point = (-max_im_value + (i * step))*1j
        sum_pade = np.complex128(0.)
        neg_polynoms = [[tau_k[k]**2, -6*tau_k[k]*order, 12*order**2] \
                        for k in range(poly_mat.shape[0])]
        pos_polynoms = [[tau_k[k]**2, 6*tau_k[k]*order, 12*order**2] \
                        for k in range(poly_mat.shape[0])]
        for j in range(poly_mat.shape[0]):
            sum_pade += np.polyval(poly_mat[j, :], eval_point) / \
                        np.polyval(poly_den, eval_point) * \
                       _pow(np.polyval(neg_polynoms[j], eval_point)/ \
                            np.polyval(pos_polynoms[j], eval_point), order)
            if np.isnan(sum_pade):
                break
        eval_error = error_eval(eval_point, poly_mat, tau, alpha, delay_vect)
        tmp_norm[i] = abs(eval_error / np.polyval(poly_den, eval_point) - sum_pade)
        tmp_ref_norm[i] = abs(eval_error / np.polyval(poly_den, eval_point))

        if tmp_norm[i] > norm:
            norm = tmp_norm[i]
        if tmp_ref_norm[i] > norm_ref:
            norm_ref = tmp_ref_norm[i]
    norm = norm / norm_ref if norm_ref>=EPS else np.inf
    return norm
