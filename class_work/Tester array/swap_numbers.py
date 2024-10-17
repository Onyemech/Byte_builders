
def lists (numbers):
	temp = 0
	for count in range(0, len(numbers) -1, 2):
		#if numbers[count] != numbers[count + 1]:
			temp = numbers[count]
			numbers[count] = numbers[count + 1]
			numbers[count + 1] = temp
	return numbers
			
