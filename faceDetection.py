import numpy as np
import cv2

#faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
fps=cap.get(5)/10000
print(fps)

while(True):
    ret, img = cap.read()
#    img = cv2.flip(img, -1)
#    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_engine = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    faces = face_engine.detectMultiScale(img,scaleFactor=1.3,minNeighbors=5)
    for (x,y,w,h) in faces:
        gray = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('gray',gray)

    k=cv2.waitKey(5)&0xff
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()