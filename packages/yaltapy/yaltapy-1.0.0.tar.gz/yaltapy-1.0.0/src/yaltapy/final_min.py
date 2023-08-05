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
from .eval_compare_func_min import eval_compare_func_min
from .decorators.control_inputs import controler_types
from .fminbnd import fminbnd

@controler_types(np.ndarray, np.ndarray, np.ndarray, float, float)
def final_min(predicted_pt, poly_mat, delay_vect, alpha, tau):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Check validity of the predicted point of the curve

    TO WRITE
    iPrecision is the size of the ball around the predicted point.
    Either there is a zero inside or not. If there is such zero,
    then the valid point is non zero

    """
    valid_point = np.zeros(3)
    ref_pt = np.zeros((12, 3))
    compare_result = np.zeros(12)
    exit_flag = np.zeros(12)
    for i in range(12):
        prec = 10 ** (-(i + 2))
        lwer_bnd = predicted_pt - prec
        uper_bnd = predicted_pt + prec
        # Security on tau
        lwer_bnd[2], uper_bnd[2] = tau, tau
        xopt, fopt, warnflag = fminbnd(eval_compare_func_min, predicted_pt,
                                   lwer_bnd, uper_bnd, args=(poly_mat,
                                                               delay_vect,
                                                               alpha), disp=False)
        compare_result[i] = fopt
        exit_flag[i] = (not warnflag)
        ref_pt[i, :] = xopt
    non_zero = [i for i, j in enumerate(compare_result) if j != 0]
    #non_zero = [i for i, j in enumerate(compare_result) if (j - 0) > prec]
    min_idx = np.argmin(compare_result[non_zero])
    ref_pt = ref_pt[non_zero, :]
    pt_a = ref_pt[min_idx, :]
    exit_flag = exit_flag[non_zero]
    if exit_flag[min_idx] == 1:
        valid_point = pt_a
    return valid_point
