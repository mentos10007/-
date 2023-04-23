

from tkinter import*
win = Tk()
win.geometry("1000x4000")

def knopka(val):
    massage = ent.get()
    lab["text"] = massage

lab = Label(win, text="...")
lab.pack()

ent = Entry(win)
ent.bind("<Button-3>", knopka)
ent.insert(0, "впиши и ПКМ")
ent.pack()

win.mainloop()