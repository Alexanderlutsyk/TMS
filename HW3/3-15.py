lst = [1,[2,3],[4],[[5,6]]]
lst= list(lst)
lst1 = []
for a in lst:
	lst1.append(lst.pop(a))
	
print(lst1)

	
