scores = 0
count = 0

average = float(input("Enter average of students\nPress 0 to terminate : "))

while average != 0:
	if average >= 0 and average <= 100:
		scores += average
		count += 1

	result = average // count

print("Your average is " , result)

	