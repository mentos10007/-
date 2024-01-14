from tkinter import*
from random import randint
root = Tk()
root.geometry("500x500")

btn_vkl = Button(root,
             text="вкл",
             font='Times 20',
             width=10,
             height=0,
)
btn_vkl.place(x=150, y=150)

btn_vikl = Button(root,
                  text="выкл",
                  font='Times 20',
                  width=10,
                  height=0,
)

btn_vikl.place(x=300, y=150)

root.mainloop()