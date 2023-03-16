import cv2 as cv
import numpy as np


def canny_demo(image):
    t = 80
    canny_output = cv.Canny(image, t, t * 2)
    return canny_output


src = cv.imread("stuff.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
binary = canny_demo(src)  # will get binary image
k = np.ones((3, 3), dtype=np.uint8)
binary = cv.morphologyEx(binary, cv.MORPH_DILATE, k)

contours, hierarchy = cv.findContours(  # this function only works on binary images
    binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    # will surround the area with an ellipse
    (cx, cy), (a, b), angle = cv.fitEllipse(contours[c])
    cv.ellipse(src, (np.int32(cx), np.int32(cy)),
               (np.int32(a/2), np.int32(b/2)), angle, 0, 360, (0, 0, 255), 2, 8, 0)

cv.imshow("contours_analysis", src)
cv.imwrite("contours_analysis.png", src)

# when object is straight line
src = cv.imread("pencil.jpg")
new = cv.resize(src, (800, 600))
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", new)
binary = canny_demo(new)
linesP = cv.HoughLinesP(binary, 1, np.pi / 180, 55, None,
                        50, 10)  # to detect sharp lines
cv.HoughLinesP
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(new, (l[0], l[1]), (l[2], l[3]), (255, 0, 0), 1, cv.LINE_AA)

cv.imshow("hough line demo", new)
cv.imwrite("contours_analysis.png", new)
cv.waitKey(0)
cv.destroyAllWindows()
