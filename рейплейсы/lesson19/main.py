alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_ru2 = alphabet[::-1]
alphabet2 = alphabet[::-1]
phrase = input("").upper()
phrase2 = ''
for i in phrase:
    if i.upper() in alphabet_ru:
        if i.upper():
            indx = alphabet_ru.index(i)
            bukva = alphabet_ru2[indx]
    if i not in alphabet:
        phrase2 += i
    else:
        indx = alphabet.index(i)
        bukva = alphabet2[indx]
        phrase2 = phrase2 + bukva
print(phrase2)