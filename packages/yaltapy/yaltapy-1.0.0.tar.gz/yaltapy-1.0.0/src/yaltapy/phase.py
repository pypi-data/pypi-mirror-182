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

from math import atan2
import numpy as np
from operator import sub

def phase(complex_vec):
    """ Computes the phase of a complex vector.

    complex_vec is a complex-valued row vector and phi is returned as its
    phase (in radians), with an effort made to keep it continuous
    over the pi-borders."""

    if complex_vec.ndim > 1:
        raise IndexError("phase only applies to row or column vectors")
    phi = [atan2(np.imag(i), np.real(i)) for i in complex_vec]
    siz = len(phi)
    df = list(map(sub, phi[:-1], phi[1:]))
    ind = [i for i, j in enumerate(df) if abs(j) > 3.5]
    for l in ind:
        phi += 2 * np.pi * np.sign(df[l]) * np.concatenate((np.zeros(l+1), np.ones(siz-l-1)))

    return phi

