import serial
import tkinter as tk

ser = serial.Serial('COM10', 9600) # Укажите порт, к которому подключена первая Arduino

def send_data():
    data = entry.get()
    ser.write(data.encode())

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Send", command=send_data)
button.pack()
root.mainloop()