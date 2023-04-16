from tkinter import *


chto = Tk()
chto.geometry("200x500")
chto.title("pon")
chto["bg"] = "lavender"

text = Label(chto, text="голубой")
text.pack()

txt = Text(chto,
           width=20,
           height=5)
txt.pack()

lab_red = Button(chto,
          bg="red",
          height=3,
          width=25)
lab_red.pack()

lab_yellow = Button(chto,
          bg="yellow",
          height=3,
          width=25)
lab_yellow.pack()

lab_zeleni = Button(chto,
          bg="green",
          height=3,
          width=25)
lab_zeleni.pack()

lab_goluboi = Button(chto,
          bg="blue",
          height=3,
          width=25)
lab_goluboi.pack()

lab_purp = Button(chto,
          bg="purple",
          height=3,
          width=25)
lab_purp.pack()


chto.mainloop()