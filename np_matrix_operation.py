import numpy as np
import random

a1 = np.array([[1,3],
               [5,7]])

a2 = np.array([[6,8],
               [2,4]])

print("MATRIX ADDITION \n",np.add(a1,a2))
print("MATRIX SUBTRACTION \n",np.subtract(a2,a1))
print("MATRIX MULTIPLY INDIVIDUAL ELEMENTS \n",np.multiply(a1,a2))
print("MATRIX DIVIDE INDIVIDUAL ELEMENTS \n",np.divide(a2,a1))
print("MATRIX MULTIPLICATION \n",np.dot(a2,a1))
print("MATRIX TRANSPOSE of FIRST MATRIX\n",a1.transpose())
print("SUM OF DIAGONAL ELEMENTS of FIRST MATRIX\n",np.trace(a1))



"""
OUTPUT

MATRIX ADDITION 
 [[ 7 11]
 [ 7 11]]
MATRIX SUBTRACTION
 [[ 5  5]
 [-3 -3]]
MATRIX MULTIPLY INDIVIDUAL ELEMENTS
 [[ 6 24]
 [10 28]]
MATRIX DIVIDE INDIVIDUAL ELEMENTS
 [[6.         2.66666667]
 [0.4        0.57142857]]
MATRIX MULTIPLICATION
 [[46 74]
 [22 34]]
MATRIX TRANSPOSE of FIRST MATRIX
 [[1 5]
 [3 7]]
SUM OF DIAGONAL ELEMENTS of FIRST MATRIX
 8

"""