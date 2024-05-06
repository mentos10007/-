import serial
import tkinter as tk

# Инициализация соединения с Arduino
ser = serial.Serial('COM8', 9600)  # Укажит
# е COM порт, к которому подключена первая Arduino

# Функция для отправки сообщения на Arduino
def send_to_arduino(message):
    ser.write(message.encode('utf-8'))

# Создание графического интерфейса для ввода сообщения
root = tk.Tk()
root.title("Отправка сообщения на Arduino")

entry = tk.Entry(root)
entry.pack()

def send_message():
    message = entry.get()
    send_to_arduino(message)

button = tk.Button(root, text="Отправить", command=send_message)
button.pack()

root.mainloop()