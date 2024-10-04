user_choice = int(input("Hello welcome \n Enter \n1-> To deposit \n2-> To Withdraw"))
balance = 0
match user_choice:
	case 1 :
		deposit = int(input("How much do you wish to deposit?"))
		balance = balance + deposit
		print(balance , "Is you balance")
	case 2 :
		withdraw = int(input("How much do you wish to withdraw?"))
		balance = balance - withdraw
		if balance < 0:
			print("Insufficient funds")
		else :
			print(balance , "Is you balance")
	case 0:
		print(balance , "Is you balance")
		break