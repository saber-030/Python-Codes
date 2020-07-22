#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:16:11 2020
imgpath = "/home/neel/Downloads/lena.jpg"
img = cv2.imread(imgpath, 1)
@author: neel
"""
"""
Program to display a live video feed from default camera on computer
in gray, using opencv and matplotlib
"""
import cv2
import matplotlib.pyplot as plt


windowName = "Live Video Feed"
cv2.namedWindow(windowName)
#Default camera
cam = cv2.VideoCapture(0)

if cam.isOpened():
    ret, frame = cam.read()
else:
    ret = False
    
while ret:
    
    ret, frame = cam.read()
        
    output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    cv2.imshow(windowName, output)
#Break on pressing Esc
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()    

cam.release()

