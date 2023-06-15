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
from kepl2cart import kepl2cart


# Constants
mu = 3.986004418E+05  # Earth's gravitational parameter [km^3/s^2]

# RADARSAT-2 orbital elements (from Celestrak)
i = np.deg2rad(98.5763) # inclination [rad]
RAAN = np.deg2rad(171.2197) # right ascension of the ascending node [rad] 
e = 0.0001286 # eccentricity [rad]
omega = np.deg2rad(90.3198) # argument of perigee [rad]
M = np.deg2rad(269.8132) # mean anomaly [rad]
n = 14.29985113 # mean motions (revolutions per day)
T = 1/n * 24 * 3600 # orbital period [s]
a = ((mu * T ** 2)/(4 * np.pi ** 2)) ** (1/3) # semimajor axis [km]
#kepl_elem = [a,e,i,omega,RAAN,M]


kepl_elem = [8000,0.5,np.pi/4,0,np.pi/8,np.pi]
# time conversion
year_TLE = 23
day_TLE = 164.51591129
t0 = TLE_time2J2000sec(year_TLE,day_TLE)

t = t0 + 60
[r, r_vect, v_vect] = kepl2cart(kepl_elem,t0,t0,mu)

















