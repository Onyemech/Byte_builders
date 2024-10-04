def menu_display():

	menu = """

	Hello Welcome to Nokia please select one of the options below

	1.Phone book 
	2.Messages
	3.Chat
	4.Call Register
	5.Tones

	"""
	user_choice  = int(input(menu))

	match user_choice:

		case 1: phone_book()
		case 2: messages()

def phone_book():
	
	phone_book_menu = """
Phone book

1.Search 
2.Service Nos
3.Add name
4,Erase
5.Edit
6.Assign tone
7.Send b'card
8.Options
0.Back
	"""

	user_option = int(input(phone_book_menu))

	match user_option:

		case 8: option()
		case 0: menu_display

def messages ():
	
	messages = """
	Messages 
	1.Write messages
	2.Inbox
	3.Outbox
	4.Pictures
	5.Templates
	6.Smileys
	7.Message settings
	0.Back
	""" 
	user_choice = int(input(messages))
	
	match user_choice:
		case 7: messages_settings()
		case 0:  menu_display()

def messages_settings():
 
	message_settings = """

	Messages settings
	1.Set 1
	2.Common
	0.Back
	"""
	
	user_choice = int(input(message_settings))

	if user_choice == 1:
		set1 ()
	elif user_choice == 2:
		common()
	elif user_choice == 0:
		messages ()
	
			
	
def set1 ():
	set = """
	Set 1
	1.Messages settings
	2.Messages sent as
	3.Messages validity
	0.Back
"""
	user_choice = int(input(set))

	if user_choice == 0:
		messages_settings()
		
def common ():
	common = """

	Common
	1. Delivery reports
	2.Reply via same center
	3.Character support
"""	
	user_choice = int(input(common))

	if user_choice == 0:
		messages_settings()



def option():

	options = """ 
	Options
	
	1.Type of View
	2.Memory status
	0.Back
"""
	user_pick = int(input(options))

	if user_pick == 0:
		menu_display()
		
	
menu_display()	