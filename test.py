

from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk



root = Tk()

root.geometry("400x400")
#^ width - heghit window :D


cmb = ttk.Combobox(root, width="10", values=("prova","ciao","come","stai"))
#cmb = Combobox

class TableDropDown(ttk.Combobox):
    def __init__(self, parent):
        self.current_table = Tk.StringVar() # create variable for table
        ttk.Combobox.__init__(self, parent)#  init widget
        self.config(textvariable = self.current_table, state = "readonly", values = ["Customers", "Pets", "Invoices", "Prices"])
        self.current(0) # index of values for current table
        self.place(x = 50, y = 50, anchor = "w") # place drop down box 

def checkcmbo():

    if cmb.get() == "prova":
         messagebox.showinfo("What user choose", "you choose prova")

    elif cmb.get() == "ciao":
        messagebox.showinfo("What user choose", "you choose ciao")

    elif cmb.get() == "come":
        messagebox.showinfo("What user choose", "you choose come")

    elif cmb.get() == "stai":
        messagebox.showinfo("What user choose", "you choose stai")

    elif cmb.get() == "":
        messagebox.showinfo("nothing to show!", "you have to be choose something")




cmb.place(relx="0.1",rely="0.1")

btn = ttk.Button(root, text="Get Value",command=checkcmbo)
btn.place(relx="0.5",rely="0.1")

root.mainloop()

