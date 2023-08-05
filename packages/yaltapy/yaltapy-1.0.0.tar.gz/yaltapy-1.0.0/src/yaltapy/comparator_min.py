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
from .fminbnd import fminbnd

def comparator_min(predicted_pt, poly_mat, delay_vect, alpha,
                   precision, positive_path=1):
    # pylint: disable=E1101,E0611,R0913
    # ignoring warnings concerning numpy module and scipy minimize function.
    # ignoring too much args warning for func comparator_min
    """Check validity of the predicted point of the curve

    precision is the size of the ball around the predicted point. Either
    there is a zero inside or not. If there is such zero, then the valid
    point output is non zero.

    Example:

    See also comparator_min_test_pva.

    """

    alpha = float(alpha)
    valid_point = np.zeros(3)
    lower_bnd = predicted_pt - precision*10
    upper_bnd = predicted_pt + precision*10
    # Security on Tau
    lower_bnd[2] = predicted_pt[2] + precision/1000.
    upper_bnd[2] = predicted_pt[2] + precision
    if positive_path != 1:
        lower_bnd[2] = predicted_pt[2] - precision
        upper_bnd[2] = predicted_pt[2] - precision/100.
    xopt, fopt, warnflag = fminbnd(eval_compare_func_min, predicted_pt,
                                   lower_bnd, upper_bnd, args=(poly_mat,
                                                               delay_vect,
                                                               alpha), disp=False)
    if not warnflag and fopt < precision:
        valid_point = xopt
    return valid_point
