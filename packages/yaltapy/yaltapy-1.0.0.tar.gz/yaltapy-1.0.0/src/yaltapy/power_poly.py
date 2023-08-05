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

@controler_types(np.ndarray, int)
def power_poly(poly, power):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Raises the polynom to the desired power.

    out_poly = power_poly(poly, power) takes the polynomial poly and
    raises it to the power power.

    Example:
    If poly = [1 2 3] = x^2 + 2x + 3 and power = 2,
    then out_poly = power_poly(poly, power) returns [1 4 10 12 9]

    """
    out_poly = 1
    for i in range(power):
        out_poly = np.convolve(out_poly, poly)

    return out_poly

