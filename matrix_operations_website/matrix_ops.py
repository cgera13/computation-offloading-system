import numpy as np
from numpy.linalg import inv
import codecs, json
import requests
import sys
import cgitb    
cgitb.enable()  # Display detailed reports in Web browser if any errors or bugs occur in the script.
                # This can show the guts of the program for users of this script.
                # Therefore, it is recommended to remove this line as others can see the script in detail.
                # The reports can be hidden in files with the following code:
                # cgitb.enable(display=0, logdir="/path/to/logdir")
                 
################################################################################
#
# Function: mat_mult
# Description: Calculate the product of two arrays, not the element-wise multiplication
# Input: Number of columns for first array, number of rows for second array,
# first array, and second array
# Output: Print the product of two arrays
#
def mat_mult(colM1, rowM2, m1, m2):
    if (colM1 != rowM2):        # check if matrix 1 columns and matrix 2 rows match
        print "Matrices with entered dimensions cannot be multiplied"
    else:                       # if they match, perform multiplication
        M1 = np.array(m1)       # define array for matrix 1
        M2 = np.array(m2)       # define array for matrix 2
        product = np.dot(M1, M2)    # dot() function performs matrix multiplication, not element-wise multiplication
        for row in product:
            print row, "<br>"
        #with open ('results.json', 'w') as outfile:
        #    json.dump(product.tolist(), outfile, indent = 4)

################################################################################
#
# Function: mat_add
# Description: Addition of two arrays, element-wise
# Input: First array and second array
# Output: Print the addtion of two arrays, element-wise
#
def mat_add(m1, m2):
    mat1 = np.array(m1)         # define array for matrix 1
    mat2 = np.array(m2)         # define array for matrix 2         
    if (np.shape(mat1) != np.shape(mat2)):  # if dimensions don't match
        print "Matrices with entered dimensions cannot be added"
    else:                                   # if they match perform addition
        M1 = mat1               
        M2 = mat2
        sum = np.add(M1, M2)
        for r in sum:
            print r, "<br>"
        #with open ('results.json', 'w') as outfile:
        #    json.dump(sum.tolist(), outfile, indent = 4)
            
        
################################################################################        
#
# Function: mat_sub
# Description: Subtract two arrays, element-wise 
# Input: First array and second array
# Output: The difference of first array and second array, element-wise 
#               
def mat_sub(m1, m2):
    mat1 = np.array(m1)
    mat2 = np.array(m2)
    if (np.shape(mat1) != np.shape(mat2)):      # check if matrix 1 and matrix 2 dimensions don't match
        print "Matrices with entered dimensions cannot be subtracted"
    else:                                       # if matrix 1 and matrix 2 dimensions match, perform subtraction
        M1 = mat1
        M2 = mat2
        sub = np.subtract(M1, M2)               
        for r in sub:                           
            print r, "<br>"                   # print each row on a new line
        #with open ('results.json', 'w') as outfile:
        #    json.dump(sub.tolist(), outfile, indent = 4)
            
################################################################################
#
# Function: mat_inverse
# Description: Calculate the multiplicative inverse of first array and second array
# Input: number of rows for first array, number of columns for first array,
# number of rows for second array, number of columns for second array,
# first array, and second array
# Output: Print multiplicative inverse of first array and second array
#
def mat_inverse(rowM1, colM1, rowM2, colM2, m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    if ((rowM1 != colM1) & (rowM2 != colM2)):   # check if matrix 1 and matrix 2 are not square matrices
        print "Matrices with entered dimensions cannot be inverted"
    else:                                       # perform inverse if both matrices are square matrices
        inv1 = inv(M1)                          # apply the inverse of matrix 1
        inv2 = inv(M2)                          # apply the inverse of matrix 2
        print "Matrix 1 inverse:<br>"
        for m in inv1:
            print m, "<br>"                     # print each row on a new line
        print "<br> Matrix 2 inverse:<br>"
        for n in inv2:
            print n, "<br>"                     # print each row on a new line
        #with open ('results.json', 'w') as outfile:
        #    add_to = inv1.tolist()
        #    add_to.append(inv2.tolist())
        #    json.dump(add_to, outfile, indent = 4)

################################################################################
#
# Function: mat_trans
# Description: Permute the dimensions of first array and second array
# Input: First array and second array
# Output: Permute the dimensions of the first array and second array
#
def mat_trans(m1, m2):
    M1 = np.array(m1)                           
    M2 = np.array(m2)
    trans1 = M1.transpose()                     # apply transpose of matrix 1
    trans2 = M2.transpose()                     # apply transpose of matrix 2
    print "Matrix 1 transpose:<br>"
    for m in trans1:
        print m, "<br>"                         # print each row of matrix 1 on a new line
    print "<br> Matrix 2 transpose:<br>"
    for n in trans2:
        print n, "<br>"                         # print each row of matrix 2 on a new line
    #with open ('results.json', 'w') as outfile:
    #    add_to = trans1.tolist()
    #    add_to.append(trans2.tolist())
    #    json.dump(add_to, outfile, indent = 4)

################################################################################
#
# Function: dft_1d
# Description: Calculate the 1-Dimensional discrete fourier transform for first array
# and second array
# Input: First array and second array, number of columns for first array, number of columns
# for second array
# Output: Print the 1-Dimensional discrete fourier transform for first array
# and second array
#
def dft_1d(m1, m2, colM1, colM2):
    dft1 = np.fft.fft(np.exp(2j * np.pi * np.array(m1) / colM1))
    dft2 = np.fft.fft(np.exp(2j * np.pi * np.array(m2) / colM2))
    print "Matrix 1 1-Dimensional Discrete Fourier Transform:<br>"
    for m in dft1:
        print m, "<br>"
    print "Matrix 2 1-Dimensional Discrete Fourier Transform:<br>" 
    for n in dft2:
        print n
    #with open ('results.json', 'w') as outfile:
    #    add_to = dft1.tolist()
    #    add_to.append(dft2.tolist())
    #    json.dump(add_to, outfile, indent = 4)
        
################################################################################        
#
# Function: idft_1d
# Description: Calculate the 1-Dimensional inverse discrete fourier transform for first array
# and second array
# Input: First array and second array
# Output: Print the 1-Dimensional inverse discrete fourier transform for the first array
# and second array
#
def idft_1d(m1, m2):
    idft1 = np.fft.ifft(np.array(m1))
    idft2 = np.fft.ifft(np.array(m2))
    print "Matrix 1 1-Dimensional Inverse Discrete Fourier Transform:<br>"
    for m in idft1:
        print m, "<br>"
    print "Matrix 2 1-Dimensional Inverse  Discrete Fourier Transform:<br>"
    for n in idft2:
        print n
    #with open ('results.json', 'w') as outfile:
    #    add_to = idft1.tolist()
    #    add_to.append(idft2.tolist())
    #    json.dump(add_to, outfile, indent = 4)  

################################################################################
#
# Function: dft_2d
# Description: Calculate the 2-Dimensional discrete fourier transform for the first array
# and second array
# Input: First array and second array
# Output: Print the 2-Dimensional discrete fourier transform for the first array
# and second array
#
def dft_2d(m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    # M1 = np.mgrid[a]        # mgrid provides support for matrix indexing
    dft1 = np.fft.fft2(M1)
    dft2 = np.fft.fft2(M2)
    print "Matrix 1 2-Dimensional Discrete Fourier Transform:<br>"
    for m in dft1:
        print m, "<br>"
    print "Matrix 2 2-Dimensional Discrete Fourier Transform:<br>"
    for n in dft2:
        print n, "<br>"
    #with open ('results.json', 'w') as outfile:
    #    add_to = dft1.tolist()
    #    add_to.append(dft2.tolist())
    #    json.dump(add_to, outfile, indent = 4)
    

################################################################################
#
# Function: idft_2d
# Description: Calculate the 2-Dimensional inverse discrete fourier transform for the first array
# and second array
# Input: First array and second array
# Output: Print the 2-Dimensional inverse discrete fourier transform for the first array
# and second array
#
def idft_2d(m1, m2):            
    M1 = np.array(m1)
    M2 = np.array(m2)
    idft1 = np.fft.ifft2(M1)
    idft2 = np.fft.ifft2(M2)
    print "Matrix 1 Inverse Discrete Fourier Transform:<br>"
    for m in idft1:
        print m, "<br>"
    print "Matrix 2 Inverse Discrete Fourier Transform:<br>"
    for n in idft2:
        print n, "<br>"
    #with open ('results.json', 'w') as outfile:
    #    add_to = idft1.tolist()
    #    add_to.append(idft2.tolist())
    #    json.dump(add_to, outfile, indent = 4)

################################################################################
#    Start of the main program
################################################################################
m1row = int(sys.argv[4]) # matrix 1 row dimension
m1col = int(sys.argv[1]) # matrix 1 column dimension
m2row = int(sys.argv[2]) # matrix 2 row dimension
m2col = int(sys.argv[5]) # matrix 2 column dimension
op = sys.argv[3]         # string for operation to perform

matrix_1 = json.loads(sys.argv[6])
matrix_2 = json.loads(sys.argv[7])

print "<br> Matrix operation selected: ", op
print "<br> The matrix 1 column dimension is ", m1col
print "<br> The matrix 2 row dimension is ", m2row, "<br><br>"

""" read matrix 1 JSON file """
"""
with open ('matrix_1_data.json') as M1_data:
    matrix_1 = json.load(M1_data)   # load matrix 1 data
"""
""" read matrix 2 JSON file"""   
"""
with open ('matrix_2_data.json') as M2_data:
    matrix_2 = json.load(M2_data)   # load matrix 2 data
"""

if (op == 'multiplication'):
    mat_mult(m1col, m2row, matrix_1, matrix_2)      # matrix multiplication
elif (op == 'addition'):
    mat_add(matrix_1, matrix_2)                     # matrix addition
elif (op == 'subtraction'):
    mat_sub(matrix_1, matrix_2)                     # matrix subtraction
elif (op == 'inversion'):
    mat_inverse(m1row, m1col, m2row, m2col, matrix_1, matrix_2) # matrix inverse
elif (op == 'transposition'):
    mat_trans(matrix_1, matrix_2)                   # matrix transpose
elif (op == '1D-DFT'):
    dft_1d(matrix_1, matrix_2, m1col, m2col)        # 1-Dimensional discrete fourier transform
elif (op == '1D-IDFT'):
    idft_1d(matrix_1, matrix_2)                     # 1-Dimensional inverse discrete fourier transform
elif (op == '2D-DFT'):
    dft_2d(matrix_1, matrix_2)                      # 2-Dimensional discrete fourier transform
elif (op == '2D-IDFT'):
    idft_2d(matrix_1, matrix_2)                     # 2-Dimensional inverse discrete fourier transform  
else:                                               # else, an operation was not selected
    print "Did not enter operation to perform"




