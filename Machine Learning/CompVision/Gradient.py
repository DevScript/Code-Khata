import cv2 as cv

img = cv.imread("audrey.jpg", 0)
src = cv.resize(img, (700, 600))
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

se = cv.getStructuringElement(cv.MORPH_RECT, (5, 5), (-1, -1))
basic = cv.morphologyEx(src, cv.MORPH_GRADIENT, se)
cv.imshow("basic gradient", basic)

dilate = cv.morphologyEx(src, cv.MORPH_DILATE, se)
exteral = cv.subtract(dilate, src)
cv.imshow("external gradient", exteral)

erode = cv.morphologyEx(src, cv.MORPH_ERODE, se)
interal = cv.subtract(src, erode)
cv.imshow("interal gradient", interal)

cv.imwrite("gradient.png", basic)
cv.imwrite("external.png", exteral)
cv.imwrite("interal.png", interal)
cv.waitKey(0)
cv.destroyAllWindows()
