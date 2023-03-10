import cv2 as cv
import numpy as np

src = cv.imread("./test.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# cv.flip is inbuilt function opencv to rotate image  values 0,1,-1 are assigned for roation
dst1 = cv.flip(src, 0)
cv.imshow("x-flip", dst1)

dst2 = cv.flip(src, 1)
cv.imshow("y-flip", dst2)

dst3 = cv.flip(src, -1)
cv.imshow("xy-flip", dst3)

# if you want you can do it by reversing every cell in image by running 2 for loops also
h, w, ch = src.shape
dst = np.zeros(src.shape, src.dtype)
for row in range(h):
    for col in range(w):
        b, g, r = src[row, col]
        dst[row, w - col - 1] = [b, g, r]
cv.imshow("custom-y-flip", dst)

cv.waitKey(0)
cv.destroyAllWindows()
