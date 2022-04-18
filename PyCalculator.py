#Import modules/packages
from tkinter import *

#Instantiate the tkinter session
root = Tk()
root.title("Simple Calculator")

#Initiate variables
running_value = 0

#Create entry field at top of window
e = Entry(root, width=35, border=5)
e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)


#Define necessary functions for use in calculator program

def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return

def field_clear():
    e.delete(0,END)

def add_fxn():
    first_number = e.get()
    global first_num
    global operation
    operation = "addition"
    first_num = int(first_number)
    e.delete(0,END)

def subt_fxn():
    first_number = e.get()
    global first_num
    global operation
    operation = "subtraction"
    first_num = int(first_number)
    e.delete(0,END)

def mult_fxn():
    first_number = e.get()
    global first_num
    global operation
    operation = "multiplication"
    first_num = int(first_number)
    e.delete(0,END)

def div_fxn():
    first_number = e.get()
    global first_num
    global operation
    operation = "division"
    first_num = int(first_number)
    e.delete(0,END)

def equal_fxn():
    second_number = int(e.get())
    if operation == "addition":
        total = first_num + second_number
    elif operation == "subtraction":
        total = first_num - second_number
    elif operation == "multiplication":
        total = first_num * second_number
    else:
        total = first_num / second_number
    e.delete(0,END)
    e.insert(0, total)

#Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_10 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))  
button_add = Button(root, text="+", padx=39, pady=20, command= add_fxn)
button_subtract = Button(root, text="-", padx=39, pady=20, command= subt_fxn)
button_multiply = Button(root, text="*", padx=39, pady=20, command= mult_fxn)
button_divide = Button(root, text="/", padx=39, pady=20, command= div_fxn)
button_equal = Button(root, text="=", padx=91, pady=20, command= equal_fxn)
button_clear = Button(root, text="Clear", padx=79, pady=20, command= field_clear)

#Put the buttons on the screen
button_1.grid(row= 3, column=0)
button_2.grid(row= 3, column=1)
button_3.grid(row= 3, column=2)

button_4.grid(row= 2, column=0)
button_5.grid(row= 2, column=1)
button_6.grid(row= 2, column=2)

button_7.grid(row= 1, column=0)
button_8.grid(row= 1, column=1)
button_9.grid(row= 1, column=2)

button_10.grid(row=4, column=0)
button_equal.grid(row=4, column=1, columnspan=2)

button_clear.grid(row=5, column=1, columnspan=2)
button_add.grid(row=5, column=0)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


root.mainloop()