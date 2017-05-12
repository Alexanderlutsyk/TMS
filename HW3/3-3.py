import random

a = random.randint(1,10)
i = 1
k = int(input())
while i < 3:
	if k == a:
		print('угадал')
		break
	else:
		print('не угадал')
	k = int(input())
	i += 1
else:
	print(' повезет в другой раз, загаданное число',a)
