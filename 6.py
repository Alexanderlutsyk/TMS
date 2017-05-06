print('введи число')
a = int(input())
if a % 3 ==0 and a % 5 == 0 :
	print('Foo Bar')
elif a % 5 == 0:
	print("Bar")
elif a % 3 == 0:
	print('Foo')
elif a % 5 != 0 or a % 3 != 0:
	print('введеное число не делится ')
