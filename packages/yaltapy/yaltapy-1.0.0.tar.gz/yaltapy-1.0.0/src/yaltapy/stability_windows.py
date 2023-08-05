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

import os
import numpy as np
import matplotlib.pyplot as plt
from .data import Messages
from .decorators.control_inputs import controler_types
from .parameters import matplotlib as mpl_params
@controler_types(np.ndarray, int, float, tau_min=float, iplot=int)
def stability_windows(crossing_table, unstab_roots_no_delay, tau_max,
                      tau_min=0, iplot=1):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Computes the stability windows of the system.

    [swin, delnbp] = stability_windows(crossing_table, unstab_roots_no_delay,
                                       tau_min, tau_max, iplot)
    takes in input the four-column matrix crossing_table describing the
    points of crossing of the imaginary axis, the number unstab_roots_no_delay
    of unstable poles of free delay system, tau_min and tau_max as the
    lower and upper bound of the delay interval, and a plot option iplot
    (no plot = 0, otherwise plot) for plotting the stability windows.
    iplot and tau_min are optional.
    If iplot is not specified, it is set to 1 and stability windows are
    displayed.
    If tau_min is not specified, it is set to 0 and the delay interval will
    be [0, tau_max].
    The outputs are two two-rows matrices swin and delnbp.
    In swin matrix, the first row contains delays in [tau_min, tau_max]
    interval where the stability changes, the second row indicates stability in
    delay intervals of the first row, 1 for stability, and 0 for unstability.
    In delnbp matrix, the first row contains delays where the number of
    unstable poles changes, the second row contains the corresponding
    number of unstable poles.

    Example:

    See also delay_frequency_analysis_min

    """
    # The set of all the strings that may be used.
    strings = Messages()

    if tau_min > tau_max:
        tau_min, tau_max = tau_max, tau_min
    if crossing_table.dtype not in (float, int, complex) \
    or (len(crossing_table) == 0):
        tau = np.concatenate((np.zeros(1), [tau_max]))
        nbp = unstab_roots_no_delay * np.ones(2)
        stab = [i == 0 for i in nbp]
        stab = [int(i) for i in stab]
    else:
        tau_table = [x for x in crossing_table[:, 0]]
        tau = [0.] # crossing delays
        nbp = [unstab_roots_no_delay] # number of unstable poles
        tau_ref = 0
        aw_loop = 1
        while tau_ref < tau_max:
            tau_ref, index_ref = min(tau_table), np.argmin(tau_table)
            tau.append(tau_ref)
            nbp.append(nbp[aw_loop-1] + 2*crossing_table[index_ref, 3])
            tau_table[index_ref] = tau_ref + crossing_table[index_ref, 1]
            aw_loop += 1
        if tau[-1] != tau_max:
            tau = np.concatenate((tau[0:-1], [tau_max]))
            stab = [i == 0 for i in nbp]
            stab = [int(i) for i in stab]
            stab = np.concatenate((stab[0:-1], [stab[-2]]))
            nbp = np.concatenate((nbp[0:-1], [nbp[-2]]))
        else:
            stab = [i == 0 for i in nbp]
            stab = [int(i) for i in stab]
    if tau_min < tau_max:
        ind = [i for i, j in enumerate(tau) if j.real > tau_min]
        # crossing delays in [tau_min, tau_max]
        tau2 = np.concatenate(([tau_min], [tau[i] for i in ind]))
        stab2 = np.concatenate(([stab[ind[0]-1]], [stab[i] for i in ind]))
        nbp2 = np.concatenate(([nbp[ind[0]-1]], [nbp[i] for i in ind]))
        delnbp = np.array([tau2, nbp2])
        if len(stab2) > 2:
            ind = [i+1 for (i, j) in enumerate(stab2[1:-1] - stab2[0:-2]) if j != 0]
            if ind:
                #ind = list(map(lambda x: x+1, ind))
                swin = np.array([np.take(tau2, \
                                         np.concatenate((\
                                         np.concatenate(([0], ind)), [-1]))), \
                                         np.take(stab2, np.concatenate((\
                                         np.concatenate(([0], ind)), [-1])))])
            else:
                swin = np.array([np.take(tau2, np.concatenate(([0], [-1]))), \
                                 np.take(stab2, np.concatenate(([0], [-1])))])
        else:
            swin = np.array([tau2, stab2])
    else:
        delnbp = np.array([tau[-1], nbp[-1]])
        swin = np.array([tau[-1], stab[-1]])

    # Graph
    if iplot:
        plt.figure()
        ax1 = plt.subplot(2, 1, 1)
        plt.plot(swin[0, :], np.concatenate(([swin[1, 0]], swin[1, :-1])), \
                 'b', drawstyle='steps', linewidth=4)
        if tau_min < tau_max:
            ax1.set_xlim([tau_min, tau_max])
            ax1.set_ylim([0, 1])
        plt.xticks(swin[0, :])
        plt.yticks([0, 1])
        plt.xlabel(strings.xlabel)
        plt.ylabel(strings.stablabel)

        ax2 = plt.subplot(2, 1, 2)
        plt.plot(delnbp[0, :], np.concatenate(([delnbp[1, 0]], delnbp[1, :-1])), \
                 'b', drawstyle='steps', linewidth=4)
        if tau_min < tau_max:
            ax2.set_xlim([tau_min, tau_max])
            ax2.set_ylim([0, max(delnbp[1, :])])
        plt.xticks(delnbp[0, :])
        plt.yticks(sorted(delnbp[1, :]))
        plt.xlabel(strings.xlabel)
        plt.ylabel(strings.ylabel)
        if 'savefig' in mpl_params:
            savefig_ = mpl_params.get('savefig')
            assert 'fname' in savefig_
            fname = savefig_.get('fname')
            if os.path.exists(fname):
                raise ValueError(f"File {fname} already exists!")
            plt.savefig(**savefig_)
        plt.show()

    return swin, delnbp
