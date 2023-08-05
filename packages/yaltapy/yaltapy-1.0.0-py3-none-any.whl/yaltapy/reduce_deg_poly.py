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

@controler_types(np.ndarray, prec=float)
def reduce_deg_poly(poly, prec=1e-12):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Eliminates leading zeros of an array.

    out_poly = reduce_deg_poly(poly, precision) returns a reduced polynom of
    the polynom poly.The function eliminates all leading zeros (numbers lower
    than precision prec).
    If precision is not specified, default precision is set to 1e-12.

    Example:
    If poly = [0.02 0.3 0.5 1] and precision = 0.04,
    then reduce_deg_poly(poly, precision) returns [0.3 0.5 1],
    and reduce_deg_poly(poly) returns [0.02 0.3 0.5 1].

    See also extend_poly, simplify_system.

    """

    count = 0 # number of leading numbers smaller than prec to remove.
    for i in range(len(poly)):
        if abs(poly[i]) < prec:
            count += 1
        else:
            break
    # we remove the leading terms until count.
    out_poly = np.delete(poly, range(count))

    return out_poly
