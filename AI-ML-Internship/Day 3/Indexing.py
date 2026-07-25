import numpy as np
#Print the first element.

arr = np.array([1, 2, 3, 4, 5])
print(arr[0])

#Print the second element.
print(arr[1])

#Print the last element.
print(arr[-1])

#Print the middle element.
print(arr[len(arr)//2])

#Print the first three elements.
print(arr[:3])

#Print the last three elements.
print(arr[-3:])

#Print elements from index 2 to 5.
print(arr[2:5])

#Replace the first element.
arr[0] = 10

#Replace the last element.
arr[-1] = 50

#Print the updated array.
print(arr)