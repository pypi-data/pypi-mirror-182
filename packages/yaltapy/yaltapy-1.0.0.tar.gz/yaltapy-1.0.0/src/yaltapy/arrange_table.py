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
import warnings
warnings.filterwarnings('ignore')

from .eval_diff import eval_diff
from .decorators.control_inputs import controler_types


@controler_types(np.ndarray, np.ndarray, np.ndarray, float, np.ndarray)
def arrange_table(poly_mat, poly_mat_der, crossing_table, alpha, delay_vect):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Computes the points of crossing of the imaginary axis.

    table_cross = arrange_table(iPolyMatrix, iPolyMatrixDer, iTableCrossing,
                                iAlpha, iDelayVect)
    takes in input the quasi polynomial, its derivative, the initial
    crossing table the fractional power alpha, the delay vector, and sorts
    the crossing table and add delay and frequency and direction values.
    delay and frequency and direction values.

    arrange_table returns table_cross as a matrix:
    - 1st column : gives the first value of the delay for which a specific zero
    crosses the axis.
    - 3rd column : gives the frequency of crossing of a zero.
    - 2nd column : is equal two times pi over frequency.
    - 4rth column : gives the crossing direction, -1 is from right to left
    and +1 from left to right.

    Example:

    See also crossing_table.

    """

    table_cross = []
    if crossing_table.shape[0]:
        crossing_table = np.atleast_2d(crossing_table)
    for i in range(crossing_table.shape[0]):
        freq = float(np.imag(crossing_table[i, 1] ** (1 / alpha)))
        theta = crossing_table[i, 0]
        if freq < 0:
            tau = (theta - 2 * np.pi) / freq
        else:
            tau = np.real(theta / freq)
        tau = float(np.real(tau))
        direction = np.sign(np.real(eval_diff(tau, 1j * freq, poly_mat, \
                              poly_mat_der, alpha, delay_vect)))
        new_dir = [tau, np.absolute(2 * np.pi / freq),
                   np.absolute(freq), direction]
        table_cross = np.concatenate((table_cross, new_dir))
    table_cross = np.array(table_cross)
    table_cross = table_cross.reshape(crossing_table.shape[0], 4)
    if len(table_cross) != 0:
        ind = np.argsort(table_cross[:, 0])
        table_cross = table_cross[ind, :]

    return table_cross
