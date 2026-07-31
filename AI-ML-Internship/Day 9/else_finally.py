try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid Input")
else:
    print("You entered:", num)
finally:
    print("Program Finished")