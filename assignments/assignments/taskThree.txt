sum = 0
average = 0

for number in range(10):
	scores = int(input("Enter score : "))
	sum += scores
	average += 1

result = sum // average
	
print("Total average is ", result)
print("Total sum is ", sum)