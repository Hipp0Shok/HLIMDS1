import cv2
import sys

if len(sys.argv) < 2:
    print("set the name and path to the file")
    sys.exit(1)
    
img = cv2.imread(sys.argv[1])
cv2.imshow('my_image', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()


