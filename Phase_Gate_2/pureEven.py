def even_numbers ():
	for numbers in range(1000, 3002, 2):
		if numbers % 2 == 0:
			print(numbers,end =",")
even_numbers ()