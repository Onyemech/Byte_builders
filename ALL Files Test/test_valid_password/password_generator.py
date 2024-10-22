import string
import random

password = string.ascii_lowercase 

def generate_password (password):

	small_letters = string.ascii_lowercase
	capital_letters = string.ascii_uppercase
	digits = string.digits
	symbols = string.punctuation

	new_lower = random.choice(small_letters )
	new_capital = random.choice(capital_letters)
	new_number = random.choice(digits)
	new_char = random.choice(symbols)


	password = []

	for count in range(4):
		password.append(small_letters[count])
		password.append(capital_letters[count])
		password.append(digits[count])
		password.append(symbols[count])

	random.shuffle(password)

	for _ in range(1):
		password += random.choice(password)
	newPass = ' ' . join(password)
	
	return newPass
print(generate_password (password))