# 2-body problem, including perturbation due to J2 
# state variables must be defined in km and km/s

import constants

def model_2bp_J2(state,t):


    x = state[0]
    y = state[1]
    z = state[2]
    v_x = state[3]
    v_y = state[4]
    v_z = state[5]
    r = (x ** 2 + y ** 2 + z ** 2) ** (1/2)
    
    # J2 acceleration
    C_J2 = -3/2 * constants.J2 * (constants.mu_e/r**2) * (constants.R_e/r)**2
    a_x_J2 = C_J2 * (1 - 5*(z/r)**2) * x/r
    a_y_J2 = C_J2 * (1 - 5*(z/r)**2) * y/r
    a_z_J2 = C_J2 * (3 - 5*(z/r)**2) * z/r
   
    # Time derivatives
    x_dot = v_x
    y_dot = v_y
    z_dot = v_z
    v_x_dot = - constants.mu_e * x / r ** 3 + a_x_J2
    v_y_dot = - constants.mu_e * y / r ** 3 + a_y_J2
    v_z_dot = - constants.mu_e * z / r ** 3 + a_z_J2

    state_dot = [x_dot, y_dot, z_dot, v_x_dot, v_y_dot, v_z_dot]
    return state_dot
    
    



    