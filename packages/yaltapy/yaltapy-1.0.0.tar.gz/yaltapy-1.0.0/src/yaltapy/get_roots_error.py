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

import numpy as np

from .final_min import final_min

def get_roots_error(itf, poly_mat, tau, delay_vect, alpha):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Computes the roots error of a quasi polynomial.

    [roots, roots_error] = get_roots_error(itf, poly_mat, tau,
                                           delay_vect, alpha)
    takes in input the Pade transfer function itf, the quasi polynomial
    poly_mat, the base delay tau, the delay vector delay_vect, the
    fractional power alpha, and computes the distance between approximated
    roots and roots of the quasi polynomial.
    Outputs are roots, the roots of the approximation with positive real
    part, and roots_error the corresponding errors.

    Example:

    """

    # Roots computation for the Pade and defines
    num = itf.num[0][0]
    all_roots = np.roots(num)
    roots = all_roots[np.real(all_roots)>0]
    ref_roots = np.zeros(len(roots), dtype=np.complex128)

    # Roots computation around the Pade approximation of the roots
    for i in range(len(roots)):
        point = np.array([np.real(roots[i]), np.imag(roots[i]), tau])
        ref_point = final_min(point, poly_mat, delay_vect, float(alpha), tau)
        ref_roots[i] = ref_point[0] + ref_point[1] * 1j

    # Error computation and test to see if the roots computation above gives
    # a valid solution (and not just a local minimum that is not a root)
    roots_error = np.absolute(roots - ref_roots)
    if roots_error.size and abs(max(roots_error) - 1e-2) < 1e-10:
        roots_error = "Error too important"

    return roots, roots_error
