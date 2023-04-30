from tkinter import*
root = Tk()
root.geometry("500x500")

# # # list = ["первый", "второй", "пятндацать"]
# # # lstbox = Listbox(root)
# # #
# # # lstbox.pack
# # #
# # # #1 способ через цикл и вставку
# # # for elem in lst:
# # #     lstbox.insert(END, elem)
# #
# # lst = ["первый", "второй", "пятндацать"]
# # lst_tk = StringVar(value=lst)
# # lstbox = Listbox(root, listvariable=lst_tk, selectmode=EXTENDED)
# # lstbox.pack
# #
# # def fu():
# #     for ind in lstbox.curselection():
# #         print(lst[ind])
# #
# # lstbox.bind('<<ListboxSelect>>', fu)
# #
# # btn = Button(root, text="вывести", command=fu)
# # btn.pack()
# # -----masage---
# # from tkinter import messagebox*
# # messagebox.showinfo()
# # messagebox.showerror()
# # messagebox.showwarning()
#
#
# # # # pack()------
# # # btn = Button(root, text="вывести")
# # # # btn.pack(anchor=SW, expand=True)
# # # btn.pack(fill=BOTH, expend=True)
# # btn1 = Button (root, text="text")
# # btn1.pack(pady=50)
# # btn1 = Button (root, text="text")
# # btn1.pack(pady=50)
#
# # -----.grid()-----
# btn1 = Button(root, text="text")
# btn1.grid(column=2, row=10, rowspawn=5, sticky=NS)
# btn2 = Button(root, text="text")
# btn2.grid(column=0, row=5, columnspawn=5, sticky=EW)
# btn=Button(root)
# btn.place(x=2, y=2)

#
# -----after-----
# def fu():
#     print("print")
#     root.after(1000, fu)
#
#
#
# root.after(3000, fu)

entry = (root, show="*")














root.mainloop()