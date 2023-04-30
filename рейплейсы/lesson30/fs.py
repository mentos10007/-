from tkinter import*
from random import randint
root = Tk()
root.geometry("500x500")

# label = Label(root, text="логин")
# label.grid(column=0, row=0)
# label1 = Label(root, text="пароль")
# label1.grid(column=0, row=1)
#
# entry = Entry(root)
# entry.grid(column=1, row=0)
# entry1 = Entry(root, show="*")
# entry1.grid(column=1, row=1)
#
# btn = Button(root, text="авторизация")
# btn.grid(column=1, row=2, sticky=E)


def fu(arms):
    btn.place(x=randint(0,450), y=randint(0,450))
btn = Button(root, text="ПОЙМАЙ МЕНЯ!!!")
btn.place(x=10, y=10)
btn.bind("<Enter>", fu)











root.mainloop()