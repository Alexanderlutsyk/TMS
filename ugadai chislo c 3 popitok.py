import random

a = random.randint(1,10)
print('угадай число от 1 до 10 за 3 попытки, введи число',a)
k = int(input())
i = 1
while i<3:
    if k == a:
        print('угадал')
        break
    else:
        print('попробуй еще раз')
        k = int(input())
    i += 1
else:
	print('попыток не осталось, загаданно число ',a)
    	
