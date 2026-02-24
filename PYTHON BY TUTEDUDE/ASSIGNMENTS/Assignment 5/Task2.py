# Task 2: Demonstrate List Slicing

"""
Problem Statement: Write a Python program that:

1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

"""
# Step 1 — create list from 1 to 10
numbers = list(range(1, 11))

# Step 2 — extract first five elements
first_five = numbers[:5]

# Step 3 — reverse extracted elements
reversed_list = first_five[::-1]

# Step 4 — print results
print("Original list:", numbers)
print("\nExtracted first five elements:", first_five)
print("\nReversed extracted elements:", reversed_list)