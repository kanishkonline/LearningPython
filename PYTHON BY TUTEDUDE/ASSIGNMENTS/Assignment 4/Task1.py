# Task 1: Read a File and Handle Errors \

"""
Problem Statement:  Write a Python program that:

1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

"""

try:
    path = r"D:\TUTEDUDE PYTHON\PYTHON BY TUTEDUDE\ASSIGNMENTS\Assignment 4\sample.txt"

    # create & write file
    with open(path, "w") as f:
        f.write("This is sample text file\n")
        f.write("It's made for Assignment 4\n")
        f.write("In Task 1\n")
        f.write("THANK YOU\n")

    # read file
    with open(path, "r") as file:
        print("Reading file content:\n")
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")

except FileNotFoundError:
    print("File not found")