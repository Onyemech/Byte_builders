list = {20, 15, 3, 23, 30, 6, 38, 8, 9, 10 }

counter = 0
sum_even = 0
sum_odd = 0
third_position = 0

for numbers in list:
	counter += 1
print("Your list is ", counter ,"in number")

for numbers in range(len(list)):
	if numbers % 2 == 0:
		sum_even +=  numbers 
print("The sum of all the elements in even position is ",sum_even)

for numbers in range(len(list)):
	if numbers % 2 != 0:
		sum_odd +=  numbers 
print("The sum of all the elements in odd position is ",sum_odd)

for numbers in range(len(list)):
	if numbers % 3 == 0:
		third_position +=  numbers 
print("The sum of all the elements in third position is  ",third_position)

get_total = 0

for numbers in list:
	 get_total += numbers
average = get_total / counter
print("The average of all the elements is ",average)
