from operator import le
import cv2 as cv
import numpy as np


img_lee = cv.imread("lee.png")
img_open = cv.imread("opencv.png")

test = cv.bitwise_xor(img_lee,img_open)

cv.imwrite("O xor Lee.png",test)
cv.imshow("OpenCV XOR Lee",test)

print(np.mean(test))

cv.waitKey(0)