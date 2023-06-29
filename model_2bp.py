# 2-body problem
# state variables must be defined in km and km/s

import constants

def model_2bp(state,t):

    x = state[0]
    y = state[1]
    z = state[2]
    v_x = state[3]
    v_y = state[4]
    v_z = state[5]
    r = (x ** 2 + y ** 2 + z ** 2) ** (1/2)
    
    x_dot = v_x
    y_dot = v_y
    z_dot = v_z
    v_x_dot = - constants.mu * x / r ** 3
    v_y_dot = - constants.mu * y / r ** 3
    v_z_dot = - constants.mu * z / r ** 3
    
    state_dot = [x_dot, y_dot, z_dot, v_x_dot, v_y_dot, v_z_dot]
    return state_dot
    
    

