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
from model_2bp import model_2bp
from TLE_time2J2000sec import TLE_time2J2000sec
from kepl2cart import kepl2cart
import matplotlib.pyplot as plt



# Constants
mu = 3.986004418E+05  # Earth's gravitational parameter [km^3/s^2]

# RADARSAT-2 orbital elements (from Celestrak) and initial conditions
i = np.deg2rad(98.5763) # inclination [rad]
RAAN = np.deg2rad(171.2197) # right ascension of the ascending node [rad] 
e = 0.0001286 # eccentricity [rad]
omega = np.deg2rad(90.3198) # argument of perigee [rad]
M = np.deg2rad(269.8132) # mean anomaly [rad]
n = 14.29985113 # mean motions (revolutions per day)
T = 1/n * 24 * 3600 # orbital period [s]
a = ((mu * T ** 2)/(4 * np.pi ** 2)) ** (1/3) # semimajor axis [km]
kepl_elem = [a,e,i,omega,RAAN,M]


#kepl_elem = [8000,0.5,np.pi/4,0,np.pi/8,np.pi]
# time conversion
year_TLE = 23
day_TLE = 164.51591129
t0 = TLE_time2J2000sec(year_TLE,day_TLE)

t = t0 + 60
[r, r_vect, v_vect] = kepl2cart(kepl_elem,t0,t0,mu)

# Time vector
t_vect = np.linspace(0,6*3600,200) # simulate for one orbital period

# Propagate orbit 

state_0 = np.concatenate((r_vect,v_vect)).flatten()# Initial state

sol = scipy.integrate.odeint(model_2bp,state_0,t_vect) # solving ODE

X_sat = sol[:, 0]  # X-coord [km] in ECI frame over time interval
Y_sat = sol[:, 1]  # Y-coord [km] in ECI frame over time interval
Z_sat = sol[:, 2]  # Z-coord [km] in ECI frame over time interval

# Plot earth + orbit + ECI axes

# Plot spherical Earth
N = 50
phi = np.linspace(0, 2 * np.pi, N)
theta = np.linspace(0, np.pi, N)
theta, phi = np.meshgrid(theta, phi)

r_Earth = 6378.14  # Average radius of Earth [km]
X_Earth = r_Earth * np.cos(phi) * np.sin(theta)
Y_Earth = r_Earth * np.sin(phi) * np.sin(theta)
Z_Earth = r_Earth * np.cos(theta)

# Plotting Earth and Orbit
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X_Earth, Y_Earth, Z_Earth, color='blue', alpha=0.7)
ax.plot3D(X_sat, Y_sat, Z_sat, 'black')
ax.view_init(30, 45)  # Changing viewing angle (adjust as needed)
plt.title('Two-Body Orbit')
ax.set_xlabel('X [km]')
ax.set_ylabel('Y [km]')
ax.set_zlabel('Z [km]')

# Make axes limits
xyzlim = np.array([ax.get_xlim3d(), ax.get_ylim3d(),      
                   ax.get_zlim3d()]).T
XYZlim = np.asarray([min(xyzlim[0]), max(xyzlim[1])])
ax.set_xlim3d(XYZlim)
ax.set_ylim3d(XYZlim)
ax.set_zlim3d(XYZlim)


# Plot ECI axes
XYZaxes = np.array([[0, 0, 0, r_Earth*2, 0, 0 ], [0, 0, 0, 0, r_Earth*2, 0 ],
                [0, 0, 0, 0, 0, r_Earth*2 ]])
X, Y, Z, U, V, W = zip(*XYZaxes)
ax.quiver(X, Y, Z, U, V, W)

plt.show()
# Plot groundtrack

# Implement orbit precession













