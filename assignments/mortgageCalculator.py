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

initialCalcultion = amount /  + interest + interest * duration

monthly_payment = initialCalcultion /  interest  * duration 

print("Your monthly payment is ", monthly_payment)