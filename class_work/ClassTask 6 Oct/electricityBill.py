user_unit = float(input("Enter your unit : "))

if user_unit <= 100:
	print("No Charge")
elif user_unit > 200:
	bill = user_unit * 100
	print("Your electricity bill is ",bill)