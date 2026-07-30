# Write student marks
with open("marks.txt", "w") as file:
    file.write("Alice - 90\n")
    file.write("Bob - 85\n")
    file.write("Charlie - 88\n")
    file.write("David - 92\n")
    file.write("Eva - 87\n")

# Append one more student's marks
with open("marks.txt", "a") as file:
    file.write("Abinaya - 95\n")

# Read and print the file
with open("marks.txt", "r") as file:
    print("Student Marks:")
    print(file.read())