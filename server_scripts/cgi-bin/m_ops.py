#!/home/server/miniconda2/bin/python

import numpy as np
import timeit
from numpy.linalg import inv
import json, codecs

import requests
import sys
import os
import cgitb
cgitb.enable()    
#print("Content-Type: text/html;charset=utf-8")

""" Must specify to the server the type of content to display """
print("Content-type: text/html; charset=utf-8")
print("\n")


class ComplexEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, complex):
			return [obj.real, obj.imag]
		# Let the base class default method raise the TypeError
		return json.JSONEncoder.default(self, obj)

################################################################################
#
# Function: test_prime
# Description: tests if a number is a prime number
# Input: number to test
# Output: Return 1 if number is prime or return 0 if number is not prime
#
def test_prime(n):
    divisors = 0
    for i in range(1, int(np.sqrt(n))+1):
        if (n % i == 0):
            divisors = divisors + 1
    if ((divisors == 1) & (n > 1)):
        return 1
    else:
        return 0
#
# Function: get_primes
# Description: Counts the number of prime numbers found up to the 
# number specified at each element in the array
# Input: Array for first matrix
# Output: An array with the number of prime numbers found up to the 
# number specified at each element in the array
#
def get_primes(matrix_1):
    for i in range(len(matrix_1)):
        for k in range(len(matrix_1[i])):
            val = int(matrix_1[i][k])
            primes = 0
            for n in range(1,val+1):
                if (test_prime(n) == 1):
                    primes = primes + 1
            matrix_1[i][k] = primes


################################################################################
#
# Function: find_max
# Description: Find element-wise maximum value between two arrays
# Input: first array and second array
# Output: Element-wise maximum value between two arrays
#
def find_max(m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    if (np.shape(M1) != np.shape(M2)):
        print("Matrices with entered dimensions do not match")
	
    else:
	result = np.maximum(M1, M2)
	print(result)

################################################################################
# 
# Function: div
# Description: Element-wise division of M1 array by M2 array
# Input: m1 array and m2 array
# Output: Element-wise division of M1 array by M2 array
#
def div(m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    if (np.shape(M1) != np.shape(M2)):
	print("Matrices with entered dimensions do not match")
	
    else:
	division = np.divide(M1, M2)
	print(division)

################################################################################
#
# Function: det
# Description: Find the determinant of a 2x2 array
# Input: first array and second array
# Output: Print the determinant of the first 2x2 array and second 2x2 array
#
def det(m1, m2):
    #M1 = np.array(m1)
    #M2 = np.array(m2)
    if (np.shape(M1) != np.shape(M2)):
	print("Matrices with entered dimensions do not match: Enter 2x2 matrix")

    else:
	a = np.array([m1, m2])
	result = np.linalg.det(a)
	print(result) 

################################################################################
#
# Function: solve
# Description: Solve a 2x2 array of linear equations
# Input: m1 array, number of rows for m1 array, number of columns for m1 array
# Output: An array with the solution for each equation
#
def solve(m1, rowM1, colM1):
    M1 = np.array(m1)
    if (rowM1 != colM1 ):
	print("Matrices with entered dimensions cannot be solved: Only enter 2 by 2 input matrix")
	
    else:
	b = np.array([10,14])
	result = np.linalg.solve(M1, b)
	print(result)

################################################################################
#
# Function: exp
# Description: First array elements raised to powers from second array, element-wise 
# Input: first array and second array
# Output: An array with first array elements raised to powers from second array, element-wise
#
def exp(m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    if (np.shape(M1) != np.shape(M2)):
	print("Matrices with entered dimensions do not match")
	
    else:
	result = np.power(M1, M2)
	print(result)

################################################################################
#
# Function: nat_log
# Description: Find the natural logarithm of first array and second array, element-wise
# Input: first array and second array
# Output: Natural logarithm in base "e" for first array and second array, element-wise
#
def nat_log(m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    result_1 = np.log(M1)
    result_2 = np.log(M2)
    print(result_1)
    print(result_2)

################################################################################
#
# Function: nth_diff
# Description: Calculate the n-th discrete difference along a given axis
# Input: First array and second array
# Output: An array with the n-th discrete difference along a given axis
#
def nth_diff(m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    result_1 = np.diff(M1)
    result_2 = np.diff(M2)
    print(result_1)
    print(result_2)

################################################################################
#
# Function: sum_all
# Description: Sum of all elements in the array
# Input: first array and second array
# Output: Sum of all elements in the first array and the sum
# of all elements in the second array
#
def sum_all(m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    result_1 = np.sum(M1)
    result_2 = np.sum(M2)
    print(result_1)
    print(result_2)

################################################################################
#
# Function: sq_root
# Description: Find the positive square root of an array, element-wise
# Input: First array and second array 
# Output: Print the positive square root for the first array, element-wise
# and print the positive square root for the second array, element-wise
#
def sq_root(m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    result_1 = np.sqrt(M1)
    result_2 = np.sqrt(M2)
    print(result_1)
    print(result_2)

################################################################################
#
# Function: find_hypot
# Description: Find the hypotenuse of a right triangle, given the "legs" 
# (i.e. an element from first array and another element from second array are the legs)
# Input: First array and second array
# Output: Print the hypotenuse as an array, element-wise
#
def find_hypot(m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    result = np.hypot(M1, M2)
    print(result)

################################################################################
#
# Function: deg_rad
# Description: Convert angles from degrees to radians
# Input: First array and second array
# Output: Return the corresponding angle in radians for the first array as well as 
# for the second array
#
def deg_rad(m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    result_1 = np.deg2rad(M1)
    result_2 = np.deg2rad(M2)
    print(result_1)
    print(result_2)

################################################################################
#
# Function: mat_mult
# Description: Calculate the product of two arrays, not the element-wise multiplication
# Input: Number of columns for first array, number of rows for second array,
# first array, and second array
# Output: Print the product of two arrays
#
def mat_mult(colM1, rowM2, m1, m2):
    if (colM1 != rowM2):        # if matrix 1 column number and matrix 2 row number don't match
        print("Matrices with entered dimensions cannot be multiplied")
	
    else:                       # if they match, perform multiplication
        M1 = np.array(m1)       # define array for matrix 1
        M2 = np.array(m2)       # define array for matrix 2
        product = np.dot(M1, M2)    # dot() function performs matrix multiplication, not element-wise multiplication
        print(product)

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
    if (np.shape(mat1) != np.shape(mat2)):  # check if dimensions match
        print("Matrices with entered dimensions cannot be added")
	
    else:                                   # if they match perform addition
        M1 = mat1               
        M2 = mat2
        result = np.add(M1, M2)
        print(result)
            
################################################################################        
#
# Function: mat_sub
# Description: Subtract two arrays, element-wise 
# Input: First array and second array
# Output: The difference of first array and second array, element-wise 
#           
def mat_sub(m1, m2):
    M1 = np.array(m1)
    M2 = np.array(m2)
    if (np.shape(M1) != np.shape(M2)):      # check if matrix 1 and matrix 2 dimensions don't match
        print("Matrices with entered dimensions cannot be subtracted")
	
    else:                                       # if matrix 1 and matrix 2 dimensions match, perform subtraction
        M1 = mat1
        M2 = mat2
        sub = np.subtract(M1, M2)               
        print(sub)
            
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
    if ((rowM1 != colM1) | (rowM2 != colM2)):   # if matrix 1 or matrix 2 are not square matrices
        print("Matrices with entered dimensions cannot be inverted")
	
    else:                                       # perform inverse if both matrices are square matrices
        inv1 = inv(M1)                          # apply the inverse of matrix 1
        inv2 = inv(M2)                          # apply the inverse of matrix 2
        print(inv1)
		print(inv2)

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
    print(trans1)
    print(trans2)

################################################################################
#
# Function: dft_1d
# Description: Calculate the 1-Dimensional discrete fourier transform for first array
# and second array
# Input: First array, second array, number of columns for first array, number of columns
# for second array
# Output: Print the 1-Dimensional discrete fourier transform for first array
# and second array
#
def dft_1d(m1, m2, colM1, colM2):
    dft1 = np.fft.fft(np.exp(2j * np.pi * np.array(m1) / colM1))
    dft2 = np.fft.fft(np.exp(2j * np.pi * np.array(m2) / colM2))
    print(dft1)
    print(dft2)

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
    print(idft1)
    print(idft2)  

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
    dft1 = np.fft.fft2(M1)
    dft2 = np.fft.fft2(M2)
    print(dft1)
    print(dft2)
    
    
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
    print(idft1)
    print(idft2)

################################################################################
#
# Function: primes
# Description: Find the number of prime numbers at each element in the first array
# and second array. Then sum all the elements for the first array and second array.
# Input: First array and second array
# Output: Print the sum of all elements in the first array and second array
#
def primes(m1, m2):
    M1 = np.array(m1)
    M1 = np.true_divide(M1, 10)
    M2 = np.array(m2)
    M2 = np.true_divide(M2, 10)
    result_1 = np.sum(get_primes(M1))
    result_2 = np.sum(get_primes(M2))
    print(result_1)
    print(result_2)


################################################################################
#    Start of the main program
################################################################################
if os.environ.get("REQUEST_METHOD") == "POST":
	
	start_time = timeit.default_timer()

	posted_content = sys.stdin.read().decode()
	server_list = json.loads(posted_content)	# load json string
	client_params = json.loads(server_list[0])	# load json matrix parameters from client
	matrix_1 = json.loads(server_list[1])		# convert matrix 1 from unicode string to a list
	matrix_2 = json.loads(server_list[2])		# convert matrix 2 from unicode string to a list
	
	
	

	op = client_params[0]	# operation to perform
	m1row = client_params[1]	
	m1col = client_params[2]
	m2row = client_params[3]
	m2col = client_params[4]
	
	
	
	if (op == 'multiplication'):
    		mat_mult(m1col, m2row, matrix_1, matrix_2)      	
	elif (op == 'addition'):
    		mat_add(matrix_1, matrix_2)                     	
	elif (op == 'subtraction'):
    		mat_sub(matrix_1, matrix_2)
	elif (op == 'inversion'):
    		mat_inverse(m1row, m1col, m2row, m2col, matrix_1, matrix_2) 
	elif (op == 'transposition'):
    		mat_trans(matrix_1, matrix_2)                   	
	elif (op == '1D-DFT'):
    		dft_1d(matrix_1, matrix_2, m1col, m2col)                # 1-Dimensional discrete fourier transform
	elif (op == '1D-IDFT'):
    		idft_1d(matrix_1, matrix_2)                             # 1-Dimensional inverse discrete fourier transform
	elif (op == '2D-DFT'):
    		dft_2d(matrix_1, matrix_2)                              # 2-D discrete fourier transform
	elif (op == '2D-IDFT'):
    		idft_2d(matrix_1, matrix_2)				# 2-D inverse discrete fourier transform
	elif (op == 'maximum'):
    		find_max(matrix_1, matrix_2)				# find maximum value element-wise			 
	elif (op == 'division'):
    		div(matrix_1, matrix_2)					# element-wise division
	elif (op == 'determinant'):
    		det(matrix_1, matrix_2)					# 2 by 2 determinant
	elif (op == 'solve'):
    		solve(matrix_1, m1row, m1col)				# 2 by 2 linear equation
	elif (op == 'exponent'):				
    		exp(matrix_1, matrix_2)					# exponent operation
	elif (op == 'ln'):
    		nat_log(matrix_1, matrix_2)					# natural logarithm
	elif (op == 'diff'):
    		nth_diff(matrix_1, matrix_2)					# nth difference
	elif (op == 'sum_all'):
    		sum_all(matrix_1, matrix_2)					# sum of all elements
	elif (op == 'sqrt'):
    		sq_root(matrix_1, matrix_2)					# square root
	elif (op == 'hypot'):
    		find_hypot(matrix_1, matrix_2)				# hypotenuse of triangle
	elif (op == 'deg2rad'):
    		deg_rad(matrix_1, matrix_2)					# convert from degrees to radians
	elif (op == 'primes'):
		primes(matrix_1, matrix_2)	
	else:                                               # else, print error
    		print "Did not enter operation to perform, operation not found and/or operation was entered incorrectly"
	


