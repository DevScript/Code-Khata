import cv2
import sys
 

cascPath = sys.argv[0]
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeCascase = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#capture frames using webcam
video_capture = cv2.VideoCapture(0)

# Capture frame-by-frame

while True:
    ret, frame = video_capture.read()
    #print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5 )
        
        
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eyeCascase.detectMultiScale(roi_gray)
        
        #to draw box around eyes
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 127, 255), 2)
    
        # Display the resulting frame
    cv2.imshow('Face detection system', frame)
    
    # press 'q' key to break 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
