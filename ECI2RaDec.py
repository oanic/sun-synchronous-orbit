"""
ground_track: plot ground track of an orbit

INPUTS
state: state of the orbit (cartesian coordinates) at a given time

OUTPUTS
dec: satellite declination [rad]
RA: satellite right ascension [rad]

Created 2023-06-27 by Oana Nica
"""
import numpy as np

def ECI2RaDec(state):
    x = state[0]
    y = state[1]
    z = state[2]
    r = (x ** 2 + y ** 2 + z ** 2) ** (1/2)

    l = x/r
    m = y/r
    n = z/r
    
    dec = np.arcsin(n)
    
    if m > 0:
        RA = np.arccos(l / np.cos(dec))
    else:
        RA = 2 * np.pi - np.arccos(l / np.cocs(dec))
        
    return dec, RA
    
    
