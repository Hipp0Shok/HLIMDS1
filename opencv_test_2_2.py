import cv2

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWrite_fourcc(*'XVID')
out = cv2.VideoWrite('my_cam_vis.avi',fourcc, 20.0, (640, 480))
while True:
    ret, img = cam.read()
    cv2.imshow('my_cma', img)
    out.write(img)
    if cv2.waitKey(10) == 27:
        break
cam.release()
out.release()
cv2.destroyAllWindows()
