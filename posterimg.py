import cv2
import numpy as np

img = cv2.imread("poster.jpg")
rocket = img[120:360, 400:500]
img[0:240, 200:300] = rocket

text = "I love image processing"
cv2.putText(img, text, (20, 220), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 3, color = (0,0,255))

cv2.imshow("poster Image", img)
cv2.waitKey(0)
