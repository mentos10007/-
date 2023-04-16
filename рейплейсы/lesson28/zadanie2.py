from tkinter import *

def h_el_lo(ziga):
    # приём и удаление из entry
    massage = ent.get()
    ent.delete(0, END)
    print(massage)

    # приём и удаление из text
    massage2 = cp.get(0.0, END)
    cp.delete(0.0, END)
    print(massage2)

chto = Tk()
chto.geometry("200x300")
chto.title("pon")
chto["bg"] = "lavender"

text = Label(chto, text="ваш адрес:")
text.pack()

ent = Entry(chto,
           width=20,)
ent.pack()

pon = Label(chto, text="коментарий:")
pon.pack()

cp = Text(chto,
           width=20,
           height=5)
cp.pack()

btn = Button(chto, text="отправить",
             bg="lightblue",
             font=20,
             height=2,
             width=10)
btn.pack()

btn.bind("<Button-1>", h_el_lo)



chto.mainloop()