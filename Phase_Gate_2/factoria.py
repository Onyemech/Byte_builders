user_input = int(input("Enter your number : "))

def check_factorial (user_input):

	result = 1

	while  user_input >= 1:
		result = result  * user_input
		user_input = user_input - 1
	print(" ", result)

check_factorial(user_input)