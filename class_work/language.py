''' python switch

language = input("Enter preferred language: ")

match language:
	case "igbo":
		print("Oya enter asusu for me biko: ")
asusu = input("Okay enter next one: ")
	
match asusu:
	case "asusu":
		print("wow")
	case "Yoruba":
		print("Owoni werey")
	case "Hausa":
		print("ina kwu ana")
	case _:
		print("where them born you sef?")'''
menu = """ 
	   1 - phone book
           2 - Messages
	   3 - Chat
	   4 - Call register
	   5 - Tone
	   6 - Settings
	   7 - Call divert
	   8 - Games
	   9 - Calculator 
	   10 - Reminders
	   11 - Clocks
	   12 - Profiles
	   13 - Sim services :
	"""

	
user_input = int(input(menu))



