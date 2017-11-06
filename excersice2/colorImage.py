#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cv2
import numpy as np

src=cv2.imread('Test_images/Lenna.png')

cv2.namedWindow('Original image')
cv2.imshow('Original image',src)

#RGB
b,g,r=cv2.split(src)

cv2.imshow("Blue",b)
cv2.imwrite("RGB/Blue.jpg",b)

cv2.imshow("Green", g)
cv2.imwrite("RGB/Green.jpg",g)

cv2.imshow("Red",r)
cv2.imwrite("RGB/Red.jpg",r)


#YCrCb
YCrCb = cv2.cvtColor(src,cv2.COLOR_BGR2YCrCb)
y,cb,cr = cv2.split(YCrCb)

cv2.imshow("Y",y)
cv2.imwrite("YCrCb/Y.jpg",y)

cv2.imshow("Cb", cb)
cv2.imwrite("YCrCb/Cb.jpg",cb)

cv2.imshow("Cr",cr)
cv2.imwrite("YCrCb/Cr.jpg",cr)

#HSV
HSV=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
hue,saturation,value=cv2.split(HSV)

cv2.imshow("Hue",hue)
cv2.imwrite("HSV/Hue.jpg",hue)

cv2.imshow("Saturation", saturation)
cv2.imwrite("HSV/Saturation.jpg",saturation)

cv2.imshow("Value",value)
cv2.imwrite("HSV/Value.jpg",value)

cv2.waitKey(0)
cv2.destroyAllWindows()


