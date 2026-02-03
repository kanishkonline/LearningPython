# Task 1: Calculate Factorial Using a Function 

"""
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""

# RECURSION

def fact_rec(num):
    if num == 1:
        return 1
    else:
        factorial = num * fact_rec(num-1)
        return factorial

print(fact_rec(6))


# LOOP

def fact(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1

    return factorial

print(fact(5))
