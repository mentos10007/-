
#
# d = {"HLEB": 1000,
#      "MOLOKO": 1.5,
#      "CIROK": 47,
#      "ELKA": 50,
#      }
# for price in d.values():
#     print price
#     s += price
# print(s)
#
# phrase = "Маша, ты где? Маша загорает.".lower()
#
# print(phrase)
# spisok_nechisti = list("?.,!")
# phrase_cleared = ""
# d = {}
# for dop in phrase:
#     if dop not in spisok_nechisti:
#         phrase_cleared += dop
# l = phrase_cleared.split(" ")
# print(l)
# for dog in l:
#     if dog not in d:
#         d[dog] = 1
#     else:
#         d[dog] += 1
# print(d)
#
# maxi = max(d.values())
# for (key, values) in d.items():
#     if vaulues == maxi:
#         print(f"ключ:{key}, значение:{values}")

a = {
    "ключ5": 5,
    "ключ2": 2,
    "ключ3": 3,
    "ключ4": 4,
    "ключ1": 1,
}
a["ключ1"], a["ключ2"] =  a["ключ2"], a["ключ1"]


del a["ключ3"]


a["new_key"] = "new values"
print(a)