import tkinter
from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk


okno = tk.Tk()
okno.geometry("1000x700")
okno.title("mesag")


# ИЗОБРАЖЕНИЕ_____________________________________________________________
# izob_polzovat = Image.open("")
#
# izob_polzovat_tk = ImageTk.PhotoImage(izob_polzovat)
#
# izob_label = tk.Label(okno, izob_polzovat=izob_polzovat_tk)
# izob_label.izob_polzovat = izob_polzovat_tk
#
# izob_label.pack()
# _______________________________________________________________________



lab = Label(okno, text="введите имя")
lab.pack()



# text_vod_imya = Text()
# text_vod_imya.pack(padx=50,
#                    pady=40
#                    )





# ВВОД ИМЯ ПОЛЬЗОВАТЕЛЯ__________________________________________________
vod_imya = tk.Entry(okno)
vod_imya.pack(padx=50,
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












https://metanit.com/python/tkinter/3.1.php

okno.mainloop()