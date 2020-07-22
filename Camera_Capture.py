#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:16:11 2020
imgpath = "/home/neel/Downloads/lena.jpg"
img = cv2.imread(imgpath, 1)
@author: neel
"""

"""
Camera Capture and display using matplotlib and opencv
Gray, HSV, BGR and RGB colour palettes explored
"""
import cv2
import matplotlib.pyplot as plt

def main():
    cam = cv2.VideoCapture(0)
    
    if cam.isOpened():
        ret, frame = cam.read()
        #print(ret)
        #print(frame)
    else:
        ret = False

    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
    plt.imshow(img1)
    plt.title('Color Image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    img1=frame
    
    plt.imshow(img1)
    plt.title('Color Image BGR')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    plt.imshow(img1)
    plt.title('Color Image HSV')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    plt.imshow(img1, cmap='gray')
    plt.title('Color Image Gray')
    plt.xticks([])
    plt.yticks([])
    plt.show()


    cam.release()

if __name__ == "__main__":
    main()