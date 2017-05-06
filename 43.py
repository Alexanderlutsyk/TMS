a = int(input())
if (a / 60) < 24:
	d = 0
	h = a % 60
	m = a // 60
	print(d,h,m)
if (a / 60) > 24:
	d = (a / 60) / 24
	h = (a % 60) /24
	m =  a // 60
	print(d,h,m)

