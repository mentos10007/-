from tkinter import*
win = Tk()
win.geometry("1000x4000")

def get_scala(val):
    print(pon.get())
    print(val)
# cb_val = BooleanVar()
# cb = Checkbutton(win,
#                 text="putin sila",
#                 command=get_cb,
#                 variable=cb_val,
#                 onvalue=True,
#                 offvalue=False)
# cb.pack()

# cb_val = IntVar()
# cb = Radiobutton(win,
#                 text="putin sila",
#                 command=get_cb,
#                 variable=cb_val,
#                 value=1)
# cb.pack()
#
# cb1_val = IntVar()
# cb1 = Radiobutton(win,
#                 text="putin sila",
#                 command=get_cb,
#                 variable=cb1_val,
#                 value=1)
# cb1.pack()

# scala = Scale(win,
#               from_=50,
#               to=120,
#               orient=HORIZONTAL,
#               length=300,  #длина полосы в пикселях
#               tickinterval=10,  #разметка
#               resolution=10,  #шаг
#               command=get_scala
#               )
# scala.pack()

# img = PhotoImage(file="png-clipart-potato-potato.png")
# img_small = img.subsample(1, 10)  #.subsample =  уменьшение
# img_big = img.zoom(3, 3)  #.zoom =  увеличивает
# img_poltora = img.subsample(3, 3).zoom(2, 2)
# lab = Label(win, image=img_poltora)
# lab.pack()

# Label(win, text="pon.", bg = "pink").pack()
# Label(win, text="tam.", bg = "blue").pack(pady=15, ipady=20)
lab = Label(win, text="...")
lab.pack()

ent = Entry(win)
ent.pack()

win.mainloop()