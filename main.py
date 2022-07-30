from tkinter import *
from tkinter import ttk
from animation import Animate
from menuBar import menuBar
from Email import email
from sortings import *
from sortings.bubble import bubbleSort
from sortings.insertion import insertionSort
from sortings.mergeSort import mergeSort
from sortings.quick import quickSort
from sortings.selection import selectionSort


def start_animation():
    algo = sort_algo.get()
    list = array.get().split(" ")
    for idx, item in enumerate(list):
        list[idx] = int(item)
    print(algo)
    print(list)
    array.delete(0, END)

    if algo == "Insertion Sort":
        insertionSort(list)

    elif algo == "Selection Sort":
        selectionSort(list)

    elif algo == "Bubble Sort":
        bubbleSort(list)

    elif algo == "Quick Sort":
        quickSort(list)

    elif algo == "Merge Sort":
        mergeSort(list)


if __name__ == "__main__":
    root = Tk()
    root.geometry("1500x600")
    # root.resizable(False, False)

    # Creating Menubar
    menu = menuBar(root)
    # Adding Menubar to our software (root window)
    root.config(menu=menu)

    # Creating Select Box to choose sort Algo
    ttk.Label(root, text="Select Sort Method : ").grid(row=0, column=0, padx=10, pady=25)
    sort_algo = StringVar()
    sortChoosen = ttk.Combobox(root, width=30, textvariable=sort_algo)
    sortChoosen['values'] = ('Insertion Sort', 'Selection Sort', 'Bubble Sort', 'Quick Sort', 'Merge Sort')
    sortChoosen.grid(row=0, column=1)
    sortChoosen.current(0)

    # Enter List to sort
    ttk.Label(root, text="Enter Space Seperated Numbers : ").grid(row=1, column=0, padx=10, pady=5)
    array = ttk.Entry(root, width=33)
    array.grid(row=1, column=1)

    animation_button = ttk.Button(root, text="Start Animation", width=30, command=start_animation)
    animation_button.grid(row=2, column=0, pady=15)

    # Separator object
    separator = ttk.Separator(root, orient='vertical')
    separator.place(relx=0.37, rely=0, relwidth=0.2, relheight=1)

    # Adding Email Functionality
    email(root)

    root.mainloop()