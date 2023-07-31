'''
groundTrack
plot ground track of an orbit

INPUTS:
 state: state of the orbit (cartesian coordinates) at t_vect
 GAST_t0: Greenwich apparent sidereal time at t0 [rad]
 w_e: Earth's rotation rate [rad/s]
 t_vect: vector of times at which the ground track is computed

Created 2023-06-27 by Oana Nica

'''
from ECI2RaDec import ECI2RaDec
from RaDec2LonLat import RaDec2LonLat
import numpy as np
import matplotlib.pyplot as plt

def ground_track(state, GAST_t0, w_e, t_vect):
    dec = np.zeros(len(t_vect))
    RA = np.zeros(len(t_vect))
    lon = np.zeros(len(t_vect))
    lat = np.zeros(len(t_vect))
    
    t0 = t_vect[0]
    for i, t in enumerate(t_vect):
        
        # convert from cartesian coordinates in ECI frame to RA and dec
        [dec[i],RA[i]] = ECI2RaDec(state[i,:])
        # convert from RA and dec to long,lat
        [lon[i],lat[i]] = RaDec2LonLat(dec[i], RA[i], GAST_t0, w_e, t0, t)

    split = []
    n = 0
    for i,lon_i in enumerate(lon):
        if abs(lon[i+1] - lon[i]) > np.pi:
            split[n] = i
            n =+ 1
    print(split)
        
        
    #plot ground track
    
    Earth_projection = "/Users/dylan/Desktop/orbit model/world.topo.bathy.200412.3x5400x2700.jpeg"
    fig, ax = plt.subplots()
    im = plt.imread(Earth_projection)
    ax.imshow(im, extent=[-180,180,-90,90])
    
    
    for i,split_i in enumerate(split):
        if i == 0:
            ax.plot(np.rad2deg(lon[:i]),np.rad2deg(lat[:i]))
        else:
            ax.plot(np.rad2deg(lon[i:i+1]),np.rad2deg(lat[:i+1]))

        
        
        
        
