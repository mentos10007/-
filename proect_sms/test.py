# import tkinter
# from tkinter import*
# from tkinter import ttk
# import tkinter as tk
#
#
#
# okno = tk.Tk()
# okno.geometry("1000x700")
# okno.title("mesag")
#



import tkinter as tk


# name = "fkkf"

class MessengerApp:
    def init(self, root):
        self.root = root
        self.root.title("Messenger App")

        self.message_history = tk.Text(root, height=10, width=50)
        self.message_history.pack()

        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.pack()

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        message_text = self.message_entry.get()
        self.message_entry.delete(0, "end")
        self.message_history.insert("end", message_text + "\n")
#
# if name == "main":
#     root = tk.Tk()
#     app = MessengerApp(root)
#     root.mainloop()



# okno.mainloop()
