import random

count = 1
correct = 0
incorrect = 0

while count < 11:
	first_number = random.randrange(15, 30)
	second_number = random.randrange(1, 14)
	
	result = first_number - second_number
	
	print(first_number , " - " , second_number)
	user_input = int(input())
	
	if user_input == result:
		print("correct")
		correct+=1
	else:
		print("incorrect")
		incorrect += 1
	count += 1
print("You final score is " , correct , "out of ", count - 1, " tries")