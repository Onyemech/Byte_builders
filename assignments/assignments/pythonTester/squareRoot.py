import math

def get_squareroot(user_number):
	if user_number < 0 :
		raise ValueError("Invalid input\n please enter a valid integer")
	if not isinstance(user_number, int):
		raise TypeError("Input must be integer")

	if user_number % 5 == 0 :
		return round(math.sqrt(user_number),2)
	else :
		return user_number 