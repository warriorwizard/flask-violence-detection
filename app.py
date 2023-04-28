from flask import Flask, render_template, Response
import cv2
import numpy as np
import argparse
import pickle
import cv2
import os
import time
from keras.models import load_model
from collections import deque
import matplotlib.pyplot as plt
# %matplotlib inline
import mail_to

app = Flask(__name__)

video= Violence = cv2.VideoCapture("rtsp://192.168.10.121:554/out.h264")
video1 = cv2.VideoCapture("./input/real-life-violence-situations-dataset/Real Life Violence Dataset/NonViolence/NV_3.mp4")
video2 = cv2.VideoCapture("./input/real-life-violence-situations-dataset/Real Life Violence Dataset/Violence/V_3.mp4")

def generate_frames(video):
    # Load the model
    model = load_model('model_test\model_resnet26marchfinal.h5')
    # Initialize deque object
    Q = deque()

    while True:
        # Read the frame
        success, frame = video.read()

        if not success:
            break

        try:
            # Resize the frame
            frame = cv2.resize(frame, (128, 128)).astype("float16")
            IMG_SIZE = 128
            frame = frame.reshape(IMG_SIZE, IMG_SIZE, 3) / 255

            # Make a prediction on the frame
            preds = model.predict(np.expand_dims(frame, axis=0))[0]
            Q.append(preds)

            # Calculate the results
            results = np.array(Q).mean(axis=0)
            i = (preds > 0.6)[0]
            label = i

            # Create the output image with the label
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = cv2.resize(output, (512, 360)).copy()
            text = "Violence: {}".format(label)
            color = (0, 255, 0)

            if label:
                color = (255, 0, 0)
            else:
                color = (0, 255, 0)

            cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

            # Encode the frame to JPEG format
            ret, buffer = cv2.imencode('.jpg', output)
            frame = buffer.tobytes()

            # Yield the frame
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        except:
            break

    # Release the video object
    video.release()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed1')
def video_feed1():
    return Response(generate_frames(video), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed2')
def video_feed2():
    return Response(generate_frames(video), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
