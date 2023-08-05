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
from .get_tau_real_root import get_tau_real_root

def predictor(last_point, penul_point, adv_factor,
              poly_mat, delay_vect, precision):
    # pylint: disable=E1101, R0913
    # ignoring warnings concerning numpy module.
    # ignoring warnings concerning too manya args for func predictor.
    """Compute the following point of the curve.

    predicted_pt, bifurc = predictor(last_point, penul_point, adv_factor,
                                     poly_mat, delay_vect, precision)

    This function is based on a predictor that uses preceeding points
    last_point and penul_point to compute an estimate of the following point
    and a corrector that will modify the estimate to put the point on the
    curve. In case of a sign change between the last point and the
    estimated point, the predictor proposes a point on the real axis with a
    rotation in the direct sense of an angle of PI/2. This allows the
    predictor to consider bifurcations at real values of the zeros.
    adv_factor allows to set the precision for the research of the predicted
    point. The parameter precision defines the offset that is applied on
    the real part of a point if the predicted point and the last point have
    a sign change. poly_mat is the matrix of quasi-polynomials, delay_vect the
    vector of delays.
    The outputs are the estimated point predicted_pt and bifurc that is set to
    1 of there is a bifurcation and 0 otherwise.
    NB : A point consists on (Re(s), Im(s), tau) coordinates .
    """

    offset = precision * 100
    bifurc = 0 # bifurcation
    predicted_pt = [last_point[i] + (last_point[i] - penul_point[i]) * \
                    adv_factor for i in range(3)]
    predicted_pt[2] = last_point[2] + (last_point[2] - penul_point[2]) * \
                      adv_factor
    # Now we check if there is a branching point
    # Chek if the iimaginary part has a sign change
    ratio_im_real = abs(last_point[1] - penul_point[1]) / abs(last_point[0] - \
                                                              penul_point[0])
    if (np.sign(predicted_pt[1] * last_point[1]) == -1) and \
       (ratio_im_real > 0.1) and (predicted_pt[0] > 0):
        predicted_pt[0] = last_point[0] + np.sign(last_point[1]) * offset
        predicted_pt[1] = 0
        predicted_pt[2] = max(get_tau_real_root(predicted_pt[0], poly_mat, \
                              delay_vect), last_point[2] + 1e-8)
        bifurc = 1
        if np.isinf(predicted_pt[2]):
            predicted_pt = [last_point[i] + (last_point[i] - penul_point[i]) * \
                            adv_factor for i in range(3)]

    return predicted_pt, bifurc


