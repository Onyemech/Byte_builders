amount = float(input("Enter your amount : "))

if amount < 0:
	print("Dear User\nYou wan thief car")
if amount > 10_000_000:
	charge_percent = amount * 20 // 100
	print ("Your duty charge percentage is ", charge_percent)

elif amount >= 5_000_000 and amount <= 10_000_000:
	charge_percent = amount * 15 // 100
	print ("Your duty charge percentage is ", charge_percent)

elif amount >= 2_500_000 and amount < 5_000_000:
	charge_percent = amount * 10 // 100
	print ("Your duty charge percentage is ", charge_percent)

elif amount < 2_500_000 and amount > 0:
	charge_percent = amount * 5 // 100
	print ("Your duty charge percentage is ", charge_percent)