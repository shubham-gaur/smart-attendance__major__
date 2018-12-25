import cv2
import sys
from PIL import Image
import glob 
import numpy



faceCascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30),
        flags = 0
    )

    # Draw a rectangle around the faces
    for ( x, y, w, h) in faces:
        # image ,top left coordinate , bottom right , color thickness
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)
    if True:
        ok = frame
        file = r"S:\Projects\Python\Major\FaceDetection\Monitor\0832CS.jpg"
        cv2.imwrite(file, ok)
        img = cv2.imread(file,0)
        cv2.imwrite('0832CS.jpg',img)
        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

        files=glob.glob("*.jpg")   
        for file in files:

            # Read the image
            image = cv2.imread(file)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
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
            if cv2.waitKey(1) & 0xFF == 'q':
                break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()




