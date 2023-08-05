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

@controler_types(np.ndarray, np.ndarray)
def order_vec(vec1, vec2):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Orders elements of two vectors.

    ordered_vec = order_vec(vec1,vec2) rearrange the second vector elements
    such that the sum of distances between elements of same indices of both
    vectors is minimal.

    Example:
    if vec1 = [1 8 3] and vec2 = [2 1 4],
    then ordered_vec = [1 4 2].

    """

    len_vec2 = len(vec2)
    len_vec1 = len(vec1)
    if len(vec1) > len(vec2):
        raise ValueError('size of array at index 1 should be larger or equal to\
                         the array at index 0')
    tmp = np.zeros((len_vec1, len_vec2))
    ordered_vec = np.zeros(len(vec2), dtype=np.complex128)
    for i in range(len_vec2):
        tmp[:, i] = np.absolute([v1 - vec2[i] for v1 in vec1])

    ind_y, idx1 = np.amin(tmp, axis=1), tmp.argmin(axis=1)
    if len(idx1) == len(np.unique(idx1)): # if no duplicate
        ordered_vec = vec2[idx1]
        return ordered_vec

    for i in range(len_vec2):
        ind_y, idx1 = np.amin(tmp, axis=1), tmp.argmin(axis=1)
        idx2 = ind_y.argmin(axis=0)
        ordered_vec[idx2] = vec2[idx1[idx2]]
        tmp[idx2, :] = np.inf
        tmp[:, idx1[idx2]] = np.inf

    return ordered_vec

