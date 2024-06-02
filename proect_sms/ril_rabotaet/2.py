import serial
import tkinter as tk

ser = serial.Serial('COM9', 9600) # Укажите порт, к которому подключена вторая Arduino

def receive_data():
    data = ser.readline().decode()
    label.config(text=data)

root = tk.Tk()
label = tk.Label(root, text="")
label.pack()
# receive_data()
root.mainloop()