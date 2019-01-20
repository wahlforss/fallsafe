# https: // pypi.org/project/opencv-python/
from prediction_call import prediction_call
from alert_user import alert_the_user
from send_push_notifications import notify
from create_video_from_images import construct_video
import asyncio
import os.path
import threading
start_frame = 0
end_frame = 0
flag = 0

# FOR PHOTOGRAPHING
import time
import cv2


def read_from_camera(camera):
    read_frame = 0
    while True:
        read_frame += 1
        return_value, image = camera.read()
        #print(read_frame)
        cv2.imwrite("images/%d.png" % (read_frame), image)


def predict_output():
    predict_frame = 1
    start_frame = 0
    end_frame = 0
    count_fallings = 0
    flag = 0
    print('starting prediction')
    while True:
        # image_url = "Demo1-3/frame%d.jpg"
        image_url = "images/%d.png"
        if not os.path.isfile(image_url % (predict_frame)):  
            print('stuck', os.path.isfile(image_url % (predict_frame)))
            continue
        prediction = prediction_call(image_url % (predict_frame))
        print(predict_frame)
        print(prediction)

        #reset the counter
        if prediction == 'standing':
            #keep updating the start and end frame to current frame if the person is still standing
            start_frame = 0
            end_frame = 0
            flag = 0
        elif prediction == 'falling' and start_frame == 0:
            # the first time any falling is observed
            start_frame = predict_frame
            flag=1
            count_fallings += 1
        elif prediction == 'falling' and start_frame != 0 and flag != 2:
            # to keep increasing end_frame till we observe falling
            end_frame = predict_frame
            count_fallings += 1
        # if end_frame - start_frame > 25 and flag ==1:
        #     # to only consider genuine and quick falls
        #     flag = 0

        if prediction == 'fallen':
            count_fallings += 1
            end_frame = predict_frame
            # register the final fall
            flag = 2

        if flag != 0 and count_fallings > 1:
            print(start_frame, 'start')
            print(max(end_frame, start_frame+25), 'end')
            construct_video(max(start_frame - 100, 0), max(end_frame,start_frame+100))
            notify()
            exit()
        
        predict_frame += 12
        print(flag)
        print

def start_surv():
    camera_port = 0
    width = 320
    height = 240
    fps = 25.0
    time_stored = 30
    max_frames_stored = fps * time_stored
    camera = cv2.VideoCapture(camera_port)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    camera.set(cv2.CAP_PROP_FPS, fps)
    time.sleep(0.1)  # If you don't wait, the image will be dark
    #while True:
    #for i in range(300):
        #frame += 1 


        # creating thread

    t1 = threading.Thread(target=predict_output,)
    t2 = threading.Thread(target=read_from_camera, args=(camera,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    del(camera)  # so that others can use the camera as soon as possible
