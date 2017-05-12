import random

a = random.randint(0,100)
k = int(input())
for i in range(100):
    if a == k:
        print('угадал')
        break
    if a < k:
        print('меньше')
    else:
        print('больше')
    k = int(input())
