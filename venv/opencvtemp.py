import cv2
import numpy

img=cv2.imread("img5.jpg",1)
cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()