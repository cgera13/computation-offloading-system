import cv2
import numpy as np
import json
import sys
import timeit
import requests

location = '1.1.1.1'
port = 80
apiString = 'http://' + location + ':' + str(port) + '/cgi-bin/face_detect_server.py'


# load OpenCV cascade classifier file for detecting eyes
eyeCascade = cv2.CascadeClassifier('../../Downloads/opencv/data/haarcascades/haarcascade_eye.xml')


#
# Function: VideoCapture
# Description: Open video capture for the camera
# Input: Device index that identifies the camera
#        On the PandaBoard, use 0
# Output: Open video capture to expose frames for reading
#
video_capture = cv2.VideoCapture(0)



while True:
   # if video capture is open
   if video_capture.isOpened():
      # read frame-by-frame
      ret, frame = video_capture.read()
      
      
      # 
      # Function: cvtColor
      # Description: Convert frame from color scale to gray scale
      # Input: Frame in color scale and conversion to gray scale
      # Output: Matrix array of frame in gray scale
      #  
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      client_list = [json.dumps(gray.tolist())]
      
      post = [json.dumps(gray.tolist()), json.dumps(gray.tolist())] #manage memory (i.e. allocate memory)
      
      
      #
      # Function: post
      # Description: Send a "post" request to the server by specifying URL string
      # and data from frame array encoded as JSON
      # Input: URL string to send request to server, frame array endoded as JSON, 
      #        amount of time set before the next frame is sent to the server
      # Output: Return the string of the rectangle position where a face was detected
      #
      post = requests.post(apiString, data=json.dumps(client_list), timeout=None)
      
      
      faces = post.content              # return string of rectangle position where face was detected from the server
       
      faces = faces.replace("\n", "")   # remove new line character from the string
      #faces = faces.replace("''", "")
      faces = faces[2:-2]               # extract a portion of the string
      faces = faces.split(' ')          # convert string to character array, where each character is delimited by spaces
      print(faces)                      # print the rectangle position, which is a character array by now
      x = int(faces[0])                 # extract the x-coordinate of the rectangle
      y = int(faces[1])                 # extract the y-coordinate of the rectangle
      w = int(faces[2])                 # extract the width of the rectangle
      h = int(faces[3])                 # extract the height of the rectangle
      

      # 
      # Function: rectangle
      # Description: Draws a rectangle where a face was detected using the position of the rectangle
      # Input: frame, first point and second point of the line in rectangle, specification to draw rectangle,
      #        color of the rectangle, and thickness of the lines in rectangle
      # Output: The drawn rectangle in the window where the face is detected
      #
      cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
      roi_gray = gray[y:y+h, x:x+w]         # region of the gray scale frame to be used for eye detection
      roi_color = frame[y:y+h, x:x+w]       # region of the frame in color to be used to draw the rectangle
                                            # where the eyes are detected
      
      #
      # Function: detectMultiScale
      # Description: Detects the eyes in the region where
      #              the face was detected
      # Input: Region in gray scale where the eyes were detected
      # Output: Returns the position of the rectangles where
      #         the eyes were detected
      #
      eyes = eyeCascade.detectMultiScale(roi_gray)
      for (ex, ey, ew, eh) in eyes:
         # 
         # Function: rectangle
         # Description: Draws a rectangle where pair of eyes were detected using the position of the rectangles
         # Input: frame, first point and second point of the line in rectangle, specification to draw rectangle,
         #        color of the rectangle, and thickness of the lines in rectangle
         # Output: The drawn rectangles in the window where the pair of eyes are detected
         # 
         cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)
      
      #display the resulting frame in window
      cv2.imshow("Video", frame)
      
      
      if cv2.waitKey(1) & 0xFF == ord('q'):
         break
      
   else:
      print("\ncan't open camera")
      break
# When everything is done, release the video capture
video_capture.release()
# close the window(s)
cv2.destroyAllWindows()





