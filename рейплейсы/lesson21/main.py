# f = open("file.txt", "w", encoding="utf-8")
# f.write("А, э")
# f.close()

# try:
#     f = open("file.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("Ыва")


# try:
#     x = int(input("Введите число:"))
#     print(10 / x)
# except ZeroDivisionError:
#     print("ы1")
# except ValueError:
#     print("ы2")
# else:
#     print("У тебя нет проблем")
# finally:
#     print("чел...")

# x = input("Введи имя друга: ")
# if x == "Антон":
#     raise NameError

# try:
#     f = open("file.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("Ыва")
# text = f.read().split()
# f.close()
# s = 0
# k = 0
# for number in text:
#     try:
#         s += int(number)
#     except ValueError:
#         print("найдено не число", number)
#         k += 1
#     return s / k
#
# try:
#     f = open("file.txt", "r", encoding="utf-8")
# except FileNotFoundError:

try:
    f = open("file.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("файл отсутствует")
text = f.readlines()
print(f"строк: {len(text)}")

full_text = " ".join(text).replace("\n", "")
print(full_text)
words = full_text.split()
print(f"слов:")


print(f"символов: ")
