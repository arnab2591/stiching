# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 13:58:35 2017

@author: Admin
"""

import cv2
import numpy as np
#optional argument
def nothing(x):
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('image')

#easy assigments
hh='Hue High'
hl='Hue Low'
sh='Saturation High'
sl='Saturation Low'
vh='Value High'
vl='Value Low'

cv2.createTrackbar(hl, 'image',0,179,nothing)
cv2.createTrackbar(hh, 'image',0,179,nothing)
cv2.createTrackbar(sl, 'image',0,255,nothing)
cv2.createTrackbar(sh, 'image',0,255,nothing)
cv2.createTrackbar(vl, 'image',0,255,nothing)
cv2.createTrackbar(vh, 'image',0,255,nothing)

while(1):
    _,frame=cap.read()
    # frame = cv2.imshow()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    #convert to HSV from BGR
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    #read trackbar positions for all
    hul=cv2.getTrackbarPos(hl, 'image')
    huh=cv2.getTrackbarPos(hh, 'image')
    sal=cv2.getTrackbarPos(sl, 'image')
    sah=cv2.getTrackbarPos(sh, 'image')
    val=cv2.getTrackbarPos(vl, 'image')
    vah=cv2.getTrackbarPos(vh, 'image')
    #make array for final values

    HSVLOW=np.array([hul,sal,val])
    HSVHIGH=np.array([huh,sah,vah])

    #apply the range on a mask
    mask = cv2.inRange(hsv,HSVLOW, HSVHIGH)
    res = cv2.bitwise_and(frame,frame, mask =mask)
    res_not = cv2.bitwise_not(res)
    cv2.imshow('image', res)
    cv2.imshow('yay', frame)
    cv2.imshow('image1', res_not)
    k = cv2.waitKey(50) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()