import numpy as np
a = np.array([[1,2,],[3,4,]])
print("Matrix\n",a)
u,s,v = np.linalg.svd(a)
print("U matrix\n",u,"/nS matrix\n",s,"/nVT matrix\n",v)
sigmaMatrix = np.zeros((a.shape[0],a.shape[1],))
print("Zero matrix\n",sigmaMatrix)
np.fill_diagonal(sigmaMatrix,s)
print("Filling diagonal with S matrix\n",sigmaMatrix)
b = u.dot(sigmaMatrix.dot(v))
print("Reconstructed matrix\n",sigmaMatrix)

'''
OUTPUT

Matrix
 [[1 2]
 [3 4]]
U matrix
 [[-0.40455358 -0.9145143 ]
 [-0.9145143   0.40455358]] /nS matrix
 [5.4649857  0.36596619] /nVT matrix
 [[-0.57604844 -0.81741556]
 [ 0.81741556 -0.57604844]]
Zero matrix
 [[0. 0.]
 [0. 0.]]
Filling diagonal with S matrix
 [[5.4649857  0.        ]
 [0.         0.36596619]]
Reconstructed matrix
 [[5.4649857  0.        ]
 [0.         0.36596619]]
 
'''