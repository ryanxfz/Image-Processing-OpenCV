import cv2
import numpy as np

#HSV = Hue, Saturation, Value(Brightness)

#img = cv2.imread('mask.png')
#cv2.imshow('img', img)
#img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow('HSV', img_hsv)

img_mask = cv2.imread('mask.png')
#cv2.imshow('img', img_mask)
img_yoshi = cv2.imread('yoshi.png')
img_hsv = cv2.cvtColor(img_yoshi, cv2.COLOR_BGR2HSV)

whitePixels = np.where(img_mask == 255)

img_hsv[whitePixels[0], whitePixels[1], 0] = 123

modified_yoshi = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('Normal Yoshi', img_yoshi)
cv2.imshow('Masked Yoshi', modified_yoshi)

cv2.waitKey(0)
cv2.destroyAllWindows()