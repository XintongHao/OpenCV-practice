#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import random

def Add_gaussian_Noise(srcArr,mean,sigma):
    NoiseArr = srcArr.copy()
    NoiseArr = np.random.normal(mean, sigma, NoiseArr.shape)
    np.add(srcArr, NoiseArr, srcArr,casting="unsafe")
    return
    
def Add_salt_pepper_Noise(srcArr, pa, pb):
    rows,cols = srcArr.shape
    amount1 = rows*cols*pa
    amount2 = rows*cols*pb
    for counter in range(int(amount1)):
        srcArr[ int(random.uniform(0,rows)) ][ int(random.uniform(0,cols)) ] = 0
    for counter in range(int(amount2)):
        srcArr[ int(random.uniform(0,rows)) ][ int(random.uniform(0,cols)) ] = 225    
        
def main():
    image = cv2.imread('Test_images/baboon.jpg',0)
    cv2.namedWindow('Original image')
    cv2.imshow('Original image', image)
    
    #Gaussian Noise
    noise_img = image.copy()
    mean=20
    sigma=50
    Add_gaussian_Noise(noise_img, mean, sigma)
    cv2.imshow('Gaussian Noise',noise_img)
    cv2.imwrite('Gaussian Noise.jpg',noise_img)
    
    #Box filter
    noise_dst = noise_img.copy()
    cv2.blur(noise_dst,(7,7))
    cv2.imshow('Box filter1',noise_dst)
    cv2.imwrite('Box filter1.jpg',noise_dst)
       
    #Gaussian filter
    noise_dst1 = noise_img.copy()
    cv2.GaussianBlur(noise_dst1, (7,7), 1.5)
    cv2.imshow('Gaussian filter1',noise_dst1)
    cv2.imwrite('Gaussian filter1.jpg',noise_dst1)
    
    #Median filter
    noise_dst2 = noise_img.copy()
    cv2.medianBlur(noise_dst2,7)
    cv2.imshow('Median filter1',noise_dst2)
    cv2.imwrite('Median filter1.jpg',noise_dst2)  
    
    #Salt and Pepper Noise
    noise_img2 = image.copy()
    pa=0.01
    pb=0.01
    Add_salt_pepper_Noise(noise_img2, pa, pb)
    cv2.imshow('Salt and Pepper Noise',noise_img2)
    cv2.imwrite('Salt and Pepper Noise.jpg',noise_img2) 
    
    #Box filter
    noise_dst3 = noise_img2.copy()
    cv2.blur(noise_dst3, (7,7))
    cv2.imshow('Box filter2',noise_dst3)
    cv2.imwrite('Box filter2.jpg',noise_dst3)
    
    #Gaussian filter
    noise_dst4 = noise_img2.copy()
    cv2.GaussianBlur(noise_dst4, (7,7), 1.5)
    cv2.imshow('Gaussian filter2',noise_dst4)
    cv2.imwrite('Gaussian filter2.jpg',noise_dst4)
    
    #Median filter
    noise_dst5 = noise_img2.copy()
    cv2.medianBlur(noise_dst5,7)
    cv2.imshow('Median filter2',noise_dst5)
    cv2.imwrite('Median filter2.jpg',noise_dst5)  
    
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    main()   

                      