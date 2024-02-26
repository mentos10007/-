# import serial
import time
from tkinter import*

from random import randint
root = Tk()
root.geometry("500x500")
#
# arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

# label =

def outText_1():
    arduino.write(bytes('1', 'utf-8'))
def outText_2():
    arduino.write(bytes("5", 'utf-8'))

btn_vkl = Button(root,
                 text="вкл",
                 font='Times 20',
                 width=0,
                 height=0,
                 command=outText_1
)
btn_vkl.place(x=50, y=150)

btn_vikl = Button(root,
                  text="выкл",
                  font='Times 20',
                  width=0,
                  height=0,
                 command=outText_2
)

def outText_5():
  btn_vikl.configure(text="5")



btn_vikl.place(x=150, y=150)




variable = StringVar(root)
variable.set("выбрать порт")
opt = OptionMenu(
    root, variable, *[
        arduino
    ]
)
opt.config(
    width=19, font=('Helvetica')
)
opt.place(x=15, y=70)



root.mainloop()

