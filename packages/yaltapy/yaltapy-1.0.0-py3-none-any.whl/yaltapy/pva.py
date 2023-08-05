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
import cmath as cm
from .phase import phase

from .decorators.control_inputs import controler_types

@controler_types(type(lambda:0), np.complex128, float)
def pva(func, center, eps):
    # pylint: disable=E1101
    # ignoring warnings concerning numpy module.
    """Argument principle.

    nb_circles = pva(func, center, eps) computes the winding number, that is
    the total number of counterclockwise turns around zero of the
    image of a circle of radius "eps" and center "center" under the
    func "func".

    Example:
    f = lambda x: x**2 + 2*x + 1;
    nb_circles = pva(f, -1, 1e-6);
    The winding number around zero of the image of the circle of radius
    1e-6 and center -1 under func "f" is equal to 2.

    """

    points = 200
    vec = np.zeros(points, dtype=np.complex128)
    pts = [center + eps*cm.exp(1j*k) for k in np.linspace(0, 2*np.pi, points)]
    # Compute the image of pts by func.
    for i in range(points):
        vec[i] = func(pts[i])

    angles = phase(vec)
    #angles = np.unwrap(np.angle(vec), discont=3.5)
    # Number of circles.
    nb_circles = (angles[-1] - angles[0]) / (2 * np.pi)
    return nb_circles if np.isnan(nb_circles) else round(nb_circles)
