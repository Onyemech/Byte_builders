'''
Declare your function name
declare a variable total 
declare your list
loop through the list and increament total each time
display results
'''

def running_total():
	
	sub_total = {0}	
	numbers = {10, 20, 30}
	
	for num in numbers:
		sub_total = sub_total + numbers
	print(sub_total)

running_total()

	