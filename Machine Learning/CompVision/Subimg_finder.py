import cv2 as cv
import numpy as np


def template_demo():
    main = cv.imread("./test.png")
    sub = cv.imread("./test01.png")
    cv.imshow("input", main)
    cv.imshow("sub", sub)
    th, tw = sub.shape[:2]
    # to match the common area between images
    result = cv.matchTemplate(main, sub, cv.TM_CCORR_NORMED)
    cv.imwrite("D:/039_003.png", np.uint8(result*255))
    t = 0.98  # precison assumed constant can be chnage ddepending on need
    loc = np.where(result > t)

    for pt in zip(*loc[::-1]):
        cv.rectangle(main, pt, (pt[0] + tw, pt[1] + th), (0, 55, 0), 1, 8, 0)
    cv.imshow("llk-demo", main)
    cv.imwrite("D:/039_004.png", main)


template_demo()
cv.waitKey(0)
cv.destroyAllWindows()
