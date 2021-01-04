#  1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
	if i < 5:
		print(i, end=" ")


print("\n\n")


#  2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = [i for i in a if i < 5]
for i in a:
	print(i, end=" ")


print("\n\n")


#  3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = list(filter(lambda x: True if x < 5 else False, a))
for i in a:
	print(i, end=" ")
