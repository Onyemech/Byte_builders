first_number = int(input("Enter your first number : "))
second_number = int(input("Enter your second number : "))
third_number = int(input("Enter your third number : "))

largest = first_number
middle_number = first_number
smallest = first_number

if smallest > second_number:
	smallest = second_number
if smallest > third_number:
	smallest = third_number

if middle_number > second_number and second_number < third_number :
	middle_number = second_number
if middle_number > third_number and third_number < second_number:
	middle_number = third_number

if largest < second_number:
	largest = second_number
if largest < third_number:
	largest = third_number


print(smallest , middle_number , largest)







