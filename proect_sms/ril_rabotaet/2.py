
import serial
from nrf24 import NRF24
import socket
import struct
import threading

def listen(sock):
    while True:
        data = sock.recv(64)
        message = struct.unpack('{}s'.format(64 - len(struct.calcsize('I'))) , data)
        print("Received message: {}".format(message[0].decode()))

ser = serial.Serial('/dev/ttyACM0', 9600)
sock = socket.socket(socket.AF_SPI_NRF24, socket.SOCK_STREAM)
sock.bind(NRF24.ComplexPipeline(0x30, 16))
threading.Thread(target=listen, args=(sock,)).start()
try:
    while True:
        line = ser.readline().decode().strip()
        sock.send(struct.pack('I{}s'.format(len(line)), line.encode()))
except KeyboardInterrupt:
    pass
finally:
    sock.close()
    ser.close()