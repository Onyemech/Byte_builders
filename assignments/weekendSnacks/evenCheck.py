def evenCheck (numbers):
	numbers = [2, 3, 7, 6, 8]

	for num in numbers:
		if numbers[num] % 2 == 0:
			print(" " , num)

evenCheck ([2, 3, 7, 6, 8])