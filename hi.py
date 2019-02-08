import numpy as np
import cv2

# Load an color image in greyscale

img = cv2.imread('m5.jpg',0)

# Make image symmetrical

resized = cv2.resize(img, (int(img.shape[1] * 2),int(img.shape[0] * 2)))

# Name of Image, and resize image (create label)

cv2.imshow('Shopping',resized)
print(img.shape)

# Close image, with any key

cv2.waitKey(0)
cv2.destroyAllWindows()
