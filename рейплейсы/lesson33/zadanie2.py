n = int(input())
stones = 0
string = input()
prev = string[0]
for i in string[1:]:
    if i == prev:
        stones += 1
    prev = i
print(stones)