import tkinter as tk
from datetime import datetime
from RF24 import RF24, RF24_PA_LOW

# Инициализация радио модуля RF24
radio = RF24(22, 0)  # указываем пины CE и CSN
radio.begin()
radio.setPALevel(RF24_PA_LOW)
radio.openWritingPipe(b"1Node")
radio.openReadingPipe(1, b"2Node")

# Создание графического интерфейса
def send_message():
    name = name_entry.get()
    message = message_entry.get()
    timestamp = datetime.now().strftime("%H:%M:%S")
    data = f"{name}: {message} [{timestamp}]"
    radio.startWrite(data.encode('utf-8'))
    print(f"Сообщение отправлено: {data}")

root = tk.Tk()
root.title("Мессенджер")

name_label = tk.Label(root, text="Введите ваше имя:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

message_label = tk.Label(root, text="Введите ваше сообщение:")
message_label.pack()

message_entry = tk.Entry(root)
message_entry.pack()

send_button = tk.Button(root, text="Отправить", command=send_message)
send_button.pack()

root.mainloop()