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

from .data import MSG
from .simplify_system import *
from .get_pade_coeff import *
from .norm_inf import *
from .compute_tf import *
from .get_roots_error import *
import numpy as np
from control.matlab import tfdata

def compute_pade(i_poly_matrix, i_delta, i_tau, i_delay_vector,
                 i_mod_arg, i_mode='ORDER'):
    """
    %   COMPUTEPADE Computes the Pade-2 approximation of a non fractionnal
    %   SISO delay system with transfer function G of the type :
    %
    %             p(s) + SUM_j(q_j(s)*exp(-j*tau*s))
    %   C(s) =  -----------------------------------   j=1:N
    %                   (s + 1) ^ iDelta
    %
    %   with iDelta >= (n + 1) where n is the degree of p(s).
    %
    %   There are two modes for computing the Pade approximation (iMode argument).
    %   iMode is either 'ORDER' and thus iModArg is the order of the
    %   approximation, or iMode is 'NORM' and iModArg represents the maximum
    %   limit of the difference (H-infinity-norm) between C(s) and its
    %   approximation.
    %
    %   Output oPadeStruct is a compact structure with following informations:
    %   - NumApprox : vector of coefficients of the numerator of the transfer
    %     function of the approximation.
    %   - DenApprox : vector of coefficients of the denominator of the transfer
    %     function of the approximation.
    %   - ErrorNorm : the H-infinity-norm of the difference between C(s) and
    %     its approximation.
    %   - PadeOrder : the order of the approximation.
    %   - Roots : the roots of the approximation.
    %   - RootsError : an array of differences between the computed roots of
    %     C(s) (by the function thread_RootLoci) and the roots of the
    %     approximation.
    %
    %   Syntax:
    %   oPadeStruct = COMPUTEPADE(iPolyMatrix, iDelta, iTau, iDelayVector, ...
    %                             iModArg, iMode)
    %
    %   Example:
    %   If iPolyMatrix = [6, -66, 180;
    %                     0,  -2, 12;
    %                     0,  6,  30;
    %                     0,  0,  -2];
    %
    %   and iDelayVector = [1, 2, 3];
    %
    %   then oPadeStruct = computePade(iPolyMatrix, 3, 1, iDelayVector, 4, 'ORDER')
    %   ans =
    %
    %   NumApprox: [1x37 double]
    %   DenApprox: [1x37 double]
    %   ErrorNorm: 8.7100e-04
    %   PadeOrder: 4
    %   Roots: [5.9996 5.0032]
    %   RootsError: [2.9745e-04 4.9066e-04]

    %   Copyright 2013-2014 YALTA v.1.0.0 (31/01/2013)
    """
    # PARAM

    class OutputPade(object):
        def __init__(self):
            self.num_approx = np.nan
            self.den_approx = np.nan
            self.error_norm = np.nan
            self.pade_order = np.nan
            self.roots = np.nan
            self.roots_error = np.nan
            self.error_catched = np.nan
        def to_dict(self):
            return self.__dict__

    o_pade = OutputPade()
    k_order_max = 20;
    k_alpha = 1; # hypothesis: we work on non fractionnal systems.

    # iDelta must be strictly greater than the degree of the quasi polynomial.
    # ie iDelta >= deg(q0) + 1
    if len(i_poly_matrix.shape)!=2:
        raise ValueError(MSG.matrix_required)
    if i_delta < i_poly_matrix.shape[1]:
        raise ValueError(MSG.degAproxToLow)

    # %%%%%%%%%%%%%%%%%%%% CHECKINGS ON SYSTEM's TYPE %%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Simplifying inputs
    a_poly_matrix, a_tau, a_delay_vector = simplify_system(i_poly_matrix, i_tau, i_delay_vector.flatten());
    if i_mode=='ORDER':
        a_pade_num, a_pade_den = get_pade_coeff(a_poly_matrix, i_delta, a_tau, a_delay_vector, i_mod_arg)
        # iModArg is here the order of approximation.
        o_pade.error_norm = norm_inf(a_poly_matrix, a_delay_vector, a_tau, k_alpha, i_mod_arg, i_delta)
        o_pade.pade_order = i_mod_arg
    elif i_mode=='NORM':
        a_error = np.inf
        a_order = 0
        # iModArg is here the desired Hinfinity norm of the error.
        while (a_error > i_mod_arg) and (a_order <= k_order_max):
            a_order += 1;
            a_error = norm_inf(a_poly_matrix, a_delay_vector, a_tau, k_alpha, a_order, i_delta)
            a_pade_num, a_pade_den = get_pade_coeff(a_poly_matrix, i_delta, a_tau, a_delay_vector, a_order)
            o_pade.error_norm = a_error
            o_pade.pade_order = a_order
    else:
        raise ValueError(MSG.errorModePade)


    o_pade.roots = MSG.optNotSelected
    o_pade.roots_error = MSG.optNotSelected

    ## Check if user has control system toolbox installed. If so, NumApprox,
    ## DenApprox, Roots and RootsError are computed.
    a_tf = compute_tf(a_pade_num, a_pade_den)
    # %[oPadeStruct.NumApprox, oPadeStruct.DenApprox] = tfdata(aTF, 'v');
    #num_approx, den_approx = tfdata(a_tf, 'v')
    o_pade.num_approx, o_pade.den_approx = a_tf.num[0][0], a_tf.den[0][0] #num_approx[0][0]
    #o_pade.den_approx = #den_approx[0][0]
    a_roots, a_roots_error = get_roots_error(a_tf, a_poly_matrix, a_tau, a_delay_vector, k_alpha)
    o_pade.roots = a_roots
    o_pade.roots_error = a_roots_error
    return o_pade


