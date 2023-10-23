import random
a = []
while len(a) != 9:
    a.append(random.randint(0, 10))
for i in a:
    if a.count(i) == 1:
        pass
    else:
        a.pop()
print(a)