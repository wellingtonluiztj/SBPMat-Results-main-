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
#############################################################################################
########################### Dimensão da matriz do círculo ###################################
#############################################################################################

a = 120#int(input('Vertical: '))
b = 120#int(input('Horizontal: '))
forma_principal = (a,b)#tamanho da matriz grande
forma_img1 = (int(a/5), int(b/5))#tamanho da matriz do círculo, 5 vezes menor que a principal
r = forma_principal[0]/15 #Resolução da matriz do círculo 10 vezes menor que a principal
r = int(r)


img1 = np.zeros(forma_img1, dtype=np.uint8) # zeros
raio, centro = disk((r,r), r, shape = forma_img1) #Círculo com raio r dentro da matriz img1
img1[raio, centro]=1

r_quad = int(forma_img1[0]/2)

#--------------------Dimensão da Matriz principal-----------------------------
principal = np.zeros(forma_principal, dtype = np.uint8)


# Raio da esfera

##############################################################################################
################################ Pontos Aleatórios ###########################################
##############################################################################################
numero_de_graos=int(input('Número de grãos: '))
# Gerar centros aleatórios para alocação de img1 em principal
for i in range(numero_de_graos): # for para cada esfera
        x_centro = random.randint(r_quad,len(principal[0])-r_quad) # cria o ponto central aleatório
        y_centro = random.randint(r_quad,len(principal[1])-r_quad)
        
# Checar a sobreposição. Se houver ponto igual a 1, não deve começar a alocação
        aux = 0
        for j in range(int(x_centro-r_quad), int(x_centro+r_quad)):
            for k in range(int(y_centro-r_quad), int(y_centro+r_quad)):
                if principal[j][k] == 1:
                    aux += 1
# Alocar pontos da matriz img1 na matriz principal       
        l=0
        if aux == 0:
            for j in range(int(x_centro-r_quad), int(x_centro+r_quad)):# Varre a array da esfera do centro até o raio na vertical
                m = 0    
                for k in range(int(y_centro-r_quad), int(y_centro+r_quad)):# Varre na horizntal
                    principal[j][k] = img1[l][m]
                    m += 1
                l += 1

plt.imshow(principal)