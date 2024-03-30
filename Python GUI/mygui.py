from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        #calls variable "feet" from textvariable=feet from 1st widget
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()             #sets up main application window
root.title("Feet to Meters")    #sets title to "feet to meters"

#Next, we create a frame widget, which will hold the contents of our user interface.
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Creates the widget with feet with entry box
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

#Creates the meters widget but no entry box since it calculates for us
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#adds padding to each widget in our content frame
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

#puts focus on our entry widget so cursor will start there
feet_entry.focus()

#if user presses "return" key, it should call our calculate routine
root.bind("<Return>", calculate)

root.mainloop()