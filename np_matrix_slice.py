import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [1,3,5,7],
                [2,4,6,8]])

print("ROWS EXCLUDING FIRST ROW\n",arr[1:,:])
print("ROWS EXCLUDING LAST COLUMN\n",arr[:,:-1])
print("2&3RD ROWS 1&2ND COLUMNS\n",arr[1:3,:2])
print("2&3RD COLUMNS\n",arr[:,2:4])
print("2&3RD ELEMENT OF 1st ROW\n",arr[0,2:4])

''' 

# OUTPUT #

ROWS EXCLUDING FIRST ROW
 [[5 6 7 8]
 [1 3 5 7]
 [2 4 6 8]]
ROWS EXCLUDING LAST COLUMN
 [[1 2 3]
 [5 6 7]
 [1 3 5]
 [2 4 6]]
2&3RD ROWS 1&2ND COLUMNS
 [[5 6]
 [1 3]]
2&3RD COLUMNS
 [[3 4]
 [7 8]
 [5 7]
 [6 8]]
2&3RD ELEMENT OF 1st ROW
 [3 4]

'''