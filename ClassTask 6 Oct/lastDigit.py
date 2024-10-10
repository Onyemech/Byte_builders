user_number = int(input("Enter your digit number : "))
if user_number != int(userInput):
	print("Invalid input")
last_digit = user_number % 10
print("Your last number is ", last_digit)
