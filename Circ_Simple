#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:18:51 2022

@author: wsantos
"""
import numpy as np
from skimage.draw import disk
import random
import matplotlib.pyplot as plt

'''
O círculo deve ter tamanho 
'''
#-------------------- Dimensão da matriz do círculo--------------------------
a = 120#int(input('Vertical: '))
b = 120#int(input('Horizontal: '))
forma_principal = (a,b)#tamanho da matriz grande
forma_img1 = (int(a/5), int(b/5))#tamanho da matriz do círculo, 5 vezes menor que a principal
r = forma_principal[0]/15 #Resolução da matriz do círculo 10 vezes menor que a principal
r = int(r)

img1 = np.zeros(forma_img1, dtype=np.uint8) # zeros
raio, centro = disk((r,r), r, shape = forma_img1) #Círculo com raio r dentro da matriz img1
img1[raio, centro]=1

#--------------------Dimensão da Matriz principal-----------------------------
principal = np.zeros(forma_principal, dtype = np.uint8)


#Raio da esfera

#------------------Incluir uma na outra---------------------------------------
# Varrer os pontos 
numero_de_graos=int(input('Número de grãos: '))
for i in range(numero_de_graos): # for para cada esfera
        x_centro = random.randint(0+r,len(principal[0])-r) # cria o ponto central aleatório
        y_centro = random.randint(0+r,len(principal[1])-r)
        for m in range(len(img1[0])):
            for n in range(len(img1[1])):
                principal[j][k]=img1[m][n]
plt.imshow(principal)