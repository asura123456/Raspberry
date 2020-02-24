import cv2
import numpy as np

#img=cv2.imread("img3.jpg",1)
#cv2.namedWindow("Image")
#cv2.imshow("Image", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#cv2.namedWindow("x11test@pycharm")

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
fps=cap.get(5)
cap.set(5,3)
print(fps)

while(True):
    ret,frame=cap.read()
#    frame=cv2.flip(frame,-1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    k=cv2.waitKey(3000)&0xff
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()