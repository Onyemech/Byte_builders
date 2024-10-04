import math

def divide_or_square (number):

	number = 10

	if number % 5 == 0:
		result = math.sqrt(number)
		return result
	else:
		result = number % 5
		return result

