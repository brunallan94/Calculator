# Creating an interface for using the calculator

from tkinter import *
from customtkinter import *

# Creating the theme of the interface
set_default_color_theme("red")

root = Tk()
root.geometry("400x600")
root.title("Simple Calculator")

# number entry box
entry = Entry(root, fg = "white", bg = "black")
entry.grid(column = 0, row = 1, columnspan= 4)

# numbers button
butt1 = Button(root, text= "0", command= True )
butt1.grid(column= 0, row= 6)

butt1 = Button(root, text= "1", command= True )
butt1.grid(column= 0, row= 5)

butt1 = Button(root, text= "2", command= True )
butt1.grid(column= 1, row= 5)

butt1 = Button(root, text= "3", command= True )
butt1.grid(column= 2, row= 5)

butt1 = Button(root, text= "4", command= True )
butt1.grid(column= 0, row= 4)

butt1 = Button(root, text= "5", command= True )
butt1.grid(column= 1, row= 4)

butt1 = Button(root, text= "6", command= True )
butt1.grid(column= 2, row= 4)

butt1 = Button(root, text= "7", command= True )
butt1.grid(column= 0, row= 3)

butt1 = Button(root, text= "8", command= True )
butt1.grid(column= 1, row= 3)

butt1 = Button(root, text= "9", command= True )
butt1.grid(column= 2, row= 3)


# symbols buttons
butt1 = Button(root, text= ".", command= True )
butt1.grid(column= 2, row= 6)

butt1 = Button(root, text= "-", command= True )
butt1.grid(column= 1, row= 6)

butt1 = Button(root, text= "+", command= True )
butt1.grid(column= 3, row= 5)

butt1 = Button(root, text= "x", command= True )
butt1.grid(column= 3, row= 4)

butt1 = Button(root, text= "/", command= True )
butt1.grid(column= 3, row= 3)

# function buttons
butt1 = Button(root, text= "CLR", command= True )
butt1.grid(column= 0, row= 2)

butt1 = Button(root, text= "=", command= True )
butt1.grid(column= 4, row= 6, rowspan= 2)

butt1 = Button(root, text= "del", command= True )
butt1.grid(column= 1, row= 2)

butt1 = Button(root, text= "N/A", command= DISABLED )
butt1.grid(column= 2, row= 2)


root.mainloop()