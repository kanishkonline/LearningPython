# Task 1: Create a Dictionary of Student Marks

"""
Problem Statement: Write a Python program that:

1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

"""

# Step 1 — create dictionary
students = {
    "kanishk":100,
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 74
}

# Step 2 — take user input
name = input("Enter the student's name: ")

# Step 3 & 4 — check and display marks
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")