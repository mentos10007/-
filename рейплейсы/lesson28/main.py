from tkinter import *

def h_el_lo(ziga):
    massage = ent.get()
    ent.delete(0, END)
    print(massage)

root = Tk()
root.geometry("1000x4000")
root.title("dota")
root["bg"] = "lavender"

lab = Label(root, text="dota 2 вышла на андройд")
lab.pack()
# lab["background"] = "black"
# lab["foreground"] = "red"
lab["bg"] = "black"
lab["fg"] = "red"
# lab["font"] = 50 #pasmer shrifta
# lab["font"] = "arial 20 bold"
lab["font"] = ("arial black",
               20,
               "bold",
               "italic",
               "overstrike",
               "underline")
lab["height"] = 5
lab["width"] = 20
# 1-беск= темнее



btn = Button(root, text="СКАЧАТЬ ДОТУ НА АНДРОЙД",
             bg="red",
             font=20,
             height=5,
             width=40)

# command=h_el_lo

btn.pack()
btn.bind("<Button-1>", h_el_lo)
#Button-1 = ЛКМ
#Button-3 = ПКМ
#Double-Button-3 = ПКМ

ent = Entry(root,
            width=20,
            font=20,
            bd=10)
# borderwidth=10
ent.pack()


txt = Text(root,
           width=20,
           height=20,
           wrap="word")

# wrap:
# word - perenos po slovam
# char - po simvolam
# none - bes perenosa
txt.pack()

root.mainloop()