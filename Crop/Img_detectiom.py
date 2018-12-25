import numpy as np
import cv2
import sys
import glob 
from PIL import Image
import numpy
face_cascade = cv2.CascadeClassifier('\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')

img = cv2.imread('img.jpg')
gray = cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(128,128,128),2)
    #roi_gray = gray[y:y+h, x:x+w]
    #roi_color = img[y:y+h, x:x+w]
    #eyes = eye_cascade.detectMultiScale(roi_gray)
    #for (ex,ey,ew,eh) in eyes:
        #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(128,128,128),2)
'''# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)
print "Found {0} faces!".format(len(faces))
# Crop Padding
left = 10
right = 10
top = 10
bottom = 10

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    print x, y, w, h

    # Dubugging boxes
    # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)'''


#image  = image[y-top:y+h+bottom, x-left:x+w+right]
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
