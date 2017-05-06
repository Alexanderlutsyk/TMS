import calendar
print('введи год')
a = int(input())
if not calendar.isleap(a): # Модуль выводит Bool 
	print('не высокосный')
else:
	print("высокосный")
