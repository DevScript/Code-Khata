import cv2 as cv

src = cv.imread("./test.png")  # reading image that is present in folder
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)  # genrating input visual
h, w, ch = src.shape  # will give height,width and channels

for row in range(h):  # image is just a 2d matrix with colors at every coordinate
    for col in range(w):
        b, g, r = src[row, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        src[row, col] = [b, g, r]
cv.imshow("output1", src)

# how to apply jet and cool filters to an image
dst = cv.applyColorMap(src, cv.COLORMAP_JET)
cv.imshow("output", dst)

color_image = cv.applyColorMap(src, cv.COLORMAP_COOL)
cv.imshow("color_image", color_image)

# Initailly the color format in any image is BGR(Blue green red) but sometimes to wor with some modules one needs to chnage it which can be done like:
# BGR to HSV
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# BGR to YUV
yuv = cv.cvtColor(src, cv.COLOR_BGR2YUV)
cv.imshow("yuv", yuv)
cv.waitKey(0)
cv.destroyAllWindows()
