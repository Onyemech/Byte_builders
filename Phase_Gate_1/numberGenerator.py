'''
declare the first number and assign it to 2
declare second number and assign the value 3 to it
Calculate the sum and store in a variable name sum
prompt user for the answer 
if the user's answer is correct display true
else display false

'''

first_number = 2
second_number = 4

result = first_number + second_number 

user_input = int(input("What is the answer of ",first_number ," + " ,second_number))

if user_input == result:
	print("True")
elif user_input != result:
	print("False")