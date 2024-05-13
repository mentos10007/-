import tkinter as tk
import serial
def send_message():
    message = message_entry.get()    # Отправка сообщения на Arduino для передачи
    ser.write(message.encode())

def get_message():
    message = message_get.get()    # Получение сообщения на Arduino для передачи
    ser.read(message.encode())

root = tk.Tk()
root.title("Мессенджер")
message_entry = tk.Entry(root, width=50)
message_entry.pack()
send_button = tk.Button(root, text="Отправить", command=send_message)
send_button.pack()
message_get = tk.Entry(root, width=100)
message_get.pack()
get_button = tk.Button(root, text="Получить", command=get_message)
get_button.pack()
# Подключение к порту Arduino
ser = serial.Serial('COM4', 9600)  # Укажите правильный порт
root.mainloop()
