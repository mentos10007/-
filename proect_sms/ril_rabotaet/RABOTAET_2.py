import tkinter as tk
import serial


root = tk.Tk()
root.title("Мессенджер")
# root.geometry('600x400')


# Подключение к порту Arduino
ser = serial.Serial('COM8', 9600)  # Укажите правильный порт


def send_message():
    message = message_entry.get()    # Отправка сообщения на Arduino для передачи
    ser.write(message.encode())


message_entry = tk.Entry(root, width=50)
message_entry.pack()
send_button = tk.Button(root, text="Отправить", command=send_message)
send_button.pack()
message_get = tk.Entry(root, width=100)
message_get.pack()

#
# def get_message():
#     message = message_get.get()    # Получение сообщения на Arduino для передачи
#     ser.read(message.encode())
#
# get_button = tk.Button(root, text="Получить", command=get_message)
# get_button.pack()
#
#

root.mainloop()
