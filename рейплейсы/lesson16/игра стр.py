# import time
# import random
#
# print("Время проверить твою ловкость и скорость и понять, "
#       "кто самый быстрый стрелок на западе! Когда увидишь 'СТРЕЛЯЙ', "
#       "у тебя будет 0.3 секунды чтобы нажать Enter. "
#       "Но если ты нажмёшь Enter раньше, то ты проиграл.")
# input("нажми enter чтобы начать")
# input("время пострелять")
#
#
# time.sleep(random.randint(1, 5))
#
# start = time.time()
# input("бум")
# end = time.time()
# delta = end - start
# print(f"{delta}сек")
# if delta < 0.01:
#     print("фальшстарт")
#
# elif delta > 0.3:
#     print("ммм")
# else:
#     print("харош")