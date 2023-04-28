Violence=r"./input/real-life-violence-situations-dataset/Real Life Violence Dataset/NonViolence/NV_3.mp4"

import cv2 as cv
import numpy as np


# capture=cv.VideoCapture(0)

capture = cv.VideoCapture("rtsp://192.168.10.114:554/out.h264")
#scaling the window 
#this method works for video,image and live video
# def rescaleFrame(frame,scale=0.75):
#     width=int(frame.shape[1]*scale)
#     height=int(frame.shape[0]*scale)
#     dimensions=(width,height)

#     return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#changing the resolution of a video
#only works on live video

# def changeRes(widht,height):
#     capture.set(3,width)
#     capture.set(4,height)

#draw and write on images

haar_cascade=cv.CascadeClassifier('./haarcascade_fullbody.xml')

while True:
    isTrue,frame=capture.read()
    # frame_resized=rescaleFrame(frame)

    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray = cv.resize(gray, (128, 128))
    # cv.imshow('gray',gray)

    faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)

    cv.imshow('detectec faces',frame)


    # cv.imshow('video',frame)
    # cv.imshow('video Resized',frame_resized)
    if cv.waitKey(20) & 0xff==ord('d'):
        break


capture.relese()    
cv.destroyAllWindows()

cv.waitKey(0)