import cv2 as cv

capture = cv.VideoCapture(0)
detector = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_alt.xml")

image = cv.imread('people.jpg')
faces = detector.detectMultiScale(image, scaleFactor=1.05, minNeighbors=1,
                                  minSize=(50, 50), maxSize=(500, 500))
for x, y, width, height in faces:
    cv.rectangle(image, (x, y), (x+width, y+height),
                 (0, 255, 255), 2, cv.LINE_8, 0)
cv.imshow("faces", image)
cv.waitKey(0)
cv.imwrite('face.jpg', image)
