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
#from scipy.optimize import minimize
from .fminbnd import fminbnd
from .eval_compare_func_min import eval_compare_func_min
from .error_eval_phase import error_eval_phase


def comparator_min_test_pva(predicted_pt, poly_mat, delay_vect,
                            alpha, precision, positive_path=1):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Check validity of the predicted point of the curve.

    precision is the size of the ball around the predicted point. Either
    there is a zero inside or not. If there is such zero, then the valid
    point output is non zero.
    In this function, the test for the zero inside the ball is done via
    the pva function that uses change of the analytic complex function
    evaluated.

    Example:

    See also comparator_min_test.

    """

    alpha = float(alpha)
    valid_pt = np.zeros(3)
    precision_max = int(np.ceil(np.real(-np.log10(precision))) + 1)

    lwer_bnd = predicted_pt - [precision*100 for i in range(len(predicted_pt))]
    uper_bnd = predicted_pt + [precision*100 for i in range(len(predicted_pt))]
    # Security on Tau
    lwer_bnd[2] = predicted_pt[2] + precision/1000.0
    uper_bnd[2] = predicted_pt[2] + precision
    if positive_path != 1:
        lwer_bnd[2] = predicted_pt[2] - precision
        uper_bnd[2] = predicted_pt[2] - precision/1000.0

    #fun = lambda x: eval_compare_func_min(x, poly_mat, delay_vect, alpha)
    #bnds = [(lwer_bnd[i], uper_bnd[i]) for i in range(len(lwer_bnd))]
    #bnds = tuple(bnds)
    #res = minimize(fun, predicted_pt, method='L-BFGS-B', bounds=bnds)
    ####res = minimize(fun, predicted_pt, method='SLSQP', bounds=bnds)
    xopt, fopt, warnflag = fminbnd(eval_compare_func_min, predicted_pt,
                                   lwer_bnd, uper_bnd, args=(poly_mat,
                                                               delay_vect,
                                                               alpha), disp=False)
    #if res.success and np.absolute(res.fun) < precision:
    #    valid_pt = res.x
    if not warnflag and fopt < precision:
        valid_pt = xopt
    else:
        #eval_pt = res.x[0] + res.x[1] * 1j
        eval_pt = xopt[0] + xopt[1] * 1j
        # numpy to python cast on types
        eval_pt = np.complex128(eval_pt)
        tau = float(xopt[2])

        err = error_eval_phase(eval_pt, poly_mat, tau,
                               alpha, delay_vect, precision=precision_max)
        if not warnflag and err < precision:
            valid_pt = xopt
    return valid_pt
