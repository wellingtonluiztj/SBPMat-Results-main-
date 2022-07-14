#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:18:51 2022

@author: wsantos
"""
import numpy as np
from skimage.draw import disk
import random

'''
O círculo deve ter tamanho 
'''

a = int(input('Vertical: '))
b = int(input('Horizontal: '))

forma = (a,b)

# Criaro primeiro array
r = forma[0]/10 #Resolution(matrix dimension)
r = int(r)
shape = ((2*r), (2*r))  #Array Shape 
img1 = np.zeros(shape, dtype=np.uint8) # zeros
raio, centro = disk((r,r), r, shape = shape) #Generate two different arrays
img1[raio, centro]=1

# Criar o segundo array
principal = np.zeros(forma,dtype = np.uint8)


#Raio da esfera


# Varrer os pontos 
for i in range(forma[0]): # for para cada esfera
        x_centro = random.randint(0,len(shape)) # cria o ponto central
        y_centro = random.randint(0,len(shape))
        for j in range([x_centro,y_centro]-r, [x_centro,y_centro]-r):# Varre a array da esfera do centro até o raio na vertical
            for k in range([x_centro,y_centro]-r, [x_centro,y_centro]-r):# Varre na horizntal
                principal[i][j] = img1[j][k]

