# Task 1: Perform Basic Mathematical Operations

# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# -	Addition
# -	Subtraction
# -	Multiplication
# -	Division
# 3.  Displays the results of each operation on the screen


num1 = int(input("Enter Your First Number Here: "))
num2 = int(input("Enter Your Second Number Here: "))

add = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2

print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", multi)
print("Division: ", div)

print("FINAL RESULTS : ",add, sub, multi, div)



#Task 2: Create a Personalized Greeting

# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.


First_Name = input("Enter Your First Name: ")
Second_Name = input("Enter Your Second Name: ")

Full_Name = First_Name + " " + Second_Name

print("Hello,",Full_Name,"Welcome to the world of coding")