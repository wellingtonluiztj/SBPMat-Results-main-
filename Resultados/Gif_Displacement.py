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
datas = glob.glob("datas/*")
datas.sort()
#exemplo de um arquivo

data =  np.loadtxt("datas/RES-010.dat",skiprows=1) #carrega a matriz

x,y = data[:,0],data[:,1] #carrega x e y

den_1 = data[:,3] #perfil de densidade 1
den_2 = data[:,4] #perfil de densidade 2

is_wall = data[:,7] #verifica se é parede ou não

den_1 = den_1.reshape((int(np.amax(x)),int(np.amax(y)))) # reshape da densidade para array
den_2 = den_2.reshape((int(np.amax(x)),int(np.amax(y)))) # reshape da densidade para array

is_wall = is_wall.reshape((int(np.amax(x)),int(np.amax(y))))# 

plt.figure(figsize=(12,12))

plt.subplot(311)
plt.title("Parede")
plt.imshow(is_wall)
plt.colorbar()

plt.subplot(312)
plt.title("Densidade 1")
plt.imshow(den_1)
plt.colorbar()

plt.subplot(313)
plt.title("Densidade 2")
plt.imshow(den_2)
plt.colorbar()

plt.tight_layout()

img = [] # some array of images
frames = [] # for storing the generated images
i = 0

list_of_datas = []
for file in datas:#[:10]:
    
    data =  np.loadtxt(file,skiprows=1)
    
    y,x = data[:,0],data[:,1]

    den_1 = data[:,3]
    den_2 = data[:,4]
    is_wall = data[:,7]

    den_1 = den_1.reshape((int(np.amax(x)),int(np.amax(y))))
    den_2 = den_2.reshape((int(np.amax(x)),int(np.amax(y))))

    is_wall = is_wall.reshape(int(np.amax(y)),(int(np.amax(x))))
    
    list_of_datas.append(is_wall + den_1) # adiciona quem virará vídeo

    i+=1
    

fig = plt.figure()
myimages = []

for i in list_of_datas:
    frame = i
    cmap = plt.cm.jet
    norm = Normalize(vmin=np.amin(list_of_datas), vmax=np.amax(list_of_datas))
    frame2 = cmap(norm(frame))
    imgplot = plt.imshow(frame, cmap=cmap)
    myimages.append([imgplot])

plt.colorbar()

#interval -> tanto faz
my_anim = animation.ArtistAnimation(fig, myimages, interval=0.001, blit=False, repeat=True)

f = 'animation.mp4'
writervideo = animation.FFMpegWriter(fps=12)
my_anim.save(f, writer=writervideo)
