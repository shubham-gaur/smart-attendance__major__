from cv2 import *
camera_port = 0
ramp_frames = 0
 
# Initialize the camera capture object with the cv2.VideoCapture class.
camera = VideoCapture(camera_port)
 
print("Taking image...")
def get_image():
 retval, im = camera.read()
 if retval:    
    imshow("cam-test",im)
    waitKey(0)
    destroyWindow("cam-test")
    return im
 
for i in xrange(ramp_frames):
 temp = get_image()
camera_capture = get_image()
file = "/Users/Shubham/Documents/Python Scripts"

imwrite("filename.jpg",camera_capture)

del(camera)
