#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:15:33 2023

@author: https://github.com/Np5123/Face-Detection-Opencv/blob/master/face-recognition
Modifyed By Michel Safars
"""
import cv2

# import the cascade for face and eye
face_cascade = cv2.CascadeClassifier("HaarCascade_FromOpenCV/haarcascade_eye.xml")
eye_cascade = cv2.CascadeClassifier("HaarCascade_FromOpenCV/haarcascade_eye.xml")


# create a function to detect the frame
def detect(gray, imgOrg):
    faces = face_cascade.detectMultiScale(gray, 1.2, 7) // 1.2 et 7 donnent de bon résultats sur mon image
    for (x, y, w, h) in faces:
        cv2.rectangle(imgOrg, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = imgOrg[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 2)
        for (ex, ey, eh, ew) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)
    return imgOrg

# Read image
img = cv2.imread("Faces Images/Visage femme.jpg")

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display image
#cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)  # flag to allow the window to be resizable.
cv2.imshow("Original Image", img)

cv2.moveWindow("Original Image", 100, 100)

cv2.imshow("Grayscale Image", gray_img)

# replaçons la fenêtre en haut de l'écran à gauche
w_X = cv2.getWindowImageRect("Original Image")[0]  # 0=X, 1=Y, 2=width, 3=height
w_width = cv2.getWindowImageRect("Original Image")[2]

# et la deuxième à coté
cv2.moveWindow("Grayscale Image", w_X + w_width + 3, 100)

canvas = detect(gray_img, img) # ▶️

cv2.imshow("Image avec visages", canvas)

# Move the "Image avec visages" window next to the "Grayscale Image" window
gray_w_X = cv2.getWindowImageRect("Grayscale Image")[0] # 🔴 bug ou erreur, mais la valeur est de 1606 ce qui n'est pas logique puisque la fenetre 2 a x=200 (et width=600)
gray_w_width = cv2.getWindowImageRect("Grayscale Image")[2]

#cv2.moveWindow("Image avec visages", w_X * 2 + gray_w_width * 2 + 3, 100)
cv2.moveWindow("Image avec visages", gray_w_X + gray_w_width + 3, 100)

cv2.waitKey(0)

cv2.destroyAllWindows()
