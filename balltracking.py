from collections import deque
from imutils.video import VideoStream 
import numpy as np 
import argparse
import cv2
import imutils
import time
ap = argparse.ArgumentParser()
ap.add_argument("-v","--video", help="path to the (optional) video file")
ap.add_argument("-b","--buffer", type=int, default=64, help="max buffer size")
args =  vars(ap.parse_args())
#define the lower and upper boundaries of the "green"
#ball in the HSV color space, then initialize the 
#list of tracked points
greenLower = (29,86,6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=args["buffer"])
#if a video path was not supplied, grab the reference
#to the webcam 
if not args.get("video, False"): 
    vs = VideoStream(src=0).start()
#otherwise, grab a reference to the video file
else:
    vs = cv2.VideoCapture(args["video"])
#allow the camera or video file to warm up
time.sleep(10.0)

