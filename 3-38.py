import string

g = string.ascii_letters
h = string.digits 
while True:
	print('введи возраст')
	a = int(input())
	if a == h:
		a = int(a)
	print('введи имя')
	b = str(input())
	if b == g:
		b = str(b)
	print('введи фамидию')
	c = str(input())
	if c == g:
		c = str(c)
	print('введи вес')
	d = float(input())
	if d == h:
		d=float(d)
	print('введи рост')
	f = float(input())
	if f == h:
		f = float(f)
	break
print(a,b,c,d,f) 
