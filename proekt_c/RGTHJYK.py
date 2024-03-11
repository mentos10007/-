

from tkinter import*
from random import randint
root = Tk()
root.geometry("500x500")

btn_vkl = Button(root,
                 text="вкл",
                 font='Times 20',
                 width=0,
                 height=0,
)
btn_vkl.place(x=50, y=150)

btn_vikl = Button(root,
                  text="выкл",
                  font='Times 20',
                  width=0,
                  height=0,
)

btn_vikl.place(x=150, y=150)




variable = StringVar(root)
variable.set("выбрать порт")
opt = OptionMenu(
    root, variable, *[
        "", "fsmsf", "dsfsf"
    ]
)
opt.config(
    width=19, font=('Helvetica')
)
opt.place(x=15, y=70)


root.mainloop()


#
# import serial
# import time
# arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
# def write_read(x):
# 	   arduino.write(bytes(x, 'utf-8'))
# 	   time.sleep(0.05)
# 	   data = arduino.readline()
# 	   return data
# while True:
# 	   num = input("Enter a number: ") # Taking input from user
# 	   value = write_read(num)
# 	   print(value) # printing the value
#
#
#
#
#
# int x;
# void setup() {
# 	Serial.begin(115200);
# 	Serial.setTimeout(1);
# }
# void loop() {
# 	while (!Serial.available());
# 	x = Serial.readString().toInt();
# 	Serial.print(x + 5);
# }






# #define LED 13
# #define BUT 2
#
#
# void setup() {
#   pinMode(BUT, INPUT_PULLUP);
#   pinMode(LED, OUTPUT);
#   Serial.begin(115200);
# }
#
# void loop() {
#   if (Serial.available()) {
#     int a = Serial.readString().toInt();
#     if (a == 1) {
#       digitalWrite(LED, HIGH);
#     } else if (a == 5) {
#       digitalWrite(LED, LOW);
#     }
#   }
#
# }
