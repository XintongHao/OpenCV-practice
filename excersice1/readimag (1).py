
import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('Test_images/Lenna.png',0)


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print img.shape  #(512, 512)
print img.size  #262144
print img.dtype  #uint8
x = img[100][100]
print x  #116





