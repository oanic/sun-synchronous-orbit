#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RaDec2LonLat: converts right ascension and declination of a spacecraft to longitude and latitude


INPUTS
 dec: declination of s/c [rad]
 RA: right ascension of s/c [rad]
 GAST_t0: Greenwich apparent sidereal time at t0 [rad]
 w_e: Earth's rotation rate [rad/s]
 t0: initial time [s]
 t: time [s]
 
Created 2023-06-29 by Oana Nica
"""
import numpy as np

def RaDec2LonLat(dec,RA,GAST_t0,w_e,t0,t):
    
    lat = dec
    lon = (RA - GAST_t0) - w_e * (t - t0)
    
    if lon > np.pi:
        lon = lon - 2 * np.pi
    elif lon < -np.pi:
        lon = lon + 2 * np.pi
    
    return lon, lat