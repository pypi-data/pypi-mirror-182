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
from .decorators.control_inputs import controler_types
from .data import Messages
from .reduce_deg_poly import reduce_deg_poly

@controler_types(np.ndarray)
def system_type(poly_mat):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Defines the type of system.

    typ = system_type(poly_mat) returns the typ of the system described by its
    quasi polynomial poly_mat (a N-by-N matrix). The function compares the
    degree of polynomial poly_mat(1,:) with the degree of the other
    polynomials.

    typ = system_type(poly_mat) returns 0 for retarded, 1 for neutral,
    and 2 for an advanced system.

    Examples:
    If poly_mat = [1 2 4
                   0 2 1
                   0 0 3]
    then the output is 0 as a retarded system.

    If poly_mat = [1 2 4
                   0 2 1
                   1 4 3]
    then the output is 1 as a neutral system.

    """

    # The set of all the strings that may be used.
    strings = Messages()

    # Variables d'initialisation
    num_poly = poly_mat.shape[0]
    precision = 1e-10
    degree = np.zeros(num_poly)

    # Computes the degree of each polynomial
    for ind in range(num_poly):
        degree[ind] = reduce_deg_poly(poly_mat[ind, :], prec=precision).shape[0]

	# Initialize the loop
    typ = strings.types[0] # Retarded system
    advanced = False
    neutral = False
    ind = 2

	# Compare the degree of the first polynomial with the others and set the
	# value of the temporary typ indicators accordingly
    while (ind <= num_poly) and (advanced == False):
        if degree[ind-1] > degree[0]:
            advanced = True
        elif degree[ind-1] == degree[0]:
            neutral = True
        ind += 1

	# Defines the typ of the system
    if advanced == True:
        typ = strings.types[1] # Advanced system
    elif neutral == True:
        typ = strings.types[2] # Neutral system

    return typ

