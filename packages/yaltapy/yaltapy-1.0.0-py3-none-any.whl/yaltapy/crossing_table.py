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

import os
import numpy as np
import scipy.optimize as so
import matplotlib.pyplot as plt
import cmath
from .parameters import matplotlib as mpl_params
from .frac_theta import frac_theta
from .order_vec import order_vec
from .decorators.control_inputs import controler_types

class Data(object):
    """Class describing our system."""

    def __init__(self):
        self.poly_mat = None
        self.angle_max = None
        self.delay_vect = None
        self.index = None
        self.roots = None

@controler_types(np.ndarray, np.ndarray, float, nb_pts=int, graph=int)
def crossing_table(poly_mat, delay_vect, alpha, nb_pts=1e3, graph=0):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Computes the crossing table of the system.

    cross_tab = crossing_table(poly_mat,delay_vect,alpha,nb_pts,graph)
    takes in input the quasi-polynomial poly_mat (M-by-N matrix), the delay
    vector delay_vect (row vector), the fractional power alpha, the number of
    discrete intervals for theta nb_pts (optional), and a boolean for crossing
    graph graph(optional), and checks zeros of pure imaginary value to
    estimate crossing of the imaginary axis.

    Example:

    See also arrange_table.

    """
    nb_pts = int(nb_pts)
    # Initialization
    my_data = Data()
    theta = np.linspace(-np.pi / nb_pts, np.pi, nb_pts + 1)
    angle_max = alpha * np.pi / 2
    my_data.poly_mat = poly_mat
    my_data.angle_max = angle_max
    my_data.delay_vect = np.concatenate((np.zeros(1), delay_vect))
    ath = -1j * theta[0] * np.concatenate((np.zeros(1), delay_vect))
    all_roots = np.roots(np.dot([cmath.exp(i) for i in ath], poly_mat))
    alpha_roots = np.zeros((len(all_roots), nb_pts + 1))
    alpha_roots[:, 0] = np.angle(all_roots)
    nb_roots = [int(np.absolute(np.angle(i)) < angle_max+1e-13) for i in all_roots]
    cross_tab = np.array([])
    fun = lambda x: frac_theta(x, my_data)
    # Use of frac_theta coupled with brentq(zero finding) to check crossing
    for i in range(1, int(nb_pts)+1):
        ate = -1j * theta[i] * np.concatenate((np.zeros(1), delay_vect))
        tmp_roots = order_vec(all_roots, np.roots(np.dot([cmath.exp(p) \
                                              for p in ate], poly_mat)))
        alpha_roots[:, i] = np.angle(tmp_roots)
        tmp_nb_roots = [np.absolute(np.angle(k)) < (angle_max + 1e-13) \
                        for k in tmp_roots]
        if any(np.not_equal(nb_roots, tmp_nb_roots)):
            my_data.roots = tmp_roots
            for j in range(len(all_roots)):
                if nb_roots[j] != tmp_nb_roots[j]:
                    my_data.index = j
                    point = so.brentq(fun, theta[i-1], theta[i], xtol=1e-15)
                    # To avoid issues at the origin, we begin with a small yet
                    # negative theta, here we correct this by approximating at
                    # zero
                    if point < 0:
                        point = 0
                    new_delay = -1j * point * np.concatenate((np.zeros(1), \
                                                          delay_vect))
                    ordered_roots = order_vec(tmp_roots, \
                                              np.roots(np.dot([cmath.exp(elt) \
                                              for elt in new_delay], poly_mat)))
                    if len(cross_tab) != 0:
                        cross_tab = np.vstack([cross_tab, \
                                           [point, ordered_roots[j]]])
                    else:
                        cross_tab = np.array([point, ordered_roots[j]])
            nb_roots = tmp_nb_roots
        all_roots = tmp_roots

    # Manage the graph option. It may become very confused for some values.
    # We may have to limit the number of curves

    if graph:
        for i in range(alpha_roots.shape[0]):
            plt.plot(theta, np.absolute(alpha_roots[i, :]))
        plt.plot(np.concatenate(([theta[0]], [theta[len(theta) - 1]])), \
                                 [angle_max, angle_max])
        plt.xlim([0, np.pi])
        plt.ylim([0, np.pi])
        if 'savefig' in mpl_params:
            savefig_ = mpl_params.get('savefig')
            assert 'fname' in savefig_
            fname = savefig_.get('fname')
            if os.path.exists(fname):
                raise ValueError(f"File {fname} already exists!")
            plt.savefig(**savefig_)
        plt.show()

    return cross_tab



