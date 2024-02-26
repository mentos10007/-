import tkinter
from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk


okno = tk.Tk()
okno.geometry("1000x700")



# ИЗОБРАЖЕНИЕ_____________________________________________________________
izob_polzovat = Image.open("")

izob_polzovat_tk = ImageTk.PhotoImage(izob_polzovat)

izob_label = tk.Label(okno, izob_polzovat=izob_polzovat_tk)
izob_label.izob_polzovat = izob_polzovat_tk

izob_label.pack()
# _______________________________________________________________________




# ВВОД ИМЯ ПОЛЬЗОВАТЕЛЯ__________________________________________________
vod_imya = tk.Entry(okno)
vod_imya.grid(
                 padx=50,
                 pady=200,
                 row=10,
                 column=10
                 )
# _______________________________________________________________________




# ВВОД СООБЩЕНИЯ_________________________________________________________
vod_soob = tk.Entry()
vod_soob.grid(padx=300,
              pady=300,
              row=98,
              column=87
              )
# _______________________________________________________________________














okno.mainloop()