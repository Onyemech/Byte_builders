'''
Display the price per litre.
prompt user for How many liters they want to purchase.
Store as number of litres.
Declare a variable named price_per_liter and assign the value 855 to it.
Declare a variable named Budget and divide the price_per_liter with 	number of litres. 
Display results
'''

print("Hello welcome to my fillng station \nprice per litres is 885: ")

number_of_amount = float(input("How much fuel do you want to buy? "))
price_per_litre = 855

budget = number_of_amount / price_per_litre 

print(f"Your are getting this {budget:.2f} as your amount of litres")

