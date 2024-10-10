
options = """ 			
			Hello Welcome 
		Please choose your option from 1 - 4
			1 . Single
			2 . Married Filling Jointly
			3 . Married Filling Seperately
			4 . Head of HouseHold
		"""
print(options)

user_choice = int(input(""))

match user_choice:
	case 1:
		amount = float(input("Enter amount : "))
		if amount <= 8350 and amount >= 0:
			new_amount = amount - 8350
			tax_rate = new_amount* 10 // 100
			print("Tax rate is $", tax_rate + 835) 
		elif amount > 8350 and amount <= 33950:
			new_amount = amount - 8350
			tax_rate = new_amount * 15 // 100
			print("Tax rate is $", tax_rate + 835) 
		elif amount > 33950 and amount <= 82250:
			new_amount = amount - 8350
			tax_rate = new_amount * 25 // 100
			print("Tax rate is ", tax_rate + 835) 
		elif amount > 82250 and amount <= 171550:
			new_amount = amount - 8350
			tax_rate = new_amount * 28 // 100
			print("Tax rate is ", tax_rate + 835) 
		elif amount > 171550 and amount <= 372_950:
			new_amount = amount - 8350
			tax_rate = new_amount * 33 // 100
			print("Tax rate is ", tax_rate + 835) 
		elif amount > 372_950:
			new_amount = amount - 8350
			tax_rate = new_amount * 35 // 100
			print("Tax rate is ", tax_rate + 835) 
		else:
			print("Invalid input")

	case 2:
		amount = float(input("Enter amount : "))
		if amount <= 16_700 and amount >= 0:
			new_amount = amount - 16700
			tax_rate = new_amount * 10 // 100
			print("Tax rate is ", tax_rate + 1670) 
		elif amount > 16700 and amount <= 67900:
			new_amount = amount - 16700
			tax_rate = new_amount * 15 // 100
			print("Tax rate is ", tax_rate+ 1670) 
		elif amount > 67900 and amount <= 137050:
			new_amount = amount - 16700
			tax_rate = new_amount * 25 // 100
			print("Tax rate is ", tax_rate+ 1670) 
		elif amount > 137050 and amount <= 208850:
			new_amount = amount - 16700
			tax_rate = new_amount * 28 // 100
			print("Tax rate is ", tax_rate+ 1670) 
		elif amount > 208850 and amount <= 372950:
			new_amount = amount - 16700
			tax_rate = new_amount * 33 // 100
			print("Tax rate is ", tax_rate+ 1670) 
		elif amount > 372950:
			new_amount = amount - 16700
			tax_rate = new_amount * 35 // 100
			print("Tax rate is ", tax_rate+ 1670) 
		else:
			print("Invalid input")

	case 3:
		amount = float(input("Enter amount : "))
		if amount <= 8350 and amount >= 0:
			new_amount = amount - 8350
			tax_rate = new_amount* 10 // 100
			print("Tax rate is $", tax_rate + 835) 
		elif amount > 8350 and amount <= 33950:
			new_amount = amount - 8350
			tax_rate = new_amount * 15 // 100
			print("Tax rate is $", tax_rate + 835) 
		elif amount > 33950 and amount <= 68525:
			new_amount = amount - 8350
			tax_rate = new_amount * 25 // 100
			print("Tax rate is ", tax_rate + 835) 
		elif amount > 68525 and amount <= 104426:
			new_amount = amount - 8350
			tax_rate = new_amount * 28 // 100
			print("Tax rate is ", tax_rate + 835) 
		elif amount > 104426 and amount <= 186_475:
			new_amount = amount - 8350
			tax_rate = new_amount * 33 // 100
			print("Tax rate is ", tax_rate + 835) 
		elif amount > 186_475:
			new_amount = amount - 8350
			tax_rate = new_amount * 35 // 100
			print("Tax rate is ", tax_rate + 835) 
		else:
			print("Invalid input")


	case 4:
		amount = float(input("Enter amount : "))
		if amount <= 11950 and amount >= 0:
			new_amount = amount - 16700
			tax_rate = new_amount * 10 // 100
			print("Tax rate is ", tax_rate) 
		elif amount > 11950 and amount <= 45500:
			new_amount = amount - 16700
			tax_rate = new_amount * 15 // 100
			print("Tax rate is ", tax_rate) 
		elif amount > 45500 and amount <= 117450:
			new_amount = amount - 16700
			tax_rate = new_amount * 25 // 100
			print("Tax rate is ", tax_rate) 
		elif amount > 117450 and amount <= 190200:
			new_amount = amount - 16700
			tax_rate = new_amount * 28 // 100
			print("Tax rate is ", tax_rate) 
		elif amount > 190200 and amount <= 372950:
			new_amount = amount - 16700
			tax_rate = new_amount * 33 // 100
			print("Tax rate is ", tax_rate) 
		elif amount > 372950:
			new_amount = amount - 16700
			tax_rate = new_amount * 35 // 100
			print("Tax rate is ", tax_rate) 
		else:
			print("Invalid input")

	





		


			
			
		
	