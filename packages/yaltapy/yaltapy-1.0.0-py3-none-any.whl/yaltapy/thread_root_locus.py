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
from .crossing_table import crossing_table
from .simplify_system import simplify_system
from .poly_vect_der import poly_vect_der
from .arrange_table import arrange_table
from .system_type import system_type
from .stability_chains import stability_chains
from .integrate_unstable_poles_min import integrate_unstable_poles_min
from .error_eval_phase import error_eval_phase
from .data import Messages
from .data import FieldsRootLocus


def thread_root_locus(poly_mat, delay_vect, alpha, tau,
                      plot=1, delta_tau=1e-4):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Comptutes the root locus of a SISO delayed system.

    The function computes the root locus of a SISO delayed system given
    by its transfer function G :

           t(s) + SUM(t_i(s)*exp(-i*tau*s))
    G(s) = ----------------------------------    i=1:N' , j=1:N
           p(s) + SUM(q_j(s)*exp(-j*tau*s))

    The delay system must be of :
    - retarded type.
    - neutral type with a finite number of poles in { Re s > -a, a>0}.

    Syntax:
    res = thread_root_locus(poly_mat, delay_vect, alpha, tau, plot, delta_tau)
    res = thread_root_locus(poly_mat, delay_vect, alpha, tau, plot)
    res = thread_root_locus(poly_mat, delay_vect, alpha, tau)

    Inputs:
    - poly_mat: the quasi polynomial
           p(s) + q_1(s)*exp(-tau*s) + ... + q_N(s)*exp(-N*tau*s)
    - delay_vect: the delay vector, which is a vector of values of k for
      which q_(j) is not null of length N (p(s) is assumed non zero).
    - alpha: a real between 0 and 1 describing the fractionnal power alpha
      for the fractionnary equation in s^(alpha).
    - tau: the value of the nominal delay tau.
    - plot(optional): option to plot the root locus for delays from 0 to tau,
      default value = 1
    - delta_tau(optional): precision of integration procedure for computing
      root locus, default value = 1e-4

    Output : Structure giving information on the :
    - roots of the system without delay

    And for retarded systems or neutral systems with a finite number of
    unstable poles in { Re s > -a, a>0}:
    - crossing table
    - set of all imaginary roots for a delay between 0 and the nominal delay
      tau.
    - position of unstable poles where the delay is equal to tau
    - error on the unstable poles
    - root locus

    """

    # ######################## PRE-TREATMENTS #############################

    # PARAM
    strings = Messages()

    # Initialization: we will access data with res[fields.type] for instance
    ob = FieldsRootLocus()
    fields, res = ob.get_fields_and_dict()

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
        roots_alpha = [roots_alpha[i] for i, j in enumerate(roots_alpha) \
                       if abs(np.angle(j)) < np.pi*alpha]

        roots_alpha = np.array(roots_alpha)

    roots_no_delay = roots_alpha ** (1 / alpha)
    res[fields.roots_no_delay] = roots_no_delay

    # End of Phase 1: Advanced Systems cannot go any further
    if res[fields.type] == strings.types[1]:
        raise TypeError(strings.cant_compute_root_locus + strings.asymp[4])

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
            raise TypeError(strings.cant_compute_root_locus + strings.asymp[0])
        elif asymp_stab == 0:
            # Asymptotic axis IS the imaginary axis.
            # Impossible to check the position of poles.
            raise TypeError(strings.cant_compute_root_locus + strings.asymp[1])
        elif asymp_stab == 2:
            # Asymptotic axis IS the imaginary axis.
            # Chain of asymptotic poles are on the left of the imaginary axis.
            raise TypeError(strings.cant_compute_root_locus + strings.asymp_imag_by_left)

    # Phase 3: Building table for crossings at the imaginary axis.
    table_crossing = crossing_table(poly_mat, delay_vect, alpha)
    cross_tab = strings.cross
    poly_mat_der = poly_vect_der(poly_mat)
    if table_crossing.size:  # not empty
        cross_tab = arrange_table(poly_mat, poly_mat_der, table_crossing,
                                  alpha, delay_vect)

    res[fields.crossing_tab] = cross_tab

    # Imaginary roots
    tmp_unstable = sum(np.real(roots_no_delay) >= 0)
    imag_roots = []

    if isinstance(cross_tab, np.ndarray):
        for i in range(cross_tab.shape[0]):
            tmp_delay = cross_tab[i, 0]
            while tmp_delay < tau:
                tmp_unstable += 2 * cross_tab[i, 3]
                imag_roots += [[tmp_delay, cross_tab[i, 2], cross_tab[i, 3]]]
                imag_roots += [[tmp_delay, -cross_tab[i, 2], cross_tab[i, 3]]]
                tmp_delay += cross_tab[i, 1]
    imag_roots = np.array(imag_roots)
    res[fields.imag_roots] = imag_roots

    if imag_roots.size:
        # sort imag_roots along the first column
        idx = np.argsort(imag_roots, axis=0)  # sorted indices along columns
        res[fields.imag_roots] = np.array(imag_roots)[idx[:, 0]]
    # Phase 4: Integrate unstable poles until point of interest
    if plot:
        unstab_poles_alpha, rtlc = integrate_unstable_poles_min(res, poly_mat,
                                   roots_alpha, alpha, delay_vect, tau, plot,
                                   delta_tau)
        #return res  # temp
        unstab_poles = np.unique(unstab_poles_alpha ** (1 / alpha))
        res[fields.unstable_poles] = unstab_poles
        res[fields.error] = np.zeros_like(unstab_poles)
        # Eliminate duplicate unstable poles
        keep_up = np.ones((len(unstab_poles)))
        for k in range(len(unstab_poles)):
            error_k = error_eval_phase(np.complex128(unstab_poles_alpha[k]), poly_mat,
                                       tau, alpha, delay_vect)
            res[fields.error][k] = error_k
            for p in range(k+1, len(unstab_poles)):
                if np.sqrt((np.real(unstab_poles[k] - np.real(unstab_poles[p]))) ** 2 +
                        (np.imag(unstab_poles[k] - np.imag(unstab_poles[p]))) ** 2) \
                        < res[fields.error][k]:
                    keep_up[p] = 0

        res[fields.unstable_poles] = res[fields.unstable_poles][keep_up != 0]
        res[fields.error] = res[fields.error][keep_up != 0]

        # root locus stored in the output dictionnary
        res[fields.root_loci] = rtlc

    return res

#poly_mat = array([[1, 3, 2, -1], [0, 3, -4, 2],[0.5, 0.7, 1.2, -0.8],
#                  [0.5, 1.34, -0.7, 1.9],[0, 0, 3.4, -1.6]])
#delay_vect = array([1, 2, 3, 6])
#tau = 2.
#alpha = 1.
#plot = 1
#delta_tau = 0.1
"""
poly_mat = array([[6, -66, 180], [0, -2, 12],[0, 6, 30],
                  [0, 0, -2]])
delay_vect = array([1, 2, 3])
tau = 1.
alpha = 1.
plot = 1
delta_tau = 1e-3
res = thread_root_locus(poly_mat, delay_vect, alpha, tau, plot, delta_tau)

for i, j in res.iteritems():
    print i, j
k = 0
for i in res['LieuRacines']:
    k += 1
    print "# of poles for branch # %d : %d" % (k, i.shape[1])
"""
