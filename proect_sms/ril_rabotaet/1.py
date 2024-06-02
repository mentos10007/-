import tkinter as tk
import serial

# Инициализация последовательного порта
ser = serial.Serial('COM1', 9600)  # Укажите порт и скорость

# Функция отправки текста на Arduino
def send_text():
    text = entry.get()
    ser.write(text.encode())

# Функция для приема текста от Arduino
def receive_text():
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        label.config(text=data)

# Создание графического интерфейса Tkinter
root = tk.Tk()
root.title("Arduino Serial Communication")

entry = tk.Entry(root)
entry.pack()

send_button = tk.Button(root, text="Send", command=send_text)
send_button.pack()

label = tk.Label(root, text="")
label.pack()

# Чтение данных со стороны Arduino
root.after(100, receive_text)

root.mainloop()