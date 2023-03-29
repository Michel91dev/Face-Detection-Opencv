#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:15:33 2023

@author: https://github.com/Np5123/Face-Detection-Opencv/blob/master/face-recognition

"""

#import the library
import cv2
#cv2.destroyAllWindows

#import the cascade for face and eye
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")



#create a function to detect the frame
def detect(gray,imgOrg):
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(imgOrg, (x,y), (x+w,y+h), (255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=imgOrg[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.1,2)
        for (ex,ey,eh,ew) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    return imgOrg



# Read image
img = cv2.imread("/Users/M/Documents/Dev Mike All/OpenCV Anaconda Python /COURS VIDEO/Face-Detection-Opencv (Michel)/Face-Detection-Opencv/Faces Images/Visage femme.jpg")

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display image
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL) # flag to allow the window to be resizable.



cv2.imshow("Original Image", img)


cv2.moveWindow( "Original Image" , 100,100)
cv2.imshow("Grayscale Image", gray_img)


w_X = cv2.getWindowImageRect("Original Image")[0] # 0=X, 1=Y, 2=width, 3=heigth
w_width = cv2.getWindowImageRect("Original Image")[2]

cv2.moveWindow( "Grayscale Image" , w_X + w_width + 3 ,100)

cv2.setWindowProperty("Original Image", cv2.WND_PROP_TOPMOST, 1) # censé mettre l'iamge original devant car elle apparait derrière Spyder ?!




canvas = detect(gray_img, img)
    cv2.imshow("Image avec visages" , canvas)


cv2.waitKey(0)

#while not(cv2.waitKey(1) & 0XFF==ord("q")):
 #       break
#video.release()
cv2.destroyAllWindows()
                      