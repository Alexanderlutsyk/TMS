mnoz = []
n = int(input())
d = 2
while d * d <= n:
	if n % d == 0:
		mnoz.append(d)
		n //= d
	else:
		d += 1
	if n > 1:
		mnoz.append(n)
print(mnoz)
