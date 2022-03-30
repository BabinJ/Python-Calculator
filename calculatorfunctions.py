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