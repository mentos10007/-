import tkinter
from tkinter import*
from tkinter import ttk
import tkinter as tk



okno = tk.Tk()
okno.geometry("1000x700")
okno.title("mesag")



# text_vod_imya = Text()
# tkinter.Text(okno, font="Courier 20", bg="Black", fg="red")
# text_vod_imya.pack()



nadpis_nik = tkinter.Label(okno, text='Hello word', font='Times 30')
nadpis_nik.grid()




okno.mainloop()
