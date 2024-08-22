from numpy import random,linalg

a = random.randint(10,size=(2,2))

print("DETERMINANT OF THE MATRIX IS\n",linalg.det(a))
print("INVERSE OF THE MATRIX IS\n",linalg.inv(a))
print("RANK OF THE MATRIX IS\n",linalg.matrix_rank(a))
print("1D MATRIX IS\n",a.flatten())


