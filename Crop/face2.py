import cv2
import sys
import glob 
from PIL import Image
import numpy

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

files=glob.glob("*.jpg")   
for file in files:

    # Read the image
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    print "Found {0} faces!".format(len(faces))
    count=1
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        #img = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        img = cv2.imread(file)
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]
        cropped = img[y:y+h, x:x+w]
        cv2.imwrite("{1}{0}".format(str(file),str(count)), cropped)
        count+=1
        
    cv2.waitKey(0)
