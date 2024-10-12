'''amount of investment
number of years
percentage
prompt user
'''
try:
	no_of_years = int(input("Enter number of years : "))
	interest = int(input("Enter your interest : "))
	amount = float(input("Enter your amount : "))

	if amount > 0 and  no_of_years > 0:
		amount_percentage = amount * interest // 100

		print("Year	  ROI		AAI ")
		for numbers in range(1 , no_of_years+1, 1):
			final_amount = amount + amount_percentage
			final_amount_percent = final_amount * interest // 100

			new_roi = amount_percentage + final_amount_percent
			print(f'{numbers:},       ${amount_percentage:,}       ${final_amount:,}')
			amount_percentage =  new_roi
	else:
		print("Invalid input")

except(Exception):
	print("Wrong input")
	