import timeit
import time
import json
import requests
import numpy as np
import os
import sys

location = '1.1.1.1'
port = 80
apiString = 'http://' + location + ':' + str(port) + '/cgi-bin/m_ops.py'

op = 'multiplication'

m1Row = m1Col = m2Row = m2Col = 2000



#
# Function: randint 
# Description: Generate array of random integers with range between 1 and 101
# Input: Range of random numbers to choose from and the shape of the array
# Output: Return an array of random integers with range between 1 and 101
#
matrix_1 = np.random.randint(1, 101, size=(m1Row,m1Col))
matrix_2 = np.random.randint(1, 101, size=(m2Row,m2Col))

params = {'op': str(op), 'm1Row': str(m1Row), 'm1Col': str(m1Col), 'm2Row': str(m2Row), 'm2Col': str(m2Col)}

client_list = [params, json.dumps(matrix_1.tolist()), json.dumps(matrix_2.tolist())]


start_time = timeit.default_timer()

#
# Function: post
# Description: Send a "post" request to the server by specifying URL string
# and data from matrices encoded as JSON
# Input: URL string to send the request to the server and data from matrices encoded as JSON
# Output: Return the result of the matrix operation as an array
#
post = requests.post(apiString, data=json.dumps(client_list))



print "\n headers for post request:\n", post.headers
print "\n server status:", post.status_code

# print the response from the server
print post.content













    
    








 
