#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:33:05 2022

@author: wsantos
"""
import numpy as np
from skimage.draw import disk
import random
import matplotlib.pyplot as plt

a = 60#int(input('Vertical: '))
b = 60#int(input('Horizontal: '))
forma_principal = (a,b)#tamanho da matriz grande
forma_img1 = (int(a), int(b))#tamanho da matriz do círculo, 5 vezes menor que a principal
r = forma_principal[0]/3 #Resolução da matriz do círculo 10 vezes menor que a principal
r = int(r)

img1 = np.zeros(forma_img1, dtype=np.uint8) # zeros
raio, centro = disk((30,30), r, shape = forma_img1) #Círculo com raio r dentro da matriz img1
img1[raio, centro]=1

plt.imshow(img1)

lista = []

for i in range(len(img1[0])):
    for j in range(len(img1[1])):
        if img1[i,j]==1:
            lista.append([j, len(img1)-i])
lista = np.array(lista)

file = open('Circulo_Simples', 'w')
np.savetxt(file, lista, fmt = '%i')