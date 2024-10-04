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

match user_input : 
	case 1:
	     	print("""Phone book
1.Search
2.Service Nos.
3.Add name
4.Erase
5.Edit
6.Assign tone
7.Send b'card
8.Options	
9.Speed dials
10.Voice tags
""")
option = int(input(""))
match option:
	case 8:
		print("Options\n1.Type of view\n2.Memory status")


	case 2:
		print("""Messages""")

messages = int(input(""))
match messages:
	case 7:
		print("1.Set 1\n2.Common") 
user_input1 = int(input(""))
match user_input1 :
	case 1:
		print("1.Set\n1.Message centre number\n2.Messages sent as\n3.Message validity")
	case 2:
		print("2.Common\n1.Delivery reports\n2.Reply via same centre\n3.Character support")


	case 3:
		print("chat")
	case 4:
		print("Call register")
	case 5:
		print("Tone")
	case 6:
		print("Settings")
	case 7:
		print("Call divert")
	case 8:
		print("Games")
	case 9:
		print("Calculator")
	case 10:
		print("Reminders")
	case 11:
		print("Clocks")
	case 12:
		print("Profiles")
	case 13:
		print("Sim services")
	case _:
		print("invalid input")








	