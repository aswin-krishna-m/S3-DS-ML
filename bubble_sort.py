arr = []
n = int(input("Enter size of array:"))

for i in range(n):
    arr.append(int(input(f"Enter element {i+1} : ")))

print(f"The array is : {arr}")

for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print("Sorted array is: ",arr)