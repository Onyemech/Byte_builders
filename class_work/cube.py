def get_cube(number):
	if number < 0:
		raise ValueError("invalid number")
	return number ** 3