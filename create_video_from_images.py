import cv2
import urllib
import numpy as np

def construct_video(frames_start, frames_end):
    # image_url = "Demo1-3/frame%d.jpg"
    image_url = "images/%d.png"
    img = []
    for i in range(frames_start, frames_end):
        img.append(cv2.imread(image_url % (i)))

    height, width, layers = img[1].shape
    fourcc = cv2.VideoWriter_fourcc(*'MP42')
    video = cv2.VideoWriter('video.mp4', fourcc, 25.0, (320, 240))

    for j in range(0, frames_end - frames_start):
        video.write(img[j])

    cv2.destroyAllWindows()
    video.release()

    my_file = open("video.mp4", "rb")
    my_bytes = my_file.read()
    my_url = "https://firebasestorage.googleapis.com/v0/b/fallsafe.appspot.com/o/video%2Fvideo.mp4"
    my_headers = {"Content-Type": "video/mp4"}
    my_request = urllib.request.Request(
        my_url, data=my_bytes, headers=my_headers, method="POST")
    try:
        loader = urllib.request.urlopen(my_request)
    except urllib.error.URLError as e:
        message = json.loads(e.read())
        print(message["error"]["message"])
    else:
        print(loader.read())

