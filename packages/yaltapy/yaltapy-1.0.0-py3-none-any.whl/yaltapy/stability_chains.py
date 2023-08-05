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

from .chain_poles_poly import chain_poles_poly
from .imag_axis_chain import imag_axis_chain


#def uniquetol(arr, precision):
#    m = 1/precision
#    return np.unique(np.round(arr*m)/m)

def uniquetol(arr, _):
    return np.unique(arr)

def stability_chains(poly_mat, delay_vect, tau, alpha, precision=1e-12):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Test system stability with chain of poles***
    Inputs: the quasi-polynomial poly_mat, the delay vector delay_vect,
    the nominal delay tau, the fractional power alpha, the precision.
    Outputs: the roots chain, and oStable(1 if stable, -1 if not)"""

    # Roots of the formal polynomial (which gives the position of the
    # asymptotic axis. If the roots are of multiplicity greater than 1, we
    # have several chains of poles asymptotic to the same axis.
    roots = np.roots(chain_poles_poly(poly_mat, delay_vect, precision))

    if len(uniquetol(roots, precision)) < len(roots):
        sys.exit("Multiplicity of chain poles greater than one")
    roots_chain = -np.log(uniquetol(np.absolute(roots), precision)) / tau

    if all(np.less(roots_chain, -precision)):
        # All the chains are on the left of the imag. axis, thus we are stable.
        stable = 1
    elif max(abs(roots_chain) < precision):
        # The chains are on the imag. axis, we need to look closer with function
        # imag_axis_chain
        stable = imag_axis_chain(poly_mat, delay_vect, alpha,
                                 roots[roots_chain == 0])
    else:
        # There is at least one chain in the RHP, thus we are unstable.
        stable = -1

    return roots_chain, stable
