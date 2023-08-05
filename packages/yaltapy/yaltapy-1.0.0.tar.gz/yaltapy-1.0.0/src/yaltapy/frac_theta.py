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
#import math
import cmath as cm

from .order_vec import order_vec

def frac_theta(point, data):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Evaluation function of imaginary roots of a quasi polynomial.

    val = frac_theta(point,data) takes in input the evaluation point point
    and the object data containing the quasi polynomial and its
    dependencies.
    The output val it the value of the evaluation function at the input
    point point.

    Example:

    """

    i_point = -1j * (point * data.delay_vect)
    res = order_vec(data.roots, np.roots(np.dot([cm.exp(i) for i in i_point], \
                                                data.poly_mat)))
    out_val = np.absolute(np.angle(res)) - data.angle_max
    out_val = out_val[data.index]

    return out_val
