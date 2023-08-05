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

# pylint: disable=E0611, E1101
# ignoring warnings concerning numpy module.

import numpy as np
#from .decorators.control_inputs import controler_types

#@controler_types(np.ndarray, np.ndarray, np.ndarray, float)
def eval_compare_func_min(point, poly_mat, delay_vect, alpha):
    # pylint: disable=E0611
    # ignoring warnings concerning numpy module.
    """Evaluation of the quasi-polynomial for the compared function.

    out_value = eval_compare_func_min(point, poly_mat, delay_vect, alpha)
    Since we need a real value, we will evaluate the absolute value of the
    quasi-polynomial in some specific point.

    Example:

    See also eval_diff.

    """
    delay_vect = np.concatenate((np.zeros(1), delay_vect))
    #import pdb;pdb.set_trace()
    poly = -point[2] * (point[0] + point[1]*1.0j)**(1.0/alpha) * delay_vect
    #poly = map(exp, poly)
    #poly = [exp(val) for val in poly]
    poly = np.exp(poly)
    # fix issue which explained significant differences between matlab and py variant
    # of thread_RootLoci()
    pp = np.dot(poly, poly_mat)
    xx = np.array([point[0] + point[1]*1.0j], dtype=np.complex128)
    out_value = abs(np.polyval(pp, xx))
    return out_value[0]
