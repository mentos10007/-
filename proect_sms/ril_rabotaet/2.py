import serial

ser = serial.Serial('COM10', 9600)  # Укажите порт и скорость соединения

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print(data)