#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:15:33 2023

@author: https://github.com/Np5123/Face-Detection-Opencv/blob/master/face-recognition

"""

#import the library
import cv2

cv2.destroyAllWindows


# Read image
img = cv2.imread('/Users/M/Documents/Dev Mike All/OpenCV Anaconda Python /COURS VIDEO/Face-Detection-Opencv (Michel)/Face-Detection-Opencv/Faces Images/Visage femme.jpg')

#img = cv2.imread('/Users/M/Documents/Dev Mike All/OpenCV Anaconda Python /OPENCV Code Michel (Spyder)/Images Michel/Michel Visio.jpg')


cv2.imshow('Visages',img)
cv2.waitKey(0)

cv2.destroyAllWindows
