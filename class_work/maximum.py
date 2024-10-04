def maximum(first_number , second_number , third_number):

	largest = 0

	if first_number > second_number:
		largest = first_number
	else:
		largest = second_number

	if third_number > largest:
		largest = third_number
	return largest

	print(maximum(100 , 200 ,10))
	
