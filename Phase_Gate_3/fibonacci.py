number = 6

zero = 0
one = 1

list = []

for numbers in range(1, number):
	total = zero + one
	list.insert(numbers, total)
	zero = one
	one = total

print(list)
	