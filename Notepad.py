from tkinter import *
from matplotlib import widgets
from menuBar import menuBar

# for connecting scrollbar to a widget
# 1. widget (yscrollcommand=scrollbar.set)
# 2. scrollbar.config(command=widget.yview)

root = Tk()
root.geometry("455x400")
root.title("Notepad")


# frame = Frame(root, bg="#39393c", width=500).pack(side=LEFT, fill=Y)
# text = Text(frame)

# NOTE
# scrollbar ke y-view ko textbox ke y-view se connect krna hai
# and textbox ke y-view ko scrollbar ke y-view se connect krna hai


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root, yscrollcommand=scrollbar.set)
text.pack(side=LEFT, anchor="nw")

scrollbar.config(command=text.yview)

root.mainloop()

