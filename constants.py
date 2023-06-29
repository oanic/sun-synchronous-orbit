# constants.py

"""This module defines project-level constants."""
import numpy as np

R_e = 6378.14 # Earth's equatorial radius [km]
mu_e = 3.986004418E+05 # Earth's standard gravitational parameter [km^3/s^2]
J2 = 1.08262668355E-3 # J2 zonal coefficient of the Earth [-]
w_e = 2 * np.pi / (23 * 3600 + 56 * 60 + 4.09053) # Earth's rotation rate [rad/s]