import cv2
import os.path
import sys
import numpy as np
import timeit
import json
import requests



location = '1.1.1.1'
port = 80
apiString = 'http://' + location + ':' + str(port) + '/cgi-bin/face_rec_server.py'


#
# Function: read_images
# Description: Reads the sample images that were created in the directory "data", reads the
#              CSV file and places the images in an array with corresponding labels 
#              in another array to recognize the person
# Input: path to the "data" directory containing sample images and size of the images set to none
# Output: Returns the array with all the sample images of the person and another array with the
#         corresponding labels to recognize the person
#
def read_images(path, sz=None):

   c = 0
   X,y = [], []
   for dirname, dirnames, filenames in os.walk(path):
      for subdirname in dirnames:	# iterate through directories containing sample images
         subject_path = os.path.join(dirname,subdirname)
         for filename in os.listdir(subject_path):
            try:
               if (filename == ".directory"):
                  continue
               
               filepath = os.path.join(subject_path, filename)
               im = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
               
               # resize image if size is given
               if (sz is not None):
                  im = cv2.resize(im, (200,200))
               
               X.append(np.asarray(im, dtype=np.uint8))
               y.append(c)
               
            except IOError, (errno, strerror):
               print "I/O error({0}): {1}".format(errno, strerror)
            except:
               print "Unexpected error:", sys.exc_info()[0]
               raise
         
         c = c + 1
   
   return [X,y]


if __name__ == "__main__":
   names = ['Jerry']
   if len(sys.argv) < 2:
      print "USAGE: face_rec_offload.py <path/to/images/directory>"
      sys.exit()
   
   [X,y] = read_images(sys.argv[1])
   y = np.asarray(y, dtype=np.int32)
   
   if len(sys.argv) == 3:
      out_dir = sys.argv[2]
   
   model = cv2.face.EigenFaceRecognizer_create()    # create the model for EigenFaceRecognizer algorithm used for face recognition
   
   #
   # Function: train
   # Description: Face recognition algorithm will be trained with the array of images
   #              and the array of labels to recognize the person
   # Input: Array of images and array of labels to identify the person 
   # Output: Train the EigenFaceRecognizer algorithm for face detection using 
   #         array of images and array of labels to recognize the person
   #
   model.train(np.asarray(X), np.asarray(y))        
   
   #
   # Function: VideoCapture
   # Description: Open video capture for the camera
   # Input: Device index that identifies the camera
   #        On the PandaBoard, use 0
   # Output: Open video capture to expose frames for reading
   #
   camera = cv2.VideoCapture(0)
   

   while (True):
      # read frame-by-frame 
      read, img = camera.read()
      client_list = [json.dumps(img.tolist())]
      
      post = [json.dumps(img.tolist()), json.dumps(img.tolist())] #manage memory
      
      #
      # Function: post
      # Description: Send a "post" request to the server by specifying URL string
      # and data from frame array encoded as JSON
      # Input: URL string to send request to server, frame array endoded as JSON, 
      #        amount of time set before the next frame is sent to the server
      # Output: Return the string of the rectangle position where a face was detected
      #
      post = requests.post(apiString, data=json.dumps(client_list), timeout=None)
      
      faces = post.content                  # return string of rectangle position where face was detected from the server
                                 
      faces = faces.replace("\n", "")       # remove new line character from the string
      faces = faces.replace("''", "")       # remove quotation marks from the string
      faces = faces[2:-2]                   # extract a portion of the string
      faces = faces.split(' ')              # convert string to character array, where each character is delimited by spaces
      
      
      x = int(faces[0])                     # extract the x-coordinate of the rectangle
      y = int(faces[1])                     # extract the y-coordinate of the rectangle
      w = int(faces[2])                     # extract the width of the rectangle
      h = int(faces[3])                     # extract the height of the rectangle

      
      # 
      # Function: rectangle
      # Description: Draws a rectangle where a face was detected using the position of the rectangle
      # Input: frame in color scale, first point and second point of the line in rectangle, specification to draw rectangle,
      #        color of the rectangle, and thickness of the lines in rectangle
      # Output: The drawn rectangle in the window where the face is detected
      #
      img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
      # 
      # Function: cvtColor
      # Description: Convert frame from color scale to gray scale
      # Input: Frame in color scale and conversion to gray scale
      # Output: Matrix array of frame in gray scale
      # 
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      roi = gray[x:x+w, y:y+h]
      try:
         
         roi = cv2.resize(roi, (200,200), interpolation=cv2.INTER_LINEAR)   # resize the expected frame to 200x200
         
         #
         # Function: predict
         # Description: Face recognition is applied
         # Input: resized frame
         # Output: Returns the label of the person recognized and a confidence score
         #
         params = model.predict(roi)
         
         print "Label: %s, Confidence: %.2f" % (params[0], params[1])
         cv2.putText(img, names[params[0]], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)   # insert name of the person recognized in the window
      except:
         continue

      cv2.imshow("Camera", img)
      if cv2.waitKey(1000 / 12) & 0xff == ord("q"):
         break
   # release video capture
   camera.release()
   # close window(s)
   cv2.destroyAllWindows()
      









