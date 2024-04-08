import tkinter as tk
from datetime import datetime
from nRF24 import NRF24

radio = NRF24(22, 0)
pipes = [b'1Node', b'2Node']

radio.begin(0, 0, "P8_23", "P8_24")  # инициализация с пинами CE, CSN, и установкой пинов для прерываний

def send_message():
    name = name_entry.get()
    message = message_entry.get()
    timestamp = datetime.now().strftime("%H:%M:%S")
    data = f"{name}: {message} [{timestamp}]"
    radio.openWritingPipe(pipes[1])
    radio.write(data.encode('utf-8'))
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