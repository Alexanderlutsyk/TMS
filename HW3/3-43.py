print('введи список')
a = input()
c = set(a)
z = None
for i in c:
    n = 0
    for u in c:
        if i > u:
            n += 1
    if n == len(c) - 1:
        z = i
        break
print(z)
