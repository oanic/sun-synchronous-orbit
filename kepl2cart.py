'''
Convert Keplerian orbit elements to cartesian state vectors
It takes as input the orbital elements as a list: [a, e, i, omega, RAAN, M0],
as well as the reference epoch t0, the current epoch t and the earth gravity 
constant mu.
It returns the position and velocity vectors expressed in the ECI frame

Created 2023-06-15 by Oana Nica
'''
import numpy as np
import constants

def kepl2cart(kepl_elem,t0,t):
    a = kepl_elem[0] # semi-major axis [m]
    e = kepl_elem[1] # eccentricity [-]
    i = kepl_elem[2] # inclination [rad]
    omega = kepl_elem[3] # argument of periapsis [rad]
    RAAN = kepl_elem[4] # right ascension of the ascending node [rad]
    M0 = kepl_elem[5] # mean anomaly at epoch t0
    
    # Calculate M(t)
    if t == t0:
        M = M0
    else:
        delta_t = t - t0
        M = M0 + delta_t * (constants.mu_e / a ** 3) ** (1/2)
        while M > 2 * np.pi:
            M = M - 2 * np.pi
            
    # Solve Kepler's equation for the eccentric anomaly E(t)
    Ei_1 = M
    err = 1
    n_iter = 0
    n_iter_max = 50 # maximum number of iterations
    
    f = lambda E: E - e * np.sin(E) - M
    f_prime = lambda E: 1 - e * np.cos(E)
    
    while err > 1e-6 and n_iter < n_iter_max:
        Ei = Ei_1 - f(Ei_1)/f_prime(Ei_1)
        err = abs(Ei - Ei_1)
        Ei_1 = Ei
        n_iter += 1
        if n_iter >= n_iter_max:
            raise ValueError("Maximum number of iterations reached during computation of the eccentric anomaly")
    E = Ei
    
    # Compute true anomaly
    theta =  2 * np.arctan2(np.sqrt(1 + e) * np.sin(E/2), np.sqrt(1 - e) * np.cos(E/2))
    
    # Compute distance to the center of the Earth
    r = a * (1 - e * np.cos(E))
    
    # Obtain the position and velocity vector in the orbital frame (z-axis perpendicular to orbital plane, x-axis pointing to periapsis)
    
    o_vect = r * np.array([np.cos(theta),np.sin(theta),0]).reshape(-1,1)

    o_dot_vect = np.sqrt(constants.mu_e * a) / r * np.array([-np.sin(E), np.sqrt(1 - e ** 2) * np.cos(E), 0]).reshape(-1,1)
    
    # Transform the previous vectors from orbital frame to the ECI frame (z-axis perpendicular to the equatorial plane, x-axis pointing to the prime meridian)
    
    R_x = lambda x: np.array([[1, 0, 0],
                              [0, np.cos(x), np.sin(x)],
                              [0, -np.sin(x), np.cos(x)]])
    R_z = lambda z: np.array([[np.cos(z), np.sin(z), 0],
                              [-np.sin(z), np.cos(z), 0],
                              [0, 0, 1]])
    
    R_mult = np.dot(np.dot(R_z(-RAAN),R_x(-i)),R_z(-omega)) # rotation matrix
    
    r_vect = np.dot(R_mult,o_vect)
    v_vect = np.dot(R_mult,o_dot_vect)
    
    return r, r_vect, v_vect

    
    
    
    
    
    
    
    
    
    