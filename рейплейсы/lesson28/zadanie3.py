from tkinter import *

def italic(ziga):
    lab['font'] = lab['font'].replace(' italic', '')
    lab["font"] += ' italic'

def bold(ziga):
    lab['font'] = lab['font'].replace(' bold', '')
    lab["font"] += ' bold'

def base(ziga):
    lab['font'] = lab['font'].replace(' bold', '').replace('italic', '')




chto = Tk()
chto.geometry("200x100")
chto.title("pon")
chto["bg"] = "lavender"

lab = Label(chto, text="///")

lab["font"] = "Arial 15"

lab.pack()



sf = lab.bind("<Button-1>", italic)
sff = lab.bind("<Button-3>", base)
sfff = lab.bind("<Double-Button-3>", bold)

















chto.mainloop()



# lab["font"] = "Arial, 15, bold"