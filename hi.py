import numpy as np
import cv2

# Load an color image in grayscale

img = cv2.imread('m5.jpg',0)

# Make image symmetrical.

resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.namedWindow('Shopping', cv2.WINDOW_NORMAL)
cv2.imshow('Shopping',resized)
print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
