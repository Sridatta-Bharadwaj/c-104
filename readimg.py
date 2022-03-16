import cv2
import numpy as np

black = np.zeros([600, 600])
black[263:516, 120:599] = 255
cv2.imshow("black image", black)
cv2.waitKey(0)
