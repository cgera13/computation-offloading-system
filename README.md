# computation-offloading-system
Offloading matrix operations, face detection, and face recognition applications from a PandaBoard device (i.e. client device) to a server (i.e. server desktop computer)

This is a computation offloading system that sends matrices from a PandaBoard platform to be computed on a server. The results of the matrix operations are returned to the PandaBoard via a RESTful API. The project involves the offloading of face detection and face recognition applications in Python with the use of the Open Source Computer Vision (OpenCV) library. In addition, the function that detects the face is executed on the server because it requires the most time to execute. The face detection portion is executed on the server for both applications since they require the most computation. The face detection results of both applications are then returned to the PandaBoard. The project also includes a website developed to run on a local computer that will perform matrix operations by requiring user-defined matrices.

The project is useful because it allows less resourceful devices to take advantage of computing resources on a more capable computer. This is a computation offloading system that can be used for applications that require extensive computation.


The website will need a local webserver in order to run locally on a computer. I used EasyPHPDevserver as the local webserver. I also used the jQuery JavaScript library to program the JavaScript portion of the website.

I developed the computation offloading system using Linux on both the PandaBoard and server. I used the Apache webserver on the server computer. In addition, I installed Python 2.7 and compiled/built the OpenCV library on both the PandaBoard and server. The RESTful API was made available by downloading the HTTPRequests library for Python on the PandaBoard. I used the Conda package manager to install the following: Python 2.7, NumPy, OpenCV, and HTTPRequests library. The NumPy library was used for access to the methods for operating on the matrices as well as for handling matrix arrays in the face detection and face recognition applications. Another requirement was to enable Common Gateway Interface scripting on the server to execute the Python scripts.

