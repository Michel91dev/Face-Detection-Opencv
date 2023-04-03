#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 23:02:44 2023

@author: M
"""

import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    cv2.imshow('Camera Feed', frame)


cap.release()
cv2.destroyAllWindows()
