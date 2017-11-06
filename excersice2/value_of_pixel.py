#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
import cv2

baboon = cv2.imread('Test_images/baboon.jpg')
barbara = cv2.imread('Test_images/barbara.png')
cameraman = cv2.imread('Test_images/cameraman.png')
coins = cv2.imread('Test_images/coins.png')
Lenna = cv2.imread('Test_images/Lenna.png')
rice_grains = cv2.imread('Test_images/rice_grains.jpg')

#RGB
print 'Values of the pixel at (20,25) in the RGB'
print 'baboon ' + (str(baboon[20,25]))
print 'barbara ' + (str(barbara[20,25]))
print 'cameraman ' + (str(cameraman[20,25]))
print 'coins ' + (str(coins[20,25]))
print 'Lenna ' + (str(Lenna[20,25]))
print 'rice_grains ' + (str(rice_grains[20,25]))

#YCrCb
print 'Values of the pixel at (20,25) in the YCrCb'
Y_baboon = cv2.cvtColor(baboon,cv2.COLOR_BGR2YCrCb)
print 'baboon ' + (str(Y_baboon[20,25]))
Y_barbara = cv2.cvtColor(barbara,cv2.COLOR_BGR2YCrCb)
print 'barbara ' + (str(Y_barbara[20,25]))
Y_cameraman = cv2.cvtColor(cameraman,cv2.COLOR_BGR2YCrCb)
print 'cameraman ' + (str(Y_cameraman[20,25]))
Y_coins = cv2.cvtColor(coins,cv2.COLOR_BGR2YCrCb)
print 'coins ' + (str(Y_coins[20,25]))
Y_Lenna = cv2.cvtColor(Lenna,cv2.COLOR_BGR2YCrCb)
print 'Lenna ' + (str(Y_Lenna[20,25]))
Y_rice_grains = cv2.cvtColor(rice_grains,cv2.COLOR_BGR2YCrCb)
print 'rice_grains ' + (str(Y_rice_grains[20,25]))

#HSV
print 'Values of the pixel at (20,25) in the HSV'
H_baboon = cv2.cvtColor(baboon,cv2.COLOR_BGR2HSV)
print 'baboon ' + (str(H_baboon[20,25]))
H_barbara = cv2.cvtColor(barbara,cv2.COLOR_BGR2HSV)
print 'barbara ' + (str(H_barbara[20,25]))
H_cameraman = cv2.cvtColor(cameraman,cv2.COLOR_BGR2HSV)
print 'cameraman ' + (str(H_cameraman[20,25]))
H_coins = cv2.cvtColor(coins,cv2.COLOR_BGR2HSV)
print 'coins ' + (str(H_coins[20,25]))
H_Lenna = cv2.cvtColor(Lenna,cv2.COLOR_BGR2HSV)
print 'Lenna ' + (str(H_Lenna[20,25]))
H_rice_grains = cv2.cvtColor(rice_grains,cv2.COLOR_BGR2HSV)
print 'rice_grains ' + (str(H_rice_grains[20,25]))

