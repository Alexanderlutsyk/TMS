import random

print('''Игра камень ножницы бумага.
условное обозначение:	
	1-камень
	2-ножницы
	3-бумага
''')
a = 0
i = 0


while True:
	user = int(input('Введи соответствующее число \n'))
	if user ==1:
		print('ты выбрал камень')
	elif user ==2:
		print('ты выбрал ножницы')
	elif user ==3:
		print('ты выбрал буагу')
	else:
		print('вы ввели неправильное значение')
	comp = random.randint(1,3)
	if comp ==1:
		print('кампутер выбрал камень')
	elif comp ==2:
		print('кампутер выбрал ножницы')
	elif comp ==3:
		print('кампутер выбрал буагу')
	
	if comp == user:
		print('ничья')
	if comp == 1 and user == 2 or comp == 2 and user == 3 or comp == 3 and user == 1:
		print('кампутер выиграл')
		i+=1
			
		
		
	if comp ==2 and user ==1 or comp==3 and user ==2 or comp == 1 and user == 3:
		print('ты сделал')
		a+=1	
		
	if i==2 or a==2:
		break
		
		
	
