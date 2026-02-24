# Task 2: Write and Append Data to a File

"""
Problem Statement: Write a Python program that:

1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""

import os
path = os.path.join(os.path.dirname(__file__), "output.txt")

try:
    # Step 1 — write data
    text = input("Enter text to write to the file: ")

    with open(path, "w") as file:
        file.write(text + "\n")

    print("\nData successfully written to output.txt.")

    # Step 2 — append data
    more_text = input("\nEnter additional text to append: ")

    with open(path, "a") as file:
        file.write(more_text + "\n")

    print("\nData successfully appended.")

    # Step 3 — read final content
    print("\nFinal content of output.txt:\n")

    with open(path, "r") as file:
        print(file.read())

except Exception as e:
    print("Error:", e)