import math
from tkinter import *

def calculator():
    root = Tk()
    root.title("Calculator")


    def button_click(number):
        current = inputBox.get()
        inputBox.delete(0, END)
        inputBox.insert(0, str(current) + str(number))

    def button_clear():
        inputBox.delete(0, END)

    def button_add():
        global num1
        global math
        math = "add"
        num1 = float(inputBox.get())
        inputBox.delete(0, END)

    def button_sub():
        global num1
        global math
        math = "sub"
        num1 = float(inputBox.get())
        inputBox.delete(0, END)

    def button_mul():
        global num1
        global math
        math = "mul"
        num1 = float(inputBox.get())
        inputBox.delete(0, END)

    def button_div():
        global num1
        global math
        math = "div"
        num1 = float(inputBox.get())
        inputBox.delete(0, END)

    def button_equal():
        num2 = float(inputBox.get())
        inputBox.delete(0, END)

        if math == "add":
            inputBox.insert(0, num1 + num2)

        if math == "sub":
            inputBox.insert(0, num1 - num2)

        if math == "mul":
            inputBox.insert(0, num1 * num2)

        if math == "div":
            inputBox.insert(0, num1 / num2)



    # Defining button
    inputBox = Entry(root, borderwidth=5, width=40, fg='black', bg='white')
    inputBox.grid(row=0, column=0, columnspan=3)

    button_1 = Button(root, text='1' ,padx=30, pady=15, command=lambda: button_click(1))
    button_2 = Button(root, text='2' ,padx=30, pady=15, command=lambda: button_click(2))
    button_3 = Button(root, text='3' ,padx=30, pady=15, command=lambda: button_click(3))

    button_4 = Button(root, text='4' ,padx=30, pady=15, command=lambda: button_click(4))
    button_5 = Button(root, text='5' ,padx=30, pady=15, command=lambda: button_click(5))
    button_6 = Button(root, text='6' ,padx=30, pady=15, command=lambda: button_click(6))

    button_7 = Button(root, text='7' ,padx=30, pady=15, command=lambda: button_click(7))
    button_8 = Button(root, text='8' ,padx=30, pady=15, command=lambda: button_click(8))
    button_9 = Button(root, text='9' ,padx=30, pady=15, command=lambda: button_click(9))

    button_0 = Button(root, text='0' ,padx=30, pady=15, command=lambda: button_click(0))

    button_clear = Button(root, text='clear' ,padx=62, pady=15, command=button_clear)
    button_equal = Button(root, text='=' ,padx=70, pady=15, command=button_equal)

    button_add = Button(root, text='+' ,padx=30, pady=15, command=button_add)
    button_sub = Button(root, text='-' ,padx=30, pady=15, command=button_sub)
    button_mul = Button(root, text='*' ,padx=30, pady=15, command=button_mul)
    button_div = Button(root, text='/' ,padx=30, pady=15, command=button_div)


    # Put the buttons on the screen
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)
    button_0.grid(row=4, column=0)

    button_clear.grid(row=4, column=1, columnspan=2)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_sub.grid(row=6, column=0)
    button_mul.grid(row=6, column=1)
    button_div.grid(row=6, column=2)


    root.mainloop()