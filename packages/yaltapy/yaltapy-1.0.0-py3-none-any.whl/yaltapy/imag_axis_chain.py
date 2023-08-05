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

def imag_axis_chain(poly_mat, delay_vect, alpha, roots, precision = 1e-12):
    """Compute if the chain is on the left or right side of the imaginary
    axis.
    References:
        1) "Stability of fractional neutral systems with multiple
        delays and poles asymptotic to the imaginary axis." CDC 2010 for
        fractional systems (fractional case: alpha in [0, 1[)
        2) "Stability of neutral systems with commensurate delays and poles
        asymptotic to the imaginary axis. SIAM 2011 (case where alpha = 1)."""

    delta = poly_mat.shape[1]
    # We suppose that the chain of asymptotic poles is on the left of the
    # imaginary axis (stable=2). Further we will evaluate the the stability
    # by computing the term nu_n to update to update if needed the output
    # variable "stable" (to -1 or 0).
    stable = 2
    # Computation of terms alpha_k, beta_k, gamma_k
    alpha_k = poly_mat[1::, 0] / poly_mat[0, 0]
    beta_k = 0
    gamma_k = 0
    if delta > 1:
        beta_k = (poly_mat[1::, 1] - alpha_k * poly_mat[0, 1]) / poly_mat[0, 0]
    if delta > 2:
        gamma_k = (poly_mat[1::, 2] - alpha_k * poly_mat[0, 2] - \
                   beta_k * poly_mat[0, 1]) / poly_mat[0, 0]
    elif delta == 2:
        gamma_k = - beta_k * poly_mat[0, 1] / poly_mat[0, 0]

    for idx in range(len(roots)):
        root = roots(idx)
        kr = sum(beta_k * (root ** delay_vect)) / \
             sum(delay_vect * alpha_k * (root ** delay_vect))
        # Mu_n
        if alpha == 1:
            mu_n = -1j * kr
        elif 0 <= alpha < 1:
            mu_n = (1j * 2 * np.pi) **(-alpha) * kr
        else:
            raise ValueError("Alpha must be a real number in [0, 1]")

        if np.real(mu_n) > precision:
            stable = -1
        elif abs(np.real(mu_n)) <= precision:
            # Nu_n
            nu_n = ((-delay_vect**2 * alpha_k * kr**2 / 2. + \
                     delay_vect * beta_k * kr - gamma_k) * \
                     (root ** delay_vect)) / \
                     sum(delay_vect * alpha_k * (root ** delay_vect))
            if np.real(nu_n) > precision:
                # system in unstable, infinity of unstable poles in RHP.
                stable = -1
            elif abs(np.real(nu_n)) <= precision:
                # impossible to check position of chains of poles at imaginary
                # axis.
                stable = 0

    return stable





