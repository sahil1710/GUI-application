from tkinter import *
from tkinter import ttk
from animation import Animate
from calculator import calculator
from screenShot import screenShot
from videoWriting import recording
from webCam import webCam

def menuBar(root):
    mainMenu = Menu(root)

    fileMenu = Menu(mainMenu, tearoff=0)
    fileMenu.add_command(label="New")
    fileMenu.add_command(label="Open")
    fileMenu.add_command(label="Save")
    fileMenu.add_command(label="Save As")
    fileMenu.add_command(label="Close")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quit)
    mainMenu.add_cascade(label='File', menu=fileMenu)

    editMenu = Menu(mainMenu, tearoff=0)
    editMenu.add_command(label="Undo")
    editMenu.add_separator()
    editMenu.add_command(label="Cut")
    editMenu.add_command(label="Copy")
    editMenu.add_command(label="Paste")
    editMenu.add_command(label="Delete")
    editMenu.add_command(label="Select All")
    mainMenu.add_cascade(label='Edit', menu=editMenu)

    helpMenu = Menu(mainMenu, tearoff=0)
    helpMenu.add_command(label="About")
    helpMenu.add_command(label="Contact")
    mainMenu.add_cascade(label='Help', menu=helpMenu)

    toolMenu = Menu(mainMenu, tearoff=0)
    toolMenu.add_command(label="Calculator", command=calculator)
    toolMenu.add_command(label="Start WebCam", command=webCam)
    toolMenu.add_command(label="ScreenShot", command=screenShot)
    toolMenu.add_command(label="Video Recording", command=recording)
    mainMenu.add_cascade(label='Tools', menu=toolMenu)

    return mainMenu
