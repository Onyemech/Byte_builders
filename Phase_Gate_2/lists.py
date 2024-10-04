list = {20, 15, 22, 23, 30, 41, 38, 8, 40, 10 , 12}

counter = 0
sum_even = 0
sum_odd = 0
third_position = 0

for numbers in list:
	counter += 1
print("Your list is ", counter - 1,"in number")

for numbers in range(len(list)):
	if numbers % 2 == 0:
		sum_even +=  numbers 
print(sum_even)

for numbers in range(len(list)):
	if numbers % 2 != 0:
		sum_odd +=  numbers 
print(sum_odd)

for numbers in range(len(list)):
	if numbers % 3 == 0:
		third_position +=  numbers 
print(sum_odd)