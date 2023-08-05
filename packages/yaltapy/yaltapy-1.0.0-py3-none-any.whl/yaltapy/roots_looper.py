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

import sys
import numpy as np
import cmath as cm

from .comparator_min import comparator_min
from .comparator_min_test_pva import comparator_min_test_pva
from .predictor import predictor
from .final_min import final_min


def roots_looper(unstab_poles, cnt_rolo, rolo, array, array_type, delta_tau,
                 poly_mat, delay_vect, alpha, tau, roots_alpha, plot_option):
    """Integrates unstable poles and plot the branches of the root locus.

    """
    # PARAM
    precision = delta_tau / 2.
    adv_factor_multiplier = 1.3
    nb_pts_max = 1000
    pointfx = []
    idxfx = []

    if array_type == 'UnstRoots':
        try:
            #length_max = array.shape[1]
            length_max = len(array)
        except IndexError:
            length_max = 0
    else:
        length_max = array.shape[0] # for imaginary roots

    if array_type == 'ImagRootsReversePath':
#        print("coucou reverse")
        positive_path = 0
    else:
        positive_path = 1

    # Loop for roots unstable at tau nul
    for i in range(0, length_max):
        cm1_cnt = 0
        cm2_cnt = 0
        cmpva1_count = 0
        cmpva2_count = 0
        pred1_cnt = 0
        pred2_cnt = 0
        point = np.zeros((3, nb_pts_max))
        if array_type == 'UnstRoots':
            point[0, 0] = np.real(roots_alpha[array[i]])
            point[1, 0] = np.imag(roots_alpha[array[i]])
        else:
            point[1, 0] = array[i, 1]
            tmp_point = np.absolute(point[1, 0])**alpha*cm.exp(1j*np.pi/2*alpha)
            point[0, 0] = np.real(tmp_point)
            point[1, 0] = np.sign(array[i, 1]) * np.imag(tmp_point)
            point[2, 0] = array[i, 0]
        adv_factor = 1.
        pva_test = 16.
        point[:, 1] = 0
        while not np.any(point[:, 1]):
            if array_type == 'ImagRootsReversePath':
                direc = -1
            else:
                direc = +1
            point[:, 1] = point[:, 0] + np.dot(direc, [0, 0, delta_tau * adv_factor])
            while point[2, 1] > (tau + precision / 10):
                adv_factor /= 2
                point[:, 1] = point[:, 0] + [0, 0, delta_tau * adv_factor]
            adv_factor /= 2
            if adv_factor > 1 / pva_test:
                cm1_cnt += 1
                point[:, 1] = comparator_min(point[:, 1], poly_mat, delay_vect, \
                                             alpha, precision, positive_path)
            else:
                cmpva1_count += 1
                point[:, 1] = comparator_min_test_pva(point[:, 1], poly_mat, \
                                                      delay_vect, alpha, \
                                                      precision, positive_path)
                pva_test *= 0.9
                if array_type == 'ImagRootsNormalPath':
                    if pva_test < 0.1:
                        sys.exit('Initialization error')
        idx = 3
        adv_factor = 1.
#        print("idx :", idx)
#        print("nb_pts_max :", nb_pts_max)
        if array_type == 'ImagRootsReversePath':
            # -----------temporary fix--------------
            tau_limit_inf = tau / 10
            tmp = np.real((point[0, 1] + point[1, 1]*1j) ** (1/alpha))
            # --------------------------------------
            condition_one = point[2, idx-2] >= tau_limit_inf and tmp <= 0
        else:
            condition_one = point[2, idx-2] <= tau

        while condition_one:
            pred1_cnt += 1
            point[:, idx-1], bifur = predictor(point[:, idx-2], point[:, idx-3], \
                                               adv_factor, poly_mat, delay_vect, \
                                               delta_tau)

            # Here is a tricky part. If the AdvFactor is too big, then the
            # predicted Tau will be too far from the limit. Thus the following
            # a bit heavy ajustments.
            if array_type == 'ImagRootsReversePath':
                condition_two = point[2, idx-1] < tau_limit_inf - precision/10
            else:
                condition_two = point[2, idx-1] > tau + precision/10
            while condition_two:
                adv_factor /= 2.
                pred2_cnt += 1
                point[:, idx-1], bifur = predictor(point[:, idx-2], \
                                                   point[:, idx-3], \
                                                   adv_factor, poly_mat, \
                                                   delay_vect, delta_tau)
                if array_type == 'ImagRootsReversePath':
                    condition_two = point[2, idx-1] < tau_limit_inf - precision/10
                else:
                    condition_two = point[2, idx-1] > tau + precision/10
#            print "indice loop : ", i
            if adv_factor > 1 / pva_test:
#                print "Min"
                cm2_cnt += 1
                point[:, idx-1] = comparator_min(point[:, idx-1], poly_mat, \
                                                 delay_vect, alpha, precision, \
                                                 positive_path)
            else:
#                print "MinTestPva"
                cmpva2_count += 1
                point[:, idx-1] = comparator_min_test_pva(point[:, idx-1], \
                                                          poly_mat, delay_vect, \
                                                          alpha, precision, \
                                                          positive_path)
                pva_test *= 0.9
            if not np.any(point[:, idx-1]):
                adv_factor /= 2.
            else:
                if array_type == 'UnstRoots':
                    if point[2, idx-1] < point[2, idx-2]:
                        sys.exit('Tau decreasing')
                if bifur:
                    point[:, idx] = point[:, idx-1]
                    point[0, idx-1] = point[0, idx-2]
                    point[2, idx-1] = point[2, idx-2] + (point[2, idx-1] - \
                                                         point[2, idx-2])/ 2
                idx += 1 + bifur
                adv_factor *= adv_factor_multiplier
            if array_type == 'ImagRootsReversePath':
                # -----------temporary fix--------------
                tmp = np.real((point[0, 1] + point[1, 1]*1j) ** (1/alpha))
                condition_one = idx < nb_pts_max + 1 and \
                             point[2, idx-2] >= tau_limit_inf and \
                             tmp <= 0
            else:
                condition_one = idx < nb_pts_max + 1 and point[2, idx-2] <= tau

        # Finalisation
        if not array_type == 'ImagRootsReversePath':
            ref_point = final_min(point[:, idx-2], poly_mat,
                                  delay_vect, alpha, tau)
            if np.any(ref_point):
                point[:, idx-2] = ref_point
            ref_point[0] = (point[0, idx-2] + point[1, idx-2]*1j) ** (1/alpha)
            ref_point[1] = np.imag(ref_point[0])
            ref_point[0] = np.real(ref_point[0])
            if ref_point[0] >= 0:
                unstab_poles = np.concatenate((unstab_poles, [point[0, idx-2] + \
                                               point[1, idx-2] * 1j]))

        if plot_option:
            # We apply the fractionnal power to the set of points.
            point_temp = (point[0, :] + point[1, :] * 1j) ** (1/alpha)
            new_points_alpha = np.empty_like(point)
            new_points_alpha[0, :] = np.real(point_temp) #
            new_points_alpha[1, :] = np.imag(point_temp)
            new_points_alpha[2, :] = point[2, :] # delay
            pointfx.append(new_points_alpha)
            idxfx.append(idx)

        ## DEBUG PART ##
        ## Trying to understand the difference of number of points found in
        ## Root Locus ##
#        print("Branche # %d: cm1: %d, cm1_pva: %d, predict1: %d, cm2: %d, cm2_pva: %d, predict2: %d" % (i, cm1_cnt, cmpva1_count, pred1_cnt, cm2_cnt, cmpva2_count, pred2_cnt))

    if plot_option:
        for i in range(length_max):
            cnt_rolo += 1
            rolo.append(pointfx[i][:, pointfx[i][2, :] != 0])


    return unstab_poles, cnt_rolo, rolo
