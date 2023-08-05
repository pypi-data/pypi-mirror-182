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

from __future__ import unicode_literals
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import axes3d
from .parameters import matplotlib as mpl_params

from .data import Messages
from .roots_looper import roots_looper
#from .debug_roots_looper import debug_roots_looper
from .data import FieldsRootLocus

def integrate_unstable_poles_min(syst, poly_mat, roots_alpha, alpha, \
                                 delay_vect, tau, plot_option, delta_tau):
    """Integrates poles until point of interest"""

    # Param
    # msg = Messages()
    # Initialization: we will access data with res[fields.type] for instance
    ob = FieldsRootLocus()
    fields, _ = ob.get_fields_and_dict()
    # Number of branches of root loci
    nb_unst_roots_no_del = sum(np.real(syst[fields.roots_no_delay]) >= 0)
    if not syst[fields.imag_roots].size:
        nlrcross = 0
    else:
        nlrcross = sum(syst[fields.imag_roots][:,2] > 0)
    if nb_unst_roots_no_del + nlrcross == 0:
        unstab_poles = np.array([])
        rolo = np.array([])
        return

    rolo = [] # root loci
    cntrolo = 0

    unst_roots = np.nonzero(np.real(syst[fields.roots_no_delay]) >= 0)[0]
    unstab_poles = np.array([])

    # Loop for roots unstable at tau nul
    # parfor aLoop=1:size(aUnstRoots,2) // parallel computation with c
    # shared library?
    #print "coucou unstRoots"
#    unstab_poles, cntrolo, rolo = \
#    roots_looper(unstab_poles, cntrolo, rolo, unst_roots, 'UnstRoots', \
#                 delta_tau, poly_mat, delay_vect, alpha, tau, roots_alpha, \
#                 plot_option)


    unstab_poles, cntrolo, rolo = \
    roots_looper(unstab_poles, cntrolo, rolo, unst_roots, 'UnstRoots', \
                 delta_tau, poly_mat, delay_vect, alpha, tau, roots_alpha, \
                 plot_option)

    # Loop for roots unstable at some non zero tau
#    print "coucou NormalImag"
    imag_roots = np.array([])
    if syst[fields.imag_roots].shape[0] > 0:
        imag_roots = syst[fields.imag_roots][syst[fields.imag_roots][:, 2] > 0, :]

    unstab_poles, cntrolo, rolo = \
    roots_looper(unstab_poles, cntrolo, rolo, imag_roots, 'ImagRootsNormalPath',
                 delta_tau, poly_mat, delay_vect, alpha, tau, roots_alpha,
                 plot_option)

    # Loop for roots unstable at some non zero tau, reverse path
    imag_roots = np.array([])
    if syst[fields.imag_roots].shape[0] > 0:
        imag_roots = syst[fields.imag_roots][syst[fields.imag_roots][:, 2] > 0, :]

    unstab_poles, cntrolo, rolo = \
    roots_looper(unstab_poles, cntrolo, rolo, imag_roots, 'ImagRootsReversePath',
                 delta_tau, poly_mat, delay_vect, alpha, tau, roots_alpha,
                 plot_option)

    # Graphs and plot
    if cntrolo:
        xs_min, ys_min = +np.inf, +np.inf
        xs_max, ys_max = -np.inf, -np.inf
    else:
        raise TypeError("No data to plot")

    tau_min, tau_max = (0, tau)

    fig, ax = plt.subplots(2, 1)
    fig.suptitle("Root locus")
    ax[0].set_position([0.125, 0.225, 0.8, 0.725])
    ax[1].set_position([0.125, 0.1, 0.8, 0.03])
    ax[0].grid(True)
    ax[0].set_axisbelow(True)
    ax[0].set_xlabel("Real part")
    ax[0].set_ylabel("Imaginary part")

    normalizer = colors.Normalize(tau_min, tau_max)
    colormapper = cm.ScalarMappable(norm = normalizer,\
                                    cmap = plt.get_cmap("jet"))

    for i in range(cntrolo):
        real = rolo[i][0, :]
        imag = rolo[i][1, :]
        delay = rolo[i][2, :]
        #colormapper.set_array(delay)

        for j in range(1, real.size):
            color = colormapper.to_rgba((delay[j-1] + delay[j])/2)
            ax[0].plot(real[j-1:j+1], imag[j-1:j+1], color = color, lw=1.5)

    cbar = fig.colorbar(colormapper, cax = ax[1], orientation="horizontal")
    cbar.set_label("Delay")

    # Old 3D plot
    # # Get instance of Axis3D
    # fig = plt.figure()
    # #import pdb;pdb.set_trace()
    # fig.add_subplot(projection="3d")
    # ax = fig.gca()

    # for i in range(cntrolo):
    #     xs = list(rolo[i][0])
    #     ys = list(rolo[i][1])
    #     zs = list(rolo[i][2])
    #     # Scatter plot with color scale between vmin(0) and vmax(tau_max)
    #     scat = ax.scatter(xs, ys, zs, c=zs, marker="*", s=200, vmin=0, vmax=tau_max)
    #     # Colored stuff
    #     jet = plt.get_cmap('jet')
    #     c_norm = colors.Normalize(vmin=0, vmax=zs[-1])
    #     scalar_map = cm.ScalarMappable(norm=c_norm, cmap=jet)
    #     # Segments to plot colored lines
    #     xs_seg = [[xs[k], xs[k+1]] for k in range(len(xs)-1)]
    #     ys_seg = [[ys[k], ys[k+1]] for k in range(len(ys)-1)]
    #     zs_seg = [[zs[k], zs[k+1]] for k in range(len(zs)-1)]
    #     for x, y, z in zip(xs_seg, ys_seg, zs_seg):
    #         color_val = scalar_map.to_rgba(z[0])
    #         ax.plot(x, y, z, color=color_val)
    # ax.set_xlabel(r'$\mathcal{R}e(s)$', fontsize=18)
    # ax.set_ylabel(r'$\mathcal{I}m(s)$', fontsize=18)
    # ax.set_zlabel("Tau(s)", fontsize=18)
    # ax.view_init(elev=30., azim=295) # to get a better angle
    # plt.title('Root Locus', fontsize=20)

    # # color bar on the right
    # cbar = fig.colorbar(scat)
    # cbar.set_label('Tau(s)\n\n\n', rotation=270, fontsize=18)

    if plot_option and plot_option!=999999: #hack for unittest
        if 'savefig' in mpl_params:
            savefig_ = mpl_params.get('savefig')
            assert 'fname' in savefig_
            fname = savefig_.get('fname')
            if os.path.exists(fname):
                raise ValueError(f"File {fname} already exists!")
            plt.savefig(**savefig_)
        plt.show()

    return unstab_poles, rolo  # temp
