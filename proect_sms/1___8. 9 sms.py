
import tkinter as tk
import serial

# Установите правильный COM порт и скорость передачи данных
ser = serial.Serial('COM1', 9600)

def send_message():
    name = entry_name.get()
    message = entry_message.get()
    full_message = f"{name}: {message}"
    ser.write(full_message.encode())
    entry_message.delete(0, tk.END)

def receive_message():
    while ser.in_waiting:
        message = ser.readline().decode().strip()
        print(message)
        text_box.insert(tk.END, message + '\n')

# Создание графического интерфейса
root = tk.Tk()
root.title("Мессенджер")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_name = tk.Label(frame, text="Имя:")
label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_message = tk.Label(frame, text="Сообщение:")
label_message.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

entry_message = tk.Entry(frame)
entry_message.grid(row=1, column=1, padx=5, pady=5)

send_button = tk.Button(frame, text="Отправить", command=send_message)
send_button.grid(row=2, columnspan=2, padx=5, pady=5)

text_box = tk.Text(root)
text_box.pack(padx=10, pady=10)

receive_button = tk.Button(root, text="Получить сообщения", command=receive_message)
receive_button.pack(padx=10, pady=5)

root.mainloop()