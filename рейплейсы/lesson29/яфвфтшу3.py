from tkinter import*
def activation():
    if cb_val.get() == True:
        b["text"] = "активна"
        b["state"] = "normal"
    else:
        b["text"] = "не активна"
        b["state"] = "disabled"

win = Tk()
cb_val = BooleanVar()
cb = Checkbutton(win, text="активна", variable=cb_val, onvalue=True,
                 offvalue=False, command=activation)

cb.pack()

b = Button(win, text="не активна", state="disabled")
b.pack()
win.mainloop()