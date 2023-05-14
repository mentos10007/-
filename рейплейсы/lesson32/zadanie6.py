from string import ascii_lowercase
alphabet = ascii_lowercase
vihod = 0
a = input()
b = input()

for i in range(len(a)):
    if a[i] != b[i]:
        n = alphabet.index(a[i])
        f = alphabet.index(b[i])
        if n < f:
            vihod = -1
        else:
            vihod = 1
        break
print(vihod)