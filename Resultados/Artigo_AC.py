#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 16:22:31 2022

@author: wsantos

Extract points from a image
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
from matplotlib import colors



img = cv2.imread('Contact_Angle.png', 2)
plt.figure()
plt.imshow(img)
#####################  Point  #######################
meioy = 14
meiox = 328
plt.hlines(y=meioy, xmin=0, xmax=np.shape(img)[1], color='b')
plt.vlines(x=meiox, ymin=0.0, ymax=np.shape(img)[0], color='b')
#####################################################

######################   Scale   ####################
#y
scale_ymin = 2
scale_ymax = 62
plt.hlines(y=scale_ymin, xmin=0, xmax=np.shape(img)[1], color='g', linestyle='dashed')
plt.hlines(y=scale_ymax, xmin=0, xmax=np.shape(img)[1], color='g', linestyle='dashed')
#x

#####################################################

#####################  Bounderies  #################

boundx = 55
boundy = 240
plt.vlines(x=boundx, ymin=0.0, ymax=np.shape(img)[0], color='tab:brown', linewidth=3)
plt.hlines(y=boundy, xmin=0, xmax=np.shape(img)[1], color='tab:brown', linewidth=3)


####################################################
scale_y = scale_ymax - scale_ymin #escala em 
Point_y = meioy - scale_ymin


##################  Conversão  ####################

y = (8*Point_y)/scale_y
y = 32 - y
print(y)
