print("Загадайте в уме число от 1 до 5")
 
a = input("Твое число больше 3-х? (y/n) ")
 
if a == 'y':
	a = input("твое число 4? (y/n) ")
	if a == 'n':
		print("твое число 5")
else:
	a = input("твое число 1? (y/n) ")
	if a == 'n':
		a = input("твое число 2? (y/n) ")
		if a == 'n':
			print("твое число 3")
 
print("The end")


