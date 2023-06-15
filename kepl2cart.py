# Convert Keplerian orbit elements to cartesian state vectors
import numpy as np

def kepl2cart(kepl_elem,t0,t,mu):
    a = kepl_elem[0]*1000 # semi-major axis [m]
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
        M = M0 + delta_t * (mu / a ** 3) ** (1/2)
        while M > 2 * np.pi:
            M = M - 2 * np.pi
            
    # Solve Kepler's equation for the eccentric anomaly E(t)
    Ei_1 = M
    err = 1
    
    f = lambda E: E - e * np.sin(E) - M
    f_prime = lambda E: 1 - e * np.cos(E)
    
    while err > 1e-6:
        Ei = Ei_1 - f(Ei_1)/f_prime(Ei_1)
        err = abs(Ei - Ei_1)
        Ei_1 = Ei
        
    E = Ei
    # Compute true anomaly
    nu =  
    
    
