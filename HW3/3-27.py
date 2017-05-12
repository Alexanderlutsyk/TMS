import random

print('количество спичек в коробке')
n = random.randint(20,40)
print(n)
print('введи не больше скольки спичек можно вытянуть за раз')
q = int(input())
print('введи сколько вытягиваешь')
a = int(input())
n = n - a
while n > 0:
	if n > 0:
		print('теперь тяну я')
		b = random.randint(1,q)
		print(b)
		n = n-b
		print(n)
	if n <= 0:
		print('я проиграл')
	if n > 0:
		print('тяни ты')
		a = int(input())
		n = n-a
	if n <= 0:
		print('ты проиграл')
	
	
	
