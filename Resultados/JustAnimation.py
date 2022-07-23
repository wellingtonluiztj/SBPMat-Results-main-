#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 13:54:26 2022

@author: wsantos
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:00:02 2022

@author: wsantos
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib.colors import Normalize
from scipy import ndimage
from matplotlib import animation


#carrega as matrizes e organiza em ordem
datas = glob.glob("gnu_output/*")#Lista os pathnames na pasta de forma desordenada
datas.sort()#Organiza os nomes dos caminhos
#exemplo de um arquivo

data =  np.loadtxt("gnu_output/RES-010.dat",skiprows=1) #carrega a matriz

x,y = data[:,0],data[:,1] #escreve nas variáveis x e y os valores da coluna 0 e 1 respectivamente

den_1,den_2,is_wall = data[:,3], data[:,4],data[:,7] #perfil de densidade 2
#verifica se é parede ou não

den_1 = den_1.reshape((int(np.amax(x)),int(np.amax(y)))) # reshape da densidade para array
den_2 = den_2.reshape((int(np.amax(x)),int(np.amax(y)))) # reshape da densidade para array
is_wall = is_wall.reshape((int(np.amax(x)),int(np.amax(y))))# 
den_1 = np.transpose(den_1)
is_wall = np.transpose(is_wall)

for i in range(len(den_1)):
    for j in range(len(den_1[1])):
        if den_1[i,j]==0:
            den_1[i,j]=4

img = [] # some array of images
frames = [] # for storing the generated images
i = 0

list_of_datas = []
for file in datas:#[:10]:
    
    data =  np.loadtxt(file,skiprows=1)
    
    list_of_datas.append(is_wall + den_1 + den_2) # adiciona quem virará vídeo

    i+=1
    

fig = plt.figure()
myimages = []

for i in list_of_datas:
    frame = i
    cmap = plt.cm.jet
    plt.axis('off')
    #norm = Normalize(vmin=np.amin(list_of_datas), vmax=np.amax(list_of_datas))
    imgplot = plt.imshow(frame, cmap=cmap)
    myimages.append([imgplot])

plt.colorbar()

#interval -> tanto faz
my_anim = animation.ArtistAnimation(fig, myimages, interval=True, blit=False, repeat=True)

f = 'animation-2.mp4'
writervideo = animation.FFMpegWriter(fps=6)
my_anim.save(f, writer=writervideo)

