#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:18:51 2022

@author: wsantos
"""
import numpy as np
from skimage.draw import disk
import random
from mpl_toolkits.mplot3d import Axes3D
from skimage.morphology import cube
#############################################################################################
##################################### Matrizes ##############################################
#############################################################################################

'''
Matriz principal
'''
a = 120#int(input('Vertical: '))
b = 120#int(input('Horizontal: '))
c = 120
forma_principal = (a,b,c)#tamanho da matriz grande
principal = np.zeros(forma_principal, dtype = np.uint8)
x = np.shape(principal)
numero = x[0]*x[1]*x[2]
'''
Matriz Cubo
'''
forma_img1 = int(a/10) #tamanho da matriz do círculo, 5 vezes menor que a principal
img1 = cube(forma_img1)
r = int(forma_img1/2)

##############################################################################################
################################ Pontos Aleatórios ###########################################
##############################################################################################

numero_de_graos=int(input('Número de grãos: '))
# Gerar centros aleatórios para alocação de img1 em principal
for t in range(numero_de_graos): # for para cada esfera
        x_centro = random.randint(r,len(principal[0])-r) # cria o ponto central aleatório
        y_centro = random.randint(r,len(principal[1])-r)
        z_centro = random.randint(r,len(principal[2])-r)
        aux = 0
        # Checar a sobreposição. Se houver ponto igual a 1, não deve começar a alocação
        for i in range(int(x_centro-r), int(x_centro+r)):
            for j in range(int(y_centro-r), int(y_centro+r)):
                for k in range(int(z_centro-r), int(z_centro+r)):
                    if principal[i][j][k] == 1:
                            aux += 1
# Alocar pontos da matriz img1 na matriz principal       
            l=0
            if aux == 0:
                for j in range(int(x_centro-r), int(x_centro+r)):# Varre a array da esfera do centro até o raio na vertical
                    m = 0    
                    for k in range(int(y_centro-r), int(y_centro+r)):# Varre na horizntal
                        principal[j][k] = img1[l][m]
                        m += 1
                        l += 1


##############################################################################################
################################ Alocando em um array ########################################
##############################################################################################

p = []

for i in range(len(principal)):
    for j in range(len(principal[0])):
        if principal[i,j] == 1:
            p.append([j, len(principal)-i])

p = np.array(p)


p = np.array(p)

x_inlet = 20
 
file = open('Poros_Regulares_Circulares','w')
np.savetxt(file, p + x_inlet, fmt='%i')


########################################################################################################################
########################################### cálculo de Porosidade ######################################################
########################################################################################################################

pts = np.argwhere(principal==1)


soma_rock = np.sum(principal==1)
soma_vac = np.sum(principal==0)
forma = np.shape(principal)


#sea.heatmap(rock_matrix==1)

#soma_zeros

porosity = soma_vac/(soma_vac + soma_rock)
print(f'A porosidade do modelo é {porosity}.')
