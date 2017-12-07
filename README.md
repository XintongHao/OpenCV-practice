# OpenCV_practice

## Copyright: Xintong Hao
 Email: hxtong@bu.edu

## Exercise 1
### How does a program read the cvMat object, in particular, what is the order of the pixel structure?

Use the function of imread() to read image and read each pixel as a matrix

## Exercise 2
### Print out the values of the pixel at (20,25) in the RGB, YCbCr and HSV versions of the image. What are the ranges of pixel values in each channel of each of the above mentioned colorspaces?

<img src="https://github.com/XintongHao/OpenCV_practice/blob/master/excersice2/value.png" />

## Exercise 3
### Which filter seems to work ”better” for images with salt-and-pepper noise and gaussian noise?

Median Filter works better for salt-and-pepper noise and the Gaussian Filter works better for gaussian noise.
As kernel increase, the results turn to indistinct.

## Exercise 4
### What are the disadvantages of binary threshold? 

The BinaryThreshold will highlight part of the features but ignore the others.

### When is Adaptive Threshold useful?

It could multiple thresholds at the same time, so it is useful when we want to perform multiple processes on the same image at different levels.
