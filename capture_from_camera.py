import numpy as np
import cv2

# Capture from Default Video Source

cap = cv2.VideoCapture(0)

# Define the video codec and create VideoWriter object -- continuing to follow the online tutorial.

fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Make XVID Codec - Write File to Output

out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the Flipped Frame to file
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release and continue everything if job is finished // stop application 
cap.release()
out.release()
cv2.destroyAllWindows()