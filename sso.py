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
import matplotlib as plt
import datetime
from model_2bp import model_2bp
from model_2bp_J2 import model_2bp_J2

from TLE_time2MJD2000 import TLE_time2MJD2000
from kepl2cart import kepl2cart
import matplotlib.pyplot as plt
from plot_Earth import plot_Earth
from mayavi import mlab
import spiceypy as spice
import constants as const
from ground_track import ground_track

# Constants

# %% RADARSAT-2 orbital elements (from Celestrak) and initial conditions
i = np.deg2rad(98.5763) # inclination [rad]
RAAN = np.deg2rad(171.2197) # right ascension of the ascending node [rad] 
e = 0.0001286 # eccentricity [rad]
omega = np.deg2rad(90.3198) # argument of perigee [rad]
M = np.deg2rad(269.8132) # mean anomaly [rad]
n = 14.29985113 # mean motions (revolutions per day)
T = 1/n * 24 * 3600 # orbital period [s]
a = ((const.mu_e * T ** 2)/(4 * np.pi ** 2)) ** (1/3) # semimajor axis [km]
kepl_elem = [a,e,i,omega,RAAN,M]

# time conversion
year_TLE = 23
day_TLE = 164.51591129
n_leap_s = 0
t0 = TLE_time2MJD2000(year_TLE,day_TLE, n_leap_s)

n_orbits = 16
delta_T = T*n_orbits
t = t0 + delta_T
[r, r_vect, v_vect] = kepl2cart(kepl_elem,t0,t0)

# Time vector
t_vect = np.linspace(t0,t,n_orbits*100) # simulate for one orbital period

# %% Propagate orbit 

state_0 = np.concatenate((r_vect,v_vect)).flatten()# Initial state

state = scipy.integrate.odeint(model_2bp_J2,state_0,t_vect) # solving ODE

X_sat = np.array(state[:, 0], dtype=float)  # X-coord [km] in ECI frame over time interval
Y_sat = np.array(state[:, 1], dtype=float)   # Y-coord [km] in ECI frame over time interval
Z_sat = np.array(state[:, 2], dtype=float)  # Z-coord [km] in ECI frame over time interval

pos = np.concatenate((X_sat, Y_sat, Z_sat),axis = 0)
# %% Plot earth + orbit + ECI axes

image = "/Users/dylan/Desktop/orbit model/world.topo.bathy.200412.3x5400x2700.jpeg"
plot_Earth(image)
orbit = mlab.plot3d(X_sat, Y_sat, Z_sat, color = (1,1,1), representation = "wireframe")

GAST_t0 = 0
ground_track(state, GAST_t0, const.w_e, t_vect)
#mlab.orientation_axes()
#fig.scene.close()
# Implement J2 perturbation and verify effect on precession

# Plot groundtrack

# Implement orbit precession

# # %%
# f = mlab.figure()

# x = np.linspace(0, 10, 11)
# y = x**2
# z = y**3

# nodes = mlab.points3d(x, y, z)


