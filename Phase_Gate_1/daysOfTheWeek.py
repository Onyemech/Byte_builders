
day0 = 0
day1 = "Monday"
day2 = "Tuesday"
day3 = "Wednesday"
day4 = "Thursday"
day5 = "Friday"
day6 = "Saturday"


user_input = int(input("Enter today's date "))
user_input_2 = int(input("Enter the number of days elapsed since today:  "))

match user_input:
	case 0: print("Today is Sunday and the future day is ")
		day5 = user_input += user_input_2
	case 1: print("Today is Monday and the future day is ")
	case 2: print("Today is Tuesday and the future day is ")
	case 3: print("Today is Wednesday and the future day is ")
	case 4: print("Today is Thursday and the future day is ")
	case 5: print("Today is Friday and the future day is ")
	case 6: print("Today is Saturday and the future day is ")
		