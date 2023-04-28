import numpy as np
import cv2 as cv

# cap = cv2.VideoCapture()
# cap.open("rtsp://admin:@192.168.10.26:554/out.264")

# while(True):
#      # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Display the resulting frame
#     cv2.imshow('frame',ret)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()


# vcap = cv.VideoCapture("rtsp://192.168.10.26:554/out.h264")
vcap = cv.VideoCapture("rtsp://192.168.10.114:554/out.h264")

while(1):
    ret, frame = vcap.read()
    cv.imshow('VIDEO', frame)
    cv.waitKey(1)