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

from __future__ import division
import os
import numpy as np
from . import crossing_table
from .simplify_system import simplify_system
from .poly_vect_der import poly_vect_der
from .arrange_table import arrange_table
from .system_type import system_type
from .stability_chains import stability_chains
from .stability_windows import stability_windows
from .data import Messages
from .data import FieldsStabilityWindows


def thread_stability_windows(poly_mat, delay_vect, alpha,
                             tau, tminsw=0., tmaxsw=0., plot=1):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Comptutes the stability windows of a SISO delayed system.

    The function computes the stability windows of a SISO delayed system given
    by its transfer function G :

           t(s) + SUM(t_i(s)*exp(-i*tau*s))
    G(s) = ----------------------------------    i=1:N' , j=1:N
           p(s) + SUM(q_j(s)*exp(-j*tau*s))

    The delay system must be of :
    - retarded type.
    - neutral type with a finite number of poles in { Re s > -a, a>0}.

    Syntax:
    res = thread_stability_windows(poly_mat,delay_vect,alpha,tau,tmaxsw,tminsw,plot)
    res = thread_stability_windows(poly_mat,delay_vect,alpha,tau,tmaxsw,tminsw)
    res = thread_stability_windows(poly_mat,delay_vect,alpha,tau,tmaxsw)
    res = thread_stability_windows(poly_mat,delay_vect,alpha,tau)

    Inputs:
    - poly_mat: the quasi polynomial
           p(s) + q_1(s)*exp(-tau*s) + ... + q_N(s)*exp(-N*tau*s)
    - delay_vect: the delay vector, which is a vector of values of k for
      which q_(j) is not null of length N (p(s) is assumed non zero).
    - alpha: a real between 0 and 1 describing the fractionnal power alpha
      for the fractionnary equation in s^(alpha).
    - tau: the value of the nominal delay tau.
    - tmaxsw: maximum delay of stability window, default value = tau
    - tminsw: minimum delay of stability window, default value = 0
    - plot: option to plot the stability windows, default value = 1

    Output : Structure giving information on the :
    - type of the system: retarded, neutral
      or advanced (in case the user was wrong in defining his/her system).
    - roots of the system without delay
    - position of the asymptotic axes of chains of poles (in the case of
      neutral systems)
      and if applicable the information that the system has a infinite number
      of unstable poles
    - the position of the chain of poles relative to the asymptotic axis
      in the case the asymptotic axis is the imaginary axis.

    And for retarded systems or neutral systems with a finite number of
    unstable poles in { Re s > -a, a>0}:
    - crossing table
    - stability window for a delay between 0 and the maximum delay tmaxsw
    - value of the delays for which the number of unstable poles changes

    """

    # ######################## PRE-TREATMENTS #############################

    # PARAM
    strings = Messages()

    # Initialization: we will access data with res[fields.type] for instance
    ob = FieldsStabilityWindows()
    fields, res = ob.get_fields_and_dict()

    # tmaxsw not specified
    if tmaxsw == 0:
        tmaxsw = tau

    # Reshape delay_vect from 2D to 1D
    delay_vect = delay_vect.flatten()

    # ##################### 1st phase of computations #######################
    # Simplify inputs
    poly_mat, tau, delay_vect = simplify_system(poly_mat, tau, delay_vect)

    # Find the type of the system
    res[fields.type] = system_type(poly_mat)

    # Find poles of the system with no delay
    roots_alpha = np.roots(sum(poly_mat, 0))
    if alpha != 1:
        roots_alpha = [roots_alpha[i] for i, j in enumerate(roots_alpha)
                       if abs(np.angle(j)) < np.pi*alpha]

        roots_alpha = np.array(roots_alpha)

    roots_no_delay = roots_alpha ** (1 / alpha)
    res[fields.roots_no_delay] = roots_no_delay

    # End of Phase 1: Advanced Systems cannot go any further
    if res[fields.type] == strings.types[1]:
        raise TypeError(strings.cant_compute_stabwin + strings.asymp[4])

    #########################################################################

    # Phase 2: Chains of poles
    if res[fields.type] == strings.types[2]:
        roots_chain, asymp_stab = stability_chains(poly_mat, delay_vect,
                                                   tau, alpha)

        res[fields.roots_chain] = roots_chain

        # End of phase 2: All chaines must be in the LHP (stability for
        # chains around the Imaginary axis are "ignored" for the moment).
        if asymp_stab == -1:
            # Asymptotic axis is strictly on the right half plane.
            # Infinite nb. of poles in RHP.
            raise TypeError(strings.cant_compute_stabwin + strings.asymp[0])
        elif asymp_stab == 0:
            # Asymptotic axis IS the imaginary axis.
            # Impossible to check the position of poles.
            raise TypeError(strings.cant_compute_stabwin + strings.asymp[1])
        elif asymp_stab == 2:
            # Asymptotic axis IS the imaginary axis.
            # Chain of asymptotic poles are on the left of the imaginary axis.
            raise TypeError(strings.cant_compute_stabwin + strings.asymp_imag_by_left)

    else:
        res[fields.roots_chain] = strings.roots

    # Phase 3: Building table for crossings at the imaginary axis.
    table_crossing = crossing_table(poly_mat, delay_vect, alpha)
    #cross_tab = strings.cross
    cross_tab = np.array([])
    poly_mat_der = poly_vect_der(poly_mat)
    if table_crossing.size:  # not empty
        cross_tab = arrange_table(poly_mat, poly_mat_der, table_crossing,
                                  alpha, delay_vect)

    res[fields.crossing_tab] = cross_tab

    # Stability windows and nb. of unstable poles (poles of small modulus)
    nb_unstab_roots_no_del = sum(np.real(roots_no_delay) > 0)
    stab_win, delnbp = stability_windows(cross_tab, int(nb_unstab_roots_no_del),
                                         tmaxsw, tau_min=tminsw, iplot=plot)

    res[fields.stab_win] = stab_win
    res[fields.nb_unstab_poles] = delnbp

    return res

if __name__ == '__main__':
    poly_mat = np.array([[1, 3, 2, -1], [0, 3, -4, 2],[0.5, 0.7, 1.2, -0.8],
                         [0.5, 1.34, -0.7, 1.9],[0, 0, 3.4, -1.6]])
    delay_vect = np.array([1, 2, 3, 6])
    tau = 4.
    alpha = 1.
    tmaxsw = 6.
    res = thread_stability_windows(poly_mat, delay_vect, alpha, tau)
    for i, j in res.iteritems():
        print(i, j)
