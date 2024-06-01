import tkinter as tk
import serial

# Подключение к порту Arduino
ser = serial.Serial('COM7', 9600)  # Укажите правильный порт


root = tk.Tk()
root.title("Мессенджер")
message_entry = tk.Entry(root, width=50)
message_entry.pack()



def send_message():
    message = message_entry.get()    # Отправка сообщения на Arduino для передачи
    ser.write(message.encode())
    # response = ser.readline()
    # # Декодируем ответ из байтов в строку с использованием UTF-8
    # decoded_response = response.decode('utf-8')
    # print(decoded_response)


send_button = tk.Button(root, text="Отправить", command=send_message)
send_button.pack()

root.mainloop()
