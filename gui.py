# Creating an interface for using the calculator

from tkinter import *
from customtkinter import *

# Creating the theme of the interface


root = Tk()
root.geometry("400x530")
root.title("Simple Calculator")
root.wm_iconphoto

# characters entry box
entry = Entry(root, fg = "white", bg = "black")
entry.grid(column = 0, row = 1, columnspan= 4)

# numbers button
butt1 = Button(root, text= "0", command= True )
butt1.grid(column= 0, row= 6, padx=10, pady=10)

butt2 = Button(root, text= "1", command= True )
butt2.grid(column= 0, row= 5, padx=10, pady=10)

butt3 = Button(root, text= "2", command= True )
butt3.grid(column= 1, row= 5, padx=10, pady=10)

butt4 = Button(root, text= "3", command= True )
butt4.grid(column= 2, row= 5, padx=10, pady=10)

butt5 = Button(root, text= "4", command= True )
butt5.grid(column= 0, row= 4, padx=10, pady=10)

butt6 = Button(root, text= "5", command= True )
butt6.grid(column= 1, row= 4, padx=10, pady=10)

butt7 = Button(root, text= "6", command= True )
butt7.grid(column= 2, row= 4, padx=10, pady=10)

butt8 = Button(root, text= "7", command= True )
butt8.grid(column= 0, row= 3, padx=10, pady=10)

butt9 = Button(root, text= "8", command= True )
butt9.grid(column= 1, row= 3, padx=10, pady=10)

butt0 = Button(root, text= "9", command= True )
butt0.grid(column= 2, row= 3, padx=10, pady=10)


# symbols buttons
butt11 = Button(root, text= ".", command= True )
butt11.grid(column= 2, row= 6, padx=10, pady=10)

butt12 = Button(root, text= "-", command= True )
butt12.grid(column= 1, row= 6, padx=10, pady=10)

butt13 = Button(root, text= "+", command= True )
butt13.grid(column= 3, row= 2, padx=10, pady=10)

butt14 = Button(root, text= "x", command= True )
butt14.grid(column= 3, row= 4, padx=10, pady=10)

butt15 = Button(root, text= "/", command= True )
butt15.grid(column= 3, row= 3, padx=10, pady=10)

# function buttons
butt16 = Button(root, text= "CLR", command= True )
butt16.grid(column= 0, row= 2, padx=10, pady=10)

butt17 = Button(root, text= "=", command= True )
butt17.grid(column= 4, row= 6, rowspan= 2, padx=10, pady=10)

butt18 = Button(root, text= "del", command= True )
butt18.grid(column= 1, row= 2, padx=10, pady=10)

butt19 = Button(root, text= "N/A", command= DISABLED )
butt19.grid(column= 2, row= 2, padx=10, pady=10)


root.mainloop()
