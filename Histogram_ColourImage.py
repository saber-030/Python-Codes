#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:16:11 2020
imgpath = "/home/neel/Downloads/lena.jpg"
img = cv2.imread(imgpath, 1)
@author: neel
"""
"""
Program to find intensity of R G & B colours per pixel, range 0 to 255, 
in an image, using opencv, matplotlib and numpy
"""
import cv2
import matplotlib.pyplot as plt
import numpy


    
path = "/home/neel/Downloads/lena.jpg"
impath = path
img = cv2.imread(impath, 1)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
R,G,B=cv2.split(img)    
# plt.subplot(1, 2, 1)
# plt.imshow(img)
# plt.title('Image')
# plt.xticks([])
# plt.yticks([])


#Subplot to display intensity of Red in each pixel
plt.subplot(1, 3, 1)
plt.hist(R.ravel(), 256, [0, 255])
plt.title('Red Histogram')
plt.xlim(xmin=0, xmax=256)
plt.show()
    
#Subplot to display intensity of Green in each pixel
plt.subplot(1, 3, 2)
plt.hist(G.ravel(), 256, [0, 255])
plt.title('Green Histogram')
plt.xlim(xmin=0, xmax=256)
plt.show()
    
#Subplot to display intensity of Blue in each pixel
plt.subplot(1, 3, 3)
plt.hist(B.ravel(), 256, [0, 255])
plt.title('Blue Histogram')
plt.xlim(xmin=0, xmax=256)
plt.show()



