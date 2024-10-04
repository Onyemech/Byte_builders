'''
def collect_user_number(user_number):
	user_number = int(input("Enter your number :"))
	return odd_even(number)

print(collect_user_number(user_number))
'''

def check_number(number):

	number = int(input("Enter a number: "))
if number < 1 and number > 999:
	print("invalid input")
if number % 2 == 0:
	number += number
	print(number)
if number % 2 == 1:
	number -= number
	print(number)
return number

print(check_number(number))


