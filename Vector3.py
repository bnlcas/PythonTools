# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 18:26:20 2018

@author: Benjamin Lucas
"""

# Handles nx3 matricies where each row is a 3-Vector

import numpy as np
from sklearn.preprocessing import normalize
from scipy.spatial.distance import cdist

def DotRows(v1, v2):
    return np.diag(np.matmul(v1, np.transpose(v2)))

def GetAngles(v1, v2):
    v1_norm = normalize(v1)
    v2_norm = normalize(v2)
    dotprod = DotRows(v1_norm, v2_norm)
    ang = np.arccos(np.clip(dotprod,-1,1))
    return ang
 
'''
def EuclideanDistance(v1, v2):
    return np.diag(cdist(v1,v2))

def Magnitude(v1):
    return EuclideanDistance(v1, np.zeros(np.shape(v1)))
    '''
def Magnitude(v1):
    return np.sqrt(DotRows(v1,v1))

def EuclideanDistance(v1, v2):
    return Magnitude(v1-v2)

def Project(v1, v_proj):
    v_proj_norm = normalize(v_proj)
    v1_projection_magnitude = DotRows(v1, v_proj_norm)
    v1_projection_magnitude_matrix = np.transpose(np.tile(v1_projection_magnitude, [3,1]))
    v1_projected = np.multiply(v_proj, v1_projection_magnitude_matrix)
    return v1_projected