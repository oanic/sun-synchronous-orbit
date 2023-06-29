# groundTrack
# plot ground track of an orbit
# state: state of the orbit (cartesian coordinates) at a given initial time
# long_gw: longitude of Greenwich meridian at initial time [rad]
# w_e: Earth's rotation rate [rad/s]
# t_vect: vector of times at which the ground track is computed

from ECI2RaDec import ECI2RaDec

def ground_track(state,long_gw,w_e,t_vect):
    dec = np.zeros(len(t_vect))
    RA = np.zeros(len(t_vect))

    for i, t in enumerate(t_vect):
        
        # convert from cartesian coordinates in ECI frame to RA and dec
        [dec[i],RA[i]] = ECI2RaDec(state[i,:])
    
        # convert from RA and dec to long,lat
    
    
def RaDec2LonLat(dec,RA,)