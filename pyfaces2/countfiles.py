
import os


path, dirs, files = os.walk("/Users/azz/Desktop/nourin/Minor/images/gallery").next()
file_count = len(files)

if file_count > 0:
    import pyfacescontroller
    for x in xrange(file_count-1):
        execfile("pyfacescontroller.py")

