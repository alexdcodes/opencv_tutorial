import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('m.jpg',0)

resized = cv2.resize(img, (600,600))

cv2.namedWindow('Shopping', cv2.WINDOW_NORMAL)
cv2.imshow('Shopping',resized)
print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
