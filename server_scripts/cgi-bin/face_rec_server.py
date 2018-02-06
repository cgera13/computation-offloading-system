#!/home/server/miniconda2/bin/python

import cv2
import numpy as np
import json
import timeit
import sys
import os
import cgitb
cgitb.enable()

print("Content-type: text/html; charset=utf-8")
print("\n")


if os.environ.get("REQUEST_METHOD") == "POST":
   
   # load OpenCV cascade classifier file for detecting faces
   faceCascade = cv2.CascadeClassifier('../../../home/server/Downloads/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
   
   
   
   posted_content = sys.stdin.read().decode()   # receive frame from PandaBoard as string
   
   
   img = json.loads(posted_content)             # load frame as JSON string
   
   img = json.loads(img[0])                     # load frame as JSON string again
   
   img = np.array(img, dtype=np.uint8)          # convert frame into numpy array with data type set to 
                                                # unsigned 8 bit integer (i.e. values from 0-255)
   
   
   
   #
   # Function: detectMultiScale
   # Description: Perform face detection and returns the position of the rectangle
   #              where the face is detected  
   # Input: frame in color scale, scaleFactor is used to compensate for faces appearing bigger
   #        because they are closer to the camera, minNeighbors defines how many objects
   #        are detected near the current one before it declares that a face is found
   # Output: Returns the position of the rectangle where the face is detected
   # 
   faces = faceCascade.detectMultiScale(img, 1.3, 5)
   
   
   print(faces)     # print the position of the rectangle so that it can returned to the PandaBoard
   
   
   

   
   
