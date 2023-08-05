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
from .error_eval import error_eval
from .pva import pva
from .decorators.control_inputs import controler_types

#@controler_types(np.complex128, np.ndarray, float, float, np.ndarray, precision=int)
def error_eval_phase(eval_point, poly_mat, tau, alpha, delay_vect, precision=13):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Computes the error evaluation.

    err = error_eval_phase(eval_point, poly_mat, tau, alpha, delay_vect, precision)
    takes in input the evaluation point eval_point, the quasi polynomial
    poly_mat, the base delay tau, the fractional power alpha, the
    vector delay delay_vect and a precision, and returns the absolute error err.
    The absolute error is the evaluation of the quasi polynomial at an
    unstable pole value.
    Default precision is 13.

    Example:

    """

    # Initialisation
    err = 0
    fun = lambda x: error_eval(x, poly_mat, tau, alpha, delay_vect)

    for prec in range(1, precision + 1):
        a_prec = 10 ** -prec
        nbz = pva(fun, eval_point, a_prec)
        if nbz < 1:
            err = 10 ** -(prec - 1)
            break
    if not err:
        err = a_prec

    return err
