import tkinter
from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk


okno = tk.Tk()
okno.geometry("1000x700")
okno.title("messeg")


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



# НАДПИСЬ ВВОДА НИКНЕЙМА_________________________________________________
nadpis_nik = tkinter.Label(okno, text='введите имя пользователя', font='Times 30')
nadpis_nik.grid()
# _______________________________________________________________________


# ВВОД ИМЯ ПОЛЬЗОВАТЕЛЯ__________________________________________________
vod_imya = tk.Entry(okno)
vod_imya.pack(padx=50,
              pady=200,
              row=10,
              column=10
              )
# _______________________________________________________________________



# НАДПИСЬ ВЫБОРА ПОРТА___________________________________________________
nadpis_com_port = tkinter.Label(okno, text='выберите порт', font='Times 30')
nadpis_com_port.grid()
# _______________________________________________________________________


# ВВОД СООБЩЕНИЯ_________________________________________________________
vod_soob = tk.Entry()
vod_soob.grid(padx=300,
              pady=300,
              row=98,
              column=87
              )
# _______________________________________________________________________


# button отправить, строка для ввода текста, ком порт надписьи ком порт выбор.
# вывод сооб с именем у другого пользователя и время











okno.mainloop()