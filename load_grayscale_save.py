import numpy as np
import cv2

img = cv2.imread('m5.jpg',0)

cv2.imshow('image',img)
x = cv2.waitKey(0)
if x == 27:

    # ESC key to exit

    cv2.destroyAllWindows()
elif x == ord('s'):

    # 'S' key to save and exit

    cv2.imwrite('gray.png',img)
    cv2.destroyAllWindows()
