'''
prompt user for name
store name as name_input
if the user enters his name 
Display u 



name_input = input("Enter your name: ")

if name_input:
	print("This is your name" ,name_input)
else:
	print("Invalid input")
'''

score = int(input("Enter score: "))

if score >= 75 and score <= 100:
	print("Your grade is A")
elif score >= 65 and score < 75:
	print("Your grade is B")
elif score >= 50 and score <= 64:
	print("Your grade is C")
elif score >= 40 and score <= 49:
	print("Your grade is D")
else:
	print("Baba get sense")
if user_input == 1: 
	phone_book_menu =  """
	1.search
	2.Erase
	0. back to menu :
			"""
	phonebook_option = int(input(phone_book_menu))
	if phonebook_option == 1:
		print("Search")
	elif phonebook_option == 2:
		print("Erase")
	elif phonebook_option == 0:
		print(menu)