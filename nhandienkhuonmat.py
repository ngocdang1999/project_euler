import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier("./cascade_files/haarcascade_frontalface_alt.xml")
cap = cv2.VideoCapture(0)
while True :
ret,fram = cap.read()
img = cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
fram = cv2.resize( img,None,fx =0.5,fy =0.5,interpolation = cv2.INTER_AREA)
face = face_cascade.detectMultiScale(fram,1.3,5)
for (x,y,w,h) in face :
cv2.rectangle(fram,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("image",fram)
c = cv2.waitKey(1)
if c ==27 :
break
cap.release()
cv2.destroyAllWindows()