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

from control.matlab import tf

def compute_tf(num, den):
    """Computes the transfer function.
    The function takes in input the numerator an denominator of the Pade-2
    approximation and returns the transfer function of the approximation.

    Example:
    if num = [0.5, 0.1, 2] and den = [0.5, 2.2, 0.7],
    COMPUTETF(iNum, iDen) returns the transfer function :
         s^2 + 0.2 s + 4
        -----------------
        s^2 + 4.4 s + 1.4"""
    #import pdb;pdb.set_trace()
    my_tf = 0
    for i in range(num.shape[0]):
        my_tf += tf(num[i, :], den[i, :])
    # Normalisation
    num, den = my_tf.num[0][0], my_tf.den[0][0]
    my_tf = tf(num / den[0], den / den[0])

    return my_tf
