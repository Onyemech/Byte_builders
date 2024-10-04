def reversed ():
	numbers = 233
	unit = 10
	hundred = 100

	last_number = numbers // hundred
	extract_remaining = numbers  % hundred
	middle_number = extract_remaining  //  unit
	first_number = extract_remaining %  unit
	

	reversed_num = (first_number * hundred) + (middle_number * unit) + last_number 

	#print(first_number)
	
	print("New reversed is ",reversed_num)
	
reversed ()