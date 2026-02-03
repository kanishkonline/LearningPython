# Task 2: Using the Math Module for Calculations
 
"""
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.

2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)

3.   Displays the calculated results.
"""

import math

user_input = float(input("Enter the number for calculation: "))

square_root = math.sqrt(user_input)
natural_log = math.log(user_input)
sine_value = math.sin(user_input)


print(f"Sqaure root of your input is : {square_root:.2f}")
print(f"Natural Log (ln) of your input is : {natural_log}")
print(f"Sine (in radians) of your input is : {sine_value}")