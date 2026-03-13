# STEP1: IMPORTING
from tkinter import *
import tkinter.font as tkFont

# STEP2: GUI INTERACTION
window = Tk("CALCULATOR")
window.title("CALCULATOR")
window.geometry("500x500")
custom_font = tkFont.Font(family="Times New Roman", size=15, weight="bold")


# STEP3: ADDING INPUTS

# Entry Box
e = Entry(window, width=50, borderwidth=10, font=custom_font)
e.place(x=0, y=0)



# Buttons: [1 to 0],[ADD, SUB, MULTI, DIV, EQUAL, CLEAR]
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))
# 1
b = Button(window, text="1", width = 12, command = lambda: click(1))
b.place(x = 10, y = 60)
# 2
b = Button(window, text="2", width = 12, command = lambda: click(2))
b.place(x = 80, y = 60)
# 3
b = Button(window, text="3", width = 12, command = lambda: click(3))
b.place(x = 170, y = 60)
# 4
b = Button(window, text="4", width = 12, command = lambda: click(4))
b.place(x = 10, y = 120)
# 5
b = Button(window, text="5", width = 12, command = lambda: click(5))
b.place(x = 80, y = 120)
# 6
b = Button(window, text="6", width = 12, command = lambda: click(6))
b.place(x = 170, y = 120)
# 7
b = Button(window, text="7", width = 12, command = lambda: click(7))
b.place(x = 10, y = 180)
# 8
b = Button(window, text="8", width = 12, command = lambda: click(8))
b.place(x = 80, y = 180)
# 9
b = Button(window, text="9", width = 12, command = lambda: click(9))
b.place(x = 170, y = 180)
# 0
b = Button(window, text="0", width = 12, command = lambda: click(0))
b.place(x = 10, y = 240)



# Operators: [Addition, Subtraction, Multiplication, Division, EQUAL, CLEAR]
# ADDITION
def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="+", width = 12, command = add)
b.place(x = 80, y = 240)


# SUBTRACTION
def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="-", width = 12, command = sub)
b.place(x = 170, y = 240)


# MULTIPLICATION
def multiply():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="*", width = 12, command = multiply)
b.place(x = 10, y = 300)


# DIVISION
def divide():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="/", width = 12, command = divide)
b.place(x = 80, y = 300)


# EQUAL
def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0,i + int(n2))
    elif math == "subtraction":
        e.insert(0,i - int(n2))
    elif math == "multiplication":
        e.insert(0,i * int(n2))
    elif math == "division":
        e.insert(0,i / int(n2))

b = Button(window, text="=", width = 12, command= equal)
b.place(x = 170, y = 300)


# CLEAR
def clear():
    e.delete(0, END)

b = Button(window, text="clear", width = 12, command= clear)
b.place(x = 10, y = 350)



# STEP4: MAINLOOP
mainloop()