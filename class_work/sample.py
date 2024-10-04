'''
prompt user for input
store as input 
declare a variable and assign the value 0
while user keeps depositing add the deposit to the variable
display results
'''

user_number = int(input("Hello welcome\nEnter 1 to deposit\n2. For withdrawal\n0. Balance\n: "))

balance = 0

while user_number != -1:

	if user_number == 1:
		deposit = float(input ("Enter your deposit amount: "))
		balance += deposit
		print(balance)
		user_number = int(input(""))

	elif user_number == 2:
		withdrawal = float(input("Enter your withdrawal amount: "))
		balance = balance - withdrawal
		print(balance)
		user_number = int(input(""))

		if withdrawal > balance:
			print("Insufficient funds")
	elif user_number == 0:
		print("Your balance is" , balance ,"\nThank you for banking with us")
		break