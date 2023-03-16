# in this code u will learn how to add two images together
import cv2 as cv
import numpy as np

src = cv.imread("./audrey.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

h, w = src.shape[:2]
dst = cv.edgePreservingFilter(  # this filter smooths away the noise at edges it can be used to create cartoon like images of real people.
    src, sigma_s=100, sigma_r=0.4, flags=cv.RECURS_FILTER)
result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
# divided intial image in two parts this is how images are joined .
result[0:h, w:2*w, :] = dst
result = cv.resize(result, (w, h//2))
cv.imshow("result", result)

cv.waitKey(0)
cv.destroyAllWindows()
