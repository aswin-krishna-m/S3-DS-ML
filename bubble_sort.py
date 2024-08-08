arr = input("Enter elements separated by single space:")
arr = [int(i) for i in arr.split()]
print(f"The array is : {arr}")

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print("Sorted array is: ",arr)


""" 
OUTPUT 

Enter elements separated by single space:3 4 6 3 2 
The array is : [3, 4, 6, 3, 2]
Sorted array is:  [2, 3, 3, 4, 6]

"""
