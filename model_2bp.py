# 2-body problem
# state variables must be defined in km and km/s

def model_2bp(state,t):
    mu = 3.986004418E+05  # Earth's gravitational parameter  
                          # [km^3/s^2]
    r_x = state[0]
    r_y = state[1]
    r_z = state[2]
    v_x = state[3]
    v_y = state[4]
    v_z = state[5]
    r = (r_x ** 2 + r_y ** 2 + r_z ** 2) ** (1/2)
    
    r_x_dot = v_x
    r_y_dot = v_y
    r_z_dot = v_z
    v_x_dot = - mu * r_x / r ** 3
    v_y_dot = - mu * r_x / r ** 3
    v_z_dot = - mu * r_x / r ** 3
    
    state_dot = [r_x_dot, r_y_dot, r_z_dot, v_x_dot, v_y_dot, v_z_dot]
    return state_dot
    
    

