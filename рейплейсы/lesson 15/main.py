# def hellow_orld():   # обьявление функции
#     print("hello_world")
#
# hellow_orld()
#
# def plus(number1, chislo2):
#     result = number1 + chislo2
#     return result
#
# plus(5, 3)    #результат записан в переменую. вызщв функции с аргументом.
# plus(chislo2=3, number1=23)

# def is_anton(name):
#     if name == "Антон":
#         return True
#
# if is_anton("Богдан"):
#     print("это антон")
# else:
#     print("это не антон")





# def check(list):
#     sort = sorted(list)
#     if list == sort:
#         return True
#
# list = [1,2,3,4,5]
# if check(list):
#     print("список не отсортирован")
# else:
#     print("список отсортирован")


# задание 2

# def find_longest(list):
#     spisok2 = []
#     for i in list:
#         spisok2.append(len(i))
#     maxy = max(spisok2)
#     ind = spisok2.index(maxy)
#     return list[ind], spisok2[ind]
# spisok = ["баран","дом", "дед"]
#
# print(find_longest(spisok))

# def min_max(chisla):
#     minimi = 0
#     maxim = 0
#     for i in chisla:
#         if i > maxim:
#             maxim = i
#         elif i < mini:
#             mini = i
#         return maxim, mani
#
#
#
# def is_prime(vnutr):
#     for i in range(2, vnutr+1):
#         if i == vnutr:
#             return True
#         if vnutr % i == 0:
#             break
#
# if is_prime(524):
#     print("DA")
# else:
#     print("NET")
#
#
#
#
#
#
# def join(spisock:list, razdelitel:str)->str:
#     resick = ""
#     for i in spisock:
#         resick += i + razdelitel
#     return resick
#
# listick = ["da", "net", "omlet"]
# print(join(listick, ">"))
#
# def factorial(chislo):
#     x = 1
#     for i in range(2, chislo):
#         x *= i
#     return x
#
#
#
#
# print(factorial(15))
