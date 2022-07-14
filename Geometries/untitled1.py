#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:51:27 2022

@author: wsantos
"""
import numpy as np
import matplotlib.pyplot as plt
import math

# Aqui, calculamos o número de Reynolds, Mach e Knudsen
c = 340.29
scale = str(input('What Scale you want to work (mm), (cm)? '))
if scale == 'mm':
    tens = 10**(-6)# Definido em metros
    L = float(input('Comprimento da amostra em micrometros: '))
    L = L*(tens)
    nu = float(input('Viscosidade do fluido: '))
    nu = nu*10**(-6)
    raio = float(input('Raio da amostra: '))
    raio = raio*tens
    A = 3.14*raio**2
    vasao = float(input('Vasão em m^3/s: '))
    u = A*vasao
    Ma = u/c
    Re = (u*L)/nu
    Kn = Ma/Re
    print(f'O número de Reynolds é {Re}, o número de Mach é {Ma} e o de Knudsen é {Kn}.')
elif scale == 'cm':
    tens = 10**(-2)# Definido em metros
    L = 7.07
    L = L*(tens)
    nu = 0.6752
    nu = nu*10**(-6)
    raio = 1.255
    raio = raio*tens
    A = 3.14*raio**2
    vasao = 0.00000016
    u = A*vasao
    Ma = u/c
    Re = (u*L)/nu
    Kn = Ma/Re
    print(f'O número de Reynolds é {Re}, o número de Mach é {Ma} e o de Knudsen é {Kn}.')
    
L_L = float(input('Defina a resolução em unidades de LBM: '))
dx = L/L_L
print(f'dx = {dx}m')


#Essa parte determina o valor da viscosidade cinemática a  partir da viscosidade dinâmica e densidade da salmora
rho_L = 1 # Definido por arbitrariedade
rho_b = 1058.058 # em kg/m^3
rho_o = 829 # em kg/m^3
rho = (rho_b+rho_o)/2
dm = (rho/rho_L)*(dx)**3
print(f'dm = {dm} ')

#Essa parte faz o cálculo da viscosidade cinemática em unidades de redes de Boltzmann usando o tempo de relaxação.
gamma = 0.0105
gamma_L = 0.1#0.1
dt = ((dm*gamma_L)/gamma)**(1/2)
print(f'dt = {dt} s.')

u_L = (dt/dx)*u
print(f'A velocidade em redes de Boltzmann é {u_L}.')

tau_L = float(input('Tempo de relaxação maior que 0.5: '))
nu_L = (1/3)*(tau_L-0.5)
Ma_L = u_L/1/(3**(1/2))
while True:
    if Ma_L < 0.3:
        break
    else:
        u_L = float(input('Velocidade com número de Mach menor que 0.3: '))
        Ma_L = u_L/(1/(3**(1/2)))      
Re_L =  u_L*L_L/nu_L
erro = 10
if Re_L+erro < Re_L < Re_L-erro:
    print('ok')
    print(f'O valor do Re_L é {Re_L}, de Mach é {Ma_L}, do tempo de relaxação é {tau_L}.')
else:
    print('no')
    print(f'O valor do Re_L é {Re_L}, de Mach é {Ma_L}, do tempo de relaxação é {tau_L}.')
    
#Essa parte determina o valor da viscosidade em unidades de redes de Boltzmann
nu_o = 4.6
nu_o = (nu_o)*(10**(-6))
nu_Lo = ((dt)/(dx)**2)*nu_o
#Essa parte calcula o tempo de relaxação do óleo
tau_o = 3*nu_Lo + 1/2
print(f'tau_o = {tau_o}.')

#Essa parte determina o parâmetro de tensão interfacial
#====Interfacial Tension Brine====
#gamma = float(input('Valor de tensão interfacial do sistema fluido/fluido: '))
#gamma_L = gamma*(((dt)**2)/dm)
#print(gamma_L)
D = ((1.721)**2 - 4*(-1.361)*(- 0.178+gamma_L ))
x1 = (-(1.721) + D**(1/2)) / (2*(-1.361))
x2 = (-(1.721) - D**(1/2)) / (2*(-1.361))
print(f'Os valores de g são {x1} e {x2}.')