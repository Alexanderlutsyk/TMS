import random

a = '12345678910'
b = random.choice(a)
c = random.randint(0,100)
d = random.random()
i = random.uniform(-100,100)
j = random.triangular()
print(b,c,d,i,j, sep=( '\n'))
