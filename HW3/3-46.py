print('введи текст который мы закодируем')
a = input()
i = 0
l =[]
l2 =[]
for i in a:
	c = ord(i) + 3
	l.append(chr(c))
l=''.join(l)
print(l)
for k in l:
	d = ord(k) - 3
	l2.append(chr(d))
l2 = ''.join(l2)
print(l2)

