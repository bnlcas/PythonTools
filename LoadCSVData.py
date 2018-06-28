# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:55:26 2018

@author: Benjamin Lucas
"""

import csv
import numpy as np
import Vector3
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt

def LoadData(filename):
    data_table = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data_table.append(row)
    return data_table

def RemoveBadRows(data_table, row_size):
    data_clean = []
    for row in data_table:
        try:
            row_clean = [float(x) for x in row]
            data_clean.append(row_clean)
        except:
            a = 1
    return data_clean

# Return the 
def ReturnField(data_table, field_ind, is_numeric = True, as_array = True):
    X = []
    for row in data_table:
        if (is_numeric):
            X.append(float(row[field_ind]))
        else:
            X.append(float(row[field_ind]))
    if(as_array):
        X = np.asarray(X)
    return X
    

#Get the matrix of 
def ReturnMatrix(data_table, column_inds):
    X = np.zeros([len(data_table), len(column_inds)])
    for i in range(len(data_table)):
        for j in range(len(column_inds)):
            try:
                X[i,j] = float(data_table[i][column_inds[j]])
            except:
                print(i)
    return X


## find elements of a numpy array x that equal a constant a
def Vectorized_Equals(vector, a):
    is_eq = lambda x: (x == a)
    vfunc = np.vectorize(is_eq)
    return vfunc(vector)


    
    
    
