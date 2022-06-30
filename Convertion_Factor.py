# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:39:38 2022

@author: welli
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 10:34:29 2022
Rotine: Calculate the convertion factors for LBM simulation
@author: wsantos
"""


#Packages
import matplotlib.pyplot as plt
import math
import matplotlib.pyplot as plt
import math


'''
Setting the Characteristic Scale dx, dm, dt
Comments: Need to creat a option to select what scale we are working
'''


scale = str(input('What Scale you want to work --- (mm), (cm)? '))
if scale == 'mm':
    tens = 10**(-6)
elif scale == 'cm':
    tens = 10**(-2)

    
#====Determine dx====
L = float(input('Sample Lenght in centimeters: '))
L = L*(tens)
N = int(input('Number of nodes: '))
d_X = L/N


#====Determine dm====
rho1 = float(input('Brine Density: '))
rho2 = 829              #float(input('Oil Density: '))
d_M = ((rho1+rho2)/2)*(d_X)**(3)


#====Determine dt====
gamma = float(input('Interfacial Tension: '))
gamma_LBM = 0.1
d_T = math.sqrt((gamma_LBM/gamma)*d_M)


'''
Relaxation time
'''


#====RelaxationTime Brine====
nu_brine = float(input('Brine Viscosity: '))
nu_brine = nu_brine*10**(-6)
nu_brine_LBM = (nu_brine)*(d_T/(d_X)**2)
tau_brine = (3*nu_brine_LBM)+0.5


#====Relaxation Time Oil====
nu_oil = float(input('Oil Viscosity: '))
nu_oil = nu_oil*10**(-6) 
nu_oil_LBM = (nu_oil)*(d_T/(d_X)**2)
tau_oil = (3*nu_oil_LBM)+0.5


'''
Force Parameter
'''


#====Interfacial Tension Brine====
D = ((-1.721)**2 - 4*1.361*(gamma_LBM + 0.178))
x1 = (-(-1.721) + D**(1/2)) / (2*(1.361))
x2 = (-(-1.721) - D**(1/2)) / (2*(1.361))


print(f'Os valores das variáveis são tau_b = {tau_brine}, tau_o = {tau_oil}, gk,k={x1} ou gk,k={x2}')


d_V = d_X/d_T #Velocity



