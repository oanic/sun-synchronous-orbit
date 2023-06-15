#############################################
# Model sun-synchronous orbit
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:58:52 2023

@author: Oana Nica
"""
#############################################

# Import packages
import numpy as np
import scipy
import matplotlib
import datetime
import model_2bp
from TLE_time2J2000sec import TLE_time2J2000sec

# Constants
mu = 3.986004418E+05  # Earth's gravitational parameter [km^3/s^2]

# # RADARSAT-2 orbital elements
# h = 592.7 # altitud [km]
# i = 97.74 # inclination [deg]
# T = 96.4 * 60 # orbital period [s]
# LTAN = 6 # local time of the ascending node
# e = 0.0006 # eccentricity (estimated) [-]
# a = ((mu * T ** 2)/(4 * np.pi ** 2)) ** (1/3) # semimajor axis [km]
# omega = 0 # argument of periapsis [deg]
# RAAN = 0 # longitude of the ascending node [deg]
# theta = 0 # true anomaly at referene epoch t0 [deg]
# t0 = 

# RADARSAT-2 orbital elements (from Celestrak)
i = np.deg2rad(98.5763) # inclination [rad]
RAAN = np.deg2rad(171.2197) # right ascension of the ascending node [rad] 
e = 0.0001286 # eccentricity [rad]
omega = np.deg2rad(90.3198) # argument of perigee [rad]
M = np.deg2rad(269.8132) # mean anomaly [rad]
n = 14.29985113 # mean motions (revolutions per day)
T = 1/n * 24 * 3600 # orbital period [s]
a = ((mu * T ** 2)/(4 * np.pi ** 2)) ** (1/3) # semimajor axis [km]


# time conversion
year_TLE = 23
day_TLE = 164.51591129
t0 = TLE_time2J2000sec(year_TLE,day_TLE)