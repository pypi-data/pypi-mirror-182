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
import scipy.optimize as so

HALF_PI = np.pi/2
TWO_PI = np.pi*2

def sc_x0(x0, lb, ub):
    if ub <= x0:
        return HALF_PI
    if lb >= x0:
        return -HALF_PI
    return TWO_PI+np.arcsin(max([-1,min(1, 2*(x0-lb)/(ub-lb)-1)]));

proc_x0 = np.vectorize(sc_x0)

def sc_x(x, lb, ub):
    return max(lb,min(ub, (np.sin(x)+1)/2*(ub-lb)+lb))

proc_x = np.vectorize(sc_x)

def proc_fun(cost, l_bnd, u_bnd, args):
    def tr_fun(x):
        return cost(proc_x(x, l_bnd, u_bnd), *args)
    return tr_fun

def fminbnd(cost, x0, l_bnd, u_bnd, args=(), **kwds):
    """
    Uses a Nelder-Mead simplex algorithm to find the minimum of a function of one
    or more variables but with bound constraints by transformation.

    Freely inspired from an idea of:
    John D'Errico (2021). fminsearchbnd, fminsearchcon
    (https://www.mathworks.com/matlabcentral/fileexchange/8277-fminsearchbnd-fminsearchcon),
    MATLAB Central File Exchange. Retrieved February 23, 2021.
    """
    assert 'retall' not in kwds
    assert 'full_output' not in kwds
    assert x0.shape == l_bnd.shape == u_bnd.shape
    x0 = proc_x0(x0, l_bnd, u_bnd)
    fun_ = proc_fun(cost, l_bnd, u_bnd, args)
    xopt, fopt, iter_, funcalls, warnflag = so.fmin(fun_, x0,
                                                             full_output=True,
                                                             retall=False, **kwds)
    xopt = proc_x(xopt, l_bnd, u_bnd)
    return xopt, fopt, warnflag

