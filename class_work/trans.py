balance = 0
user_input = int(input("Enter option\n1 -> deposit \n2 -> withdraw\n3 -> Display balnce\nEnter 0 to terminate: "))

while != 0:
	if user_input == 1:
		amount = float(input("Enter deposit amount : "))
		balance += amount
		print(balance, 'your remainig balance')
		user_input = int(input("Enter option\n1 -> deposit \n2 -> withdraw\n3 -> Display balnce\nEnter 0 to terminate: "))


	elif user_input == 2:
		amount = float(input("Enter withdraw amount : "))
		if balance < amount:
			print("Insufficient funds")
		else:
			balance -= amount
	elif user_input == 3:
		print(balance , "is you remaining balance")
	if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 0:
		print("Invalid input")
	user_input = int(input("Enter option\n1 -> deposit \n2 -> withdraw\n3 -> Display balnce\nEnter 0 to terminate: "))


#def get_transaction()
	