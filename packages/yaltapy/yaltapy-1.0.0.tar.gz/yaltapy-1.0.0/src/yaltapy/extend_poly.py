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

# pylint: disable=E0611
# ignoring warnings concerning numpy module.

import numpy as np
from .decorators.control_inputs import controler_types

@controler_types(np.ndarray, int)
def extend_poly(in_poly, length):
    """Extends the length of a polynomial.

    out_poly = extend_poly(in_poly, length) resizes the polynomial in_poly by
    adding leading zeros. Leading zeros are added if the integer length is
    bigger than the length of the input polynomial, otherwise nothing is done.

    Example:
    If in_poly = numpy.array([4 2 1]) and length = 5,
    then out_poly = [0 0 4 2 1].

    See also reduce_deg_poly, simplify_system

    """

    if not isinstance(length, int) or length < 0:
        raise TypeError("n must be a positive integer")
    if in_poly.ndim != 1:
        raise TypeError("iPoly must be a 1D array")

    k = in_poly.shape[0]
    diff = length - k
    out_poly = in_poly
    if diff > 0:
        # pylint: disable=E1101
        # ignoring warnings concerning numpy module.
        new = np.zeros(diff)
        out_poly = np.concatenate((new, in_poly))
        # pylint: enable=E1101

    return out_poly
