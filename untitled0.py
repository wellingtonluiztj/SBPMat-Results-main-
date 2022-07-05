#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:15:19 2022

@author: wsantos
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:10:34 2022

@author: wellington
"""

import numpy as np
from skimage.draw import disk
import matplotlib.pyplot as plt
import random
from math import floor
import os

'''
Geometria
'''
#############################################################
################## Domínio computacional ####################
#############################################################
h = int(input('Horizontal Size: ')) # número de pontos na horizontal
x_inlet = 4
h = h - x_inlet
v = int((49*h)/138) # número de pontos na vertical mantendo a proporção h = 2.8*v


#############################################################
#################### Geometria do Poro ######################
#############################################################

v_s = int(v/2)
h_s = int(h/3)
shape_square = (v_s,h_s)
img = np.zeros(shape_square, dtype = np.uint8)

for xindex in range(3,v_s-3):
    for yindex in range(3,h_s-3):
        img[xindex][yindex] = np.clip(img[xindex][yindex], 1, 1) # torna 1 todos os locais indicados pelos índices
rock_matrix = np.hstack((np.vstack((img,img)), \
                         np.vstack((img,img)), \
                             np.vstack((img,img))))
plt.imshow(rock_matrix)

'''
Extract Coordinates
'''

p = []

for i in range(len(rock_matrix)):
    for j in range(len(rock_matrix[0])):
        if rock_matrix[i,j] == 1:
            p.append([j, len(rock_matrix)-i])

p = np.array(p)


cwd = os.getcwd() 
directory = '{}/R-1/obst-wall.d90'.format(cwd)
file = open(directory, "w")
np.savetxt(file, p + x_inlet, fmt='%i')


'''
Porosity Calculation
'''

pts = np.argwhere(rock_matrix==1)


soma_rock = np.sum(rock_matrix==1)
soma_vac = np.sum(rock_matrix==0)
forma = np.shape(rock_matrix)


#sea.heatmap(rock_matrix==1)

#soma_zeros

porosity = soma_vac/(soma_vac + soma_rock)
print(porosity)


