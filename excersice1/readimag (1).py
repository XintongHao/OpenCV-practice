
import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('Test_images/Lenna.png',0)


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


p = img.shape
print p
rows, cols = img.shape
for i in range(rows):
    for j in range(cols):
        k=img[i,j]
        print k

