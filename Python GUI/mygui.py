from tkinter import *
from tkinter import ttk



def calculate(*args):
    try:
        #calls variable "feet" from textvariable=feet from 1st widget
        value = float(rvFeet.get())
        finalCost = value * 10
        pitchText = f"""Thank you {customerName.get()}. Our Wash and Wax Package includes:
 
Cleaning roof and applying a protectant UV coating to plastics/seals to protect from cracking from the Sun 
Cleaning and protecting awnings 
Pressure-Washing exterior
Soaping and rinsing exterior
Manually applying a Polymer Sealant-Wax
Cleaning and protecting windows 
Cleaning Wheels and applying a shine to tires
**Please note that this package does NOT include Oxidation Removal**

For your vehicle, this would come to ${finalCost:.2f}. We're mostly booked up for the month but still have a couple of open appointments left. Is this something that you would be interested in?"""
        
        
        result_text.delete('1.0', END)      #Clears existing text
        result_text.insert('1.0', pitchText)    #Inserts pitchText --> result_text

    except ValueError:
        pass

root = Tk()             #sets up main application window
root.title("Customer Lister")    #sets title to "feet to meters"

#Next, we create a frame widget, which will hold the contents of our user interface.
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


#Creates the widget with feet with entry box
rvFeet = StringVar()
rvFeet_entry = ttk.Entry(mainframe, width=7, textvariable=rvFeet)
rvFeet_entry.grid(column=1, row=1, sticky=(W, E))

customerName = StringVar()
customerName_entry = ttk.Entry(mainframe, width=7, textvariable=customerName)
customerName_entry.grid(column=1, row=2, sticky=(W, E))

#Makes a pitchPre object
pitchPre=StringVar()

#Creates a text area widget and attaches it to mainframe
result_text = Text(mainframe, height=20, width=100)
result_text.grid(column=1, row=3, sticky=W)


ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=1, sticky=W)

ttk.Label(mainframe, text="Total Cost").grid(column=2, row=3, sticky=W)
ttk.Label(mainframe, text="RV in feet").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="Customer Name").grid(column=2, row=2, sticky=W)

#adds padding to each widget in our content frame
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

#puts focus on our entry widget so cursor will start there
rvFeet_entry.focus()

#if user presses "return" key, it should call our calculate routine
root.bind("<Return>", calculate)

root.mainloop()