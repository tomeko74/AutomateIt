#Program for face detection
import cv2

face_cascade = cv2.CascadeClassifier('.\data\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('.\data\haarcascade_eye.xml')

img = cv2.imread('twarze3.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

face_cascade = cv2.CascadeClassifier('.\data\haarcascade_frontalface_default.xml')
original_image_path = 'twarze3.jpg'

image = cv2.imread(original_image_path)
faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite('twarze3_face.jpg', image)

"""
"""
image = cv2.imread("Aga1.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Over the Clouds", image)
cv2.imshow("Over the Clouds - gray", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""