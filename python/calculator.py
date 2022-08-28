from tkinter import *

screen = Tk()
screen.title("Calculator")
screen.resizable(width=False, height=False)

user_input = Entry(screen)
user_input.grid(row=0, column=0, columnspan=3)

def add_buffer():
    global first_number
    first_number = float(user_input.get())
    user_input.delete(0, END)
    return first_number

def subtract_buffer():
    global first_number
    first_number = -abs(float(user_input.get()))
    user_input.delete(0, END)
    return first_number

def multiply_buffer():
    global first_number
    first_number = "m" + user_input.get()
    user_input.delete(0, END)
    return first_number

def divide_buffer():
    global first_number
    first_number = "d" + user_input.get()
    user_input.delete(0, END)
    return first_number

def equals():
    global first_number
    second_number = float(user_input.get())
    user_input.delete(0, END)
    if type(first_number) == str:
        if first_number[0] == "m":
            calculate = float(first_number[1:]) * second_number
        elif first_number[0] == "d":
            calculate = float(first_number[1:]) / second_number
    elif first_number < 0:
        calculate = abs(first_number) + -abs(second_number)
    else:
        calculate = first_number + second_number
    if calculate.is_integer():
        calculate = int(calculate)
    first_number = 0
    second_number = 0
    user_input.insert(0, calculate)


one = Button(screen, text="1", padx=40, pady=20, command=lambda: user_input.insert(END, "1"))
two = Button(screen, text="2", padx=40, pady=20, command=lambda: user_input.insert(END, "2"))
three = Button(screen, text="3", padx=40, pady=20, command=lambda: user_input.insert(END, "3"))
four = Button(screen, text="4", padx=40, pady=20, command=lambda: user_input.insert(END, "4"))
five = Button(screen, text="5", padx=40, pady=20, command=lambda: user_input.insert(END, "5"))
six = Button(screen, text="6", padx=40, pady=20, command=lambda: user_input.insert(END, "6"))
seven = Button(screen, text="7", padx=40, pady=20, command=lambda: user_input.insert(END, "7"))
eight = Button(screen, text="8", padx=40, pady=20, command=lambda: user_input.insert(END, "8"))
nine = Button(screen, text="9", padx=40, pady=20, command=lambda: user_input.insert(END, "9"))
zero = Button(screen, text="0", padx=40, pady=20, command=lambda: user_input.insert(END, "0"))
clear = Button(screen, text="Clear", padx=30, pady=20, command=lambda: user_input.delete(0, END))
dot = Button(screen, text=".", padx=40, pady=20, command=lambda: user_input.insert(END, "."))
plus = Button(screen, text="+", padx=38, pady=20, command=add_buffer)
minus = Button(screen, text="-", padx=40, pady=20, command=subtract_buffer)
multiply = Button(screen, text="*", padx=40, pady=20, command=multiply_buffer)
divide = Button(screen, text="/", padx=40, pady=20, command=divide_buffer)
equals = Button(screen, text="   =   ", padx=80, pady=20, command=equals)

one.grid(row=3, column=0)
two.grid(row=3, column=1)
three.grid(row=3, column=2)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
seven.grid(row=1, column=0)
eight.grid(row=1, column=1)
nine.grid(row=1, column=2)
zero.grid(row=4, column=0)
dot.grid(row=4, column=1)
clear.grid(row=4, column=2)
plus.grid(row=5, column=0)
minus.grid(row=5, column=1)
multiply.grid(row=5, column=2)
equals.grid(row=6, column=1, columnspan=2)
divide.grid(row=6, column=0)

screen.mainloop()