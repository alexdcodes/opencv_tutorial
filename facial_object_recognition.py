import cv2
import numpy as np
from matplotlib import pyplot as plt

# Help us train the program to find objects, first we change to grayscale to train the application

img = cv2.imread('demo_watch.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()