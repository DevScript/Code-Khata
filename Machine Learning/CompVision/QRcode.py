import cv2
import numpy as np

src = cv2.imread("qr.png")
cv2.imshow("image", src)
# gray image
# to work with detector first convert to gray
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
qrcoder = cv2.QRCodeDetector()
codeinfo, points, straight_qrcode = qrcoder.detectAndDecode(
    gray)  # this method is used to decode and read qr code
print(points)  # the vertice points of the qr_code
result = np.copy(src)
cv2.drawContours(result, [np.int32(points)], 0, (0, 0, 255), 2)
# the data stored will be printed
print("qrcode information is :\n%s" % codeinfo)
cv2.imshow("result", result)
cv2.imwrite("result.png", result)
code_roi = np.uint8(straight_qrcode)
cv2.imshow("qrcode roi", code_roi)
cv2.imwrite("qrcode_roi.png", code_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
