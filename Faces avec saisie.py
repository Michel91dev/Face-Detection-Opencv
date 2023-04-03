#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:15:33 2023

@author: https://github.com/Np5123/Face-Detection-Opencv/blob/master/face-recognition

"""

#import the library
import cv2

#import the cascade for face and eye
face_cascade = cv2.CascadeClassifier("HaarCascade_FromOpenCV/haarcascade_eye.xml")
eye_cascade = cv2.CascadeClassifier("HaarCascade_FromOpenCV/haarcascade_eye.xml")
#create a function to detect the frame
def detect(gray,frame, scale_factor, min_neighbors):
    faces=face_cascade.detectMultiScale(gray,scale_factor,min_neighbors)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.1,2)
        for (ex,ey,eh,ew) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    return frame

#turn on the webcam
video=cv2.VideoCapture(0)

# Prompt de saisie des paramètres
scale_factor = float(input("Entrez le facteur d'échelle : "))
min_neighbors = int(input("Entrez le nombre minimum de voisins : "))

while True:
    _,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    canvas=detect(gray, frame, scale_factor, min_neighbors)

    cv2.imshow("video",canvas)
    if cv2.waitKey(1) & 0XFF==ord("q"):
        break
video.release()
cv2.destroyAllWindows
