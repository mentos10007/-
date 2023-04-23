from tkinter import*
win = Tk()
win.geometry("1000x4000")

def knopka(event):
    pass

lab = Label(win, text="text")
lab.pack()

cb_val = IntVar()
cb = Radiobutton(win)
cb.pack()

cb1_val = IntVar()
cb1 = Radiobutton(win)
cb1.pack()



win.mainloop()