def palindrome ():

	numbers = 121
	unit = 10
	hundred = 100

	last_number = numbers // hundred
	extract_remaining = numbers  % hundred
	middle_number = extract_remaining  //  unit
	first_number = extract_remaining %  unit
	

	reversed_num = (first_number * hundred) + (middle_number * unit) + last_number 
	if reversed_num == numbers:
		return True
	elif reversed_num != numbers:
		print("False")
		
palindrome ()
