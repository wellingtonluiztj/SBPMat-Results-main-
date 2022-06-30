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
import os

'''
Disk
'''
geometry = str(input('What geometry do you enter (square or disk)? '))

if geometry == 'disk':
    r = int(input('Choose Disk Radio : ')) #Resolution(matrix dimension)
    shape = ((2*r)+10, (2*r)+10)  #Array Shape 
    img1 = np.zeros(shape, dtype=np.uint8) # zeros
    raio, centro = disk((r,r), r, shape = shape) #Generate two different arrays
    img1[raio, centro]=1
    rock_matrix = np.hstack((np.vstack((img1,img1,img1)), np.vstack((img1,img1, img1)), np.vstack((img1,img1,img1))))
    plt.imshow(rock_matrix)
elif geometry == 'square':
    h = int(input('Square Size: '))
    l=h
    shape = (h,l) 
    img3 = np.zeros(shape, dtype=np.uint8)
    for xindex in range(9,len(img3)-10):
        for yindex in range(9,len(img3)-10):
            img3[xindex][yindex] = np.clip(img3[xindex][yindex], 1, 1)
    rock_matrix = np.hstack((np.vstack((img3,img3,img3)), np.vstack((img3,img3, img3)), np.vstack((img3,img3,img3))))
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

x_inlet = 20
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





