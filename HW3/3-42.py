
s = float(input())

x = 1.0
while abs(x * x - s) > 0.0000001:
    x = (x * x + s) / 2. / x  
print (x)
