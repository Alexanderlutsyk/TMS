import random

a = int(input())
lst = []
lst1 = []
for i in range(100):
	x = random.randint(1,100)
	lst.append(x)
for k in lst:
	if k > a:
		lst1.append(k)
print(lst1)
