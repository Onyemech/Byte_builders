'''
prompt user to enter amount
store as amount
prompt user to enter interest rate
store it as interest rate
prompt user to enter the duration in years
store as duration
Calculate by using the formula m = principal / rate ( 1 + rate)power number of years / 1 + rate )power n - 1
Display results
'''

amount = int(input("Enter the principal amount : "))
interest = int(input("Enter the annual interest rate : "))
duration = int(input("Enter the duration in years : "))


actual_interest = (interest *1/100)/12

initialCalcultion =  actual_interest * ((1 +  actual_interest)**(duration *12))

finalCalculation =  ((1 + actual_interest)**(duration*12)) - 1

amountCalculation =  initialCalcultion / finalCalculation

monthly_payment = amount * amountCalculation

print("Your monthly payment is $",round(monthly_payment,2))




