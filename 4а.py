import calendar
print('введи год')
a = int(input())
if not calendar.isleap(a):
	print('не высокосный')
else:
	print("высокосный")
