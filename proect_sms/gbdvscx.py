
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.filedialog


def send_message():
    message = message_entry.get()
    chat_log.config(state=tk.NORMAL)
    username = username_entry.get()  # Получаем имя из поля ввода
    if message and username:  # Проверяем, что и сообщение, и имя были введены
        chat_log.insert('end', username + ": " + message + "\n")
    else:
        chat_log.insert('end', "Вы должны ввести имя и сообщение\n")
    message_entry.delete(0, tk.END)
    chat_log.config(state=tk.DISABLED)

# def set_profile_picture():
#     file_path = tk.filedialog.askopenfilename()
#     image = Image.open(file_path)
#     image = image.resize((100, 100), Image.ANTIALIAS)
#     photo = ImageTk.PhotoImage(image)
#     profile_picture_label.config(image=photo)
#     profile_picture_label.image = photo

# Создание основного окна
root = tk.Tk()
root.title("Чат")

# Создание виджетов
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

username_label = tk.Label(left_frame, text="Введите ваше имя:")
username_entry = tk.Entry(left_frame)
username_label.pack()
username_entry.pack()

# profile_picture_button = tk.Button(left_frame, text="Выбрать изображение профиля", command=set_profile_picture)
# profile_picture_button.pack()
#
# image_path = "default_profile_image.jpg"  # Путь к изображению профиля по умолчанию
# default_image = Image.open(image_path)
# default_image = default_image.resize((100, 100), Image.ANTIALIAS)
# default_photo = ImageTk.PhotoImage(default_image)
# profile_picture_label = tk.Label(left_frame, image=default_photo)
# profile_picture_label.pack()

message_entry = tk.Entry(right_frame)
send_button = tk.Button(right_frame, text="Отправить", command=send_message)
chat_log = tk.Text(right_frame, state=tk.DISABLED)

message_entry.pack(side=tk.LEFT)
send_button.pack(side=tk.LEFT, padx=5)
chat_log.pack(side=tk.LEFT, padx=5)

# Запуск основного цикла обработки событий
root.mainloop()