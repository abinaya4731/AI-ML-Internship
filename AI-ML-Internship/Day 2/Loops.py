#Q1: Print numbers from 1 to 10.

for i in range(1, 11):
    print(i)

#Q2: Print numbers from 10 to 1.

for i in range(10, 0, -1):
    print(i)

#Q3: Print even numbers from 1 to 20.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#Q4: Print odd numbers from 1 to 20.

for i in range(1, 21):
    if i % 2 != 0:
        print(i)

    
#Q5: Print the multiplication table of 5.

for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

#Q6: Find the sum of numbers from 1 to 100.

sum = 0
for i in range(1, 101):
    sum += i
print("The sum of numbers from 1 to 100 is:", sum)

#Q7: Print the square of numbers from 1 to 10.

for i in range(1, 11):
    print("The square of", i, "is:", i * i)

#Q8: Print each letter of the word "Python".

for letter in "Python":
    print(letter)

#Q9: Use a while loop to print numbers from 1 to 5.

i = 1
while i <= 5:
    print(i)
    i += 1      

#Q10: Take a number from the user and print numbers from 1 to that number.

num = int(input("Enter a number: "))
for i in range(1, num + 1):
    print(i)