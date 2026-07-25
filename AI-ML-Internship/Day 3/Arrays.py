import numpy as np

#Q1: Create an array of 5 numbers.
numbers = [10, 20, 30, 40, 50]

#Q2: Create an array of 5 names.
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

#Q3: Print the first element.
print(numbers[0])
print(names[0])

#Q4: Print the last element.
print(numbers[-1])
print(names[-1])

#Q5: Print the third element.
print(numbers[2])
print(names[2])

#Q6: Print all elements.
for n in numbers:
    print(n)

for name in names:
    print(name)

#Q7: Find the length of the array.
print(len(numbers))
print(len(names))

#Q8: Create an array using np.arange(1,11).

arr1 = np.arange(1, 11)
print(arr1)

#Q9: Create an array using np.zeros(5).
arr2 = np.zeros(5)
print(arr2)

#Q10: Create an array using np.ones(5).
arr3 = np.ones(5)
print(arr3)