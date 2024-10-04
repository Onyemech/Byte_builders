def largest (list_of_numbers):

	largest = list_of_numbers [0]

	for num in list_of_numbers:
		if num > largest:
			largest = num
	print(largest)

largest ([4, 20, 10])
