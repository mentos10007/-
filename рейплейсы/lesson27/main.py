# # import math
# #
# # zemlekopi = int(input("> "))
# # print(math.ceil(zemlekopi))
# #
# # c1 = input("Введите первый цвет:")
# # c2 = input("Введите второй цвет:")
# # c = ("красный", "желтый", "синий")
# #
# # if c1 not in c or c2 not in c:
# #     print("Один из основных цветов введён неверно!")
# # elif c1 == c[0] and c2 == c[1] or c2 == c[1] and c2 == c[0]
# #     print("оранжевый")
# # elif c1 == c[0] and c2 == c[1] or c2 == c[1] and c2 == c[0]
# #     print("оранжевый")
# # elif c1 == c[0] and c2 == c[1] or c2 == c[1] and c2 == c[0]
# #     print("фиол")
#
# # first_lesson = float("введите начало урока")
# # len_lesson = int(input("Ваедите длительность урока"))
# # break_time = int("введите длитеьность перемены")
# # lesson_count = int(input("введите колво уроков"))
# # hours, minutes = first_lesson.split(":")
# # hours, minutes = int(hours), int(minutes)
# # time = hours*60 + minutes
# # for i in range(lesson_count):
# #     print(f"{i+1} урок: ", end="")
# #     print(f"{str(hours).rjust(2, '0')}:{str(minutes)}")
#
# col_zomb = int(input("кол во зомби к началу эпидемии:"))
# vozm_zaraz =int(input("кол во возможных зараженых людей"))
# day = int(input("на какой день делается расчет:"))
# print(f"1 день: {col_zomb}")
# for i in range(2, day + 1):
#     o = col_zomb = col_zomb * vozm_zaraz + col_zomb
#     col_zomb = o
#     print(f"{i} день:{col_zomb+vozm_zaraz+col_zomb}")
#     pastebin.com/nqVi7gde
from user import User

u1 = User(fam="Смирнов", im="Антон", log="smir-ant", pas="12345")
u2 = User()

# print(u1.login)
# print(u2.login)
#
# print(u1.familiya)
# print(u2.familiya)

users = [u1, u2]
i = input("введите логин")
p = input("введите пороль")
for chelovek in users:
    print("авторизация успешна")
    current = chelovek