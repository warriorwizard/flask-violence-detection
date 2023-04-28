import numpy as np
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


def print_results(video, limit=None):
    # fig=plt.figure(figsize=(16, 30))
    # if not os.path.exists('output'):
    #     os.mkdir('output')

    print("Loading model ...")
    # model = load_model('./results/model.h5')
    model = load_model('model_test\model_resnet26marchfinal.h5')
    # Q = deque(maxlen=128)
    Q = deque()

    # vs = cv2.VideoCapture(video)
    writer = None
    (W, H) = (None, None)
    count = 0     
    cout=0
    while True:
        (grabbed, Frame) = video.read()
        # cv2.imshow('frame',frame)
        ID = video.get(1)
        if not grabbed:
            break
        try:
            if (ID % 7 == 0):
                count = count + 1
                n_frames = len(Frame)
                
                if W is None or H is None:
                    (H, W) = Frame.shape[:2]

                frame = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)
                output = cv2.resize(frame, (512, 360)).copy()
                frame = cv2.resize(frame, (128, 128)).astype("float16")
                IMG_SIZE = 128
                frame = frame.reshape(IMG_SIZE, IMG_SIZE, 3) / 255
                preds = model.predict(np.expand_dims(frame, axis=0))[0]
                Q.append(preds)

                results = np.array(Q).mean(axis=0)
                i = (preds > 0.6)[0] #np.argmax(results)


                label = i
                # print(i)

                text = "Violence: {}".format(label)
                # print('prediction:', text)
                # file = open("output.txt",'w')
                # file.write(text)
                # file.close()

                color = (0, 255, 0)

                if label:
                    color = (255, 0, 0) 
                else:
                    color = (0, 255, 0)

                cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)
                output=cv2.imshow("Output", output)

                #----------------------mail part-----------
                # print(cout)
                if label==True:
                    cv2.imwrite('temp.jpg',Frame)   
                    cout+=2
                else:
                    if cout<=0:
                        pass
                    else:
                        cout-=1
                # cout=cout%7
                if cout==6:
                    mail_to.mailto('./temp.jpg')
                    # mail_to.mailto(Frame)
                    # time.sleep(3)
                    cout=0
                

                # saving mp4 with labels but cv2.imshow is not working with this notebook
                # if writer is None:
                #         fourcc = cv2.VideoWriter_fourcc(*"MJPG")
                #         # writer = cv2.VideoWriter("output.mp4", fourcc, 60,(W, H), True)

                # writer.write(output)
                # cv2.imshow("Output", output)

                # fig.add_subplot(8, 3, count)
                # plt.imshow(output)

    #         if limit and count > limit:
    #             break

        except:
            break 
        cv2.waitKey(1)
    
    # # plt.show()
    # print("Cleaning up...")
    # if writer is not None:
    #     writer.release()
    # vs.release()



# Violence=r"./input/real-life-violence-situations-dataset/Real Life Violence Dataset/NonViolence/NV_3.mp4"
# Violence=cv2.VideoCapture("./input/real-life-violence-situations-dataset/Real Life Violence Dataset/NonViolence/NV_3.mp4")
# Violence1=cv2.VideoCapture("./input/real-life-violence-situations-dataset/Real Life Violence Dataset/Violence/V_3.mp4")
# Violence2=cv2.VideoCapture(".\input\\real-life-violence-situations-dataset\\real life violence situations\\Real Life Violence Dataset\\Violence\\V_6.mp4")
# Violence=cv2.VideoCapture("./college_2.mp4")
# Violence=cv2.VideoCapture("./vedio_7.mp4")
# Violence=cv2.VideoCapture("D:\Deep Surveillance using ResNet50V2\input\\real-life-violence-situations-dataset\Real Life Violence Dataset\Violence/vedio_6.mp4")
# Violence = cv2.VideoCapture("rtsp://192.168.10.114:554/out.h264")
Violence = cv2.VideoCapture("rtsp://192.168.10.121:554/out.h264")

# print_results(Violence)
# time.sleep(10)
print_results(Violence1)
# print_results(Violence2)




