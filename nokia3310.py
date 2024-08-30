def DisplayPhoneMenu():



	userInput =int(input(" Hello welcome to Nokia \n1-> Phone book\n2-> Messages\n3-> Chat\n4-> Call register\n5-> Tones\n6-> Settings\n7-> Call divert\n8-> Games\n9-> Calculator\n10-> Reminders\n11-> Clock\n12-> Profiles\n13-> SIM services\nEnter 0 to shut down: "))



	
	match userInput :

		case 1: Phonebook()

		case 2: Messages()

		case 3: print("Chat")

		case 4: CallRegister()

		case 5: Tones()

		case 6: Settings()

		case 7: print("Call divert")

		case 8: print("Games")

		case 9: print("Calculator")

		case 10:print("Reminder")

		case 12: print("Profiles")

		case 13: print("SIM services")

		case 11: Clock()





def Phonebook():

	print("phone book");

	userInput = int(input("\n1->Search\n2->Service Nos.\n3->Add name\n4->Erase\n5->Edit\n6->Assign tone\n7->Send b'card\n8->Options\n9->Speed dials\n10->Voice tags\n0->Back"))


	match userInput:

		case 1: print("Search")

		case 2: print("Service Nos.")

		case 3: print("Add name")

		case 4: print("Erase")

		case 5: print("Edit")

		case 6: print("Assign tone")

		case 7: print("Send b'card");

		case 8 : Options()

		case 9: print("Speed dials")

		case 10: print("Voice tags")

		case 0: DisplayPhoneMenu()





def Options():

	userInput = int(input("Options\n1->Type of view\n2->Memory Status\n0->Back"))

	match userInput:

		case 1 : System.out.print("Type of view")

		case 2 : System.out.println("Memory Status")

		case 0 : Phonebook()


def Messages():

	userInput = int(input("Messages\n1->Write messages\n2->Inbox\n3->Outbox\n4->Picture messages\n5->Templates\n6->Smileys\n7->Message setting\n8->Info service\n9->Voice mailbox number\n10->Service command editor\n0->Exit"))



	match userInput:

		case 1: print("Write Messages")

		case 2: print("Inbox")

		case 3: print("Outbox")

		case 4: print("Picture messages")

		case 5: print("Templates")

		case 6: print("Smileys")
		
		case 7: Message_settings()

		case 8: print("Info service")

		case 9: print("Voice mailbox number")

		case 10: print("Service command editor")

		case 0: DisplayPhoneMenu()



def Message_settings():
	
	userInput = int(input("Message settings\n1->Set 1\n2->Common\n0->Back"))

	match userInput:

		case 1:  Set1()

		case 2: Common()

		case 0: Messages()

def Set1():

	print("Set 1");

	userInput = int(input("1->Message centre number\n2->Messages sent as\n3->Message validity\n0.Back"))

	match userInput:

		case 1: print("Message centre")

		case 2: print("Message sent")

		case 3: print("Message validity")

		case 0: MessageSettings()


def Common():

	print("Common")

	userInput = int(input("1->Delivery reports\n2->Reply via same centre\n3->Character support\n0->Back"))

	match userInput:

		case 1: print("Delivery reports")

		case 2: print("Reply via same centre")

		case 3: print("Character support")

		case 0: MessageSettings()


def CallRegister():

	print("Call Register");

	userInput = int(inputprint("\n1->Missed calls\n2->Received calls\n3->Dialled numbers\n4->Erase recent call lists\n5->Show call duration\n6->Show all costs\n7->Call cost settings\n8->Prepaid credit\n"))



	match userInput:

		case 1: print("Missed calls")

		case 2: print("Received calls")

		case 3: print("Dialled numbers")

		case 4: print("Erase recent call lists")

		case 5: CallDuration()

		case 6: ShowAllCosts()

		case 7: CallCostSettings()

		case 8: print("Prepaid credit")

		case 0: DisplayPhoneMenu()




def CallDuration():

    print("Show call duration")

    userInput = int(input("\n1->Last call duration\n2->All call's duration\n3->Received call's duration\n4->Dialled call's duration\n5->Clear timers\n0->Back"))

   

    match userInput:

        case 1: print("Last call duration")

        case 2: print("All call's duration")

        case 3: print("Received call's duration")

        case 4: print("Dialled call's duration")

        case 5: print("Clear timers")

        case 0: CallRegister()


def ShowAllCosts():

    userInput = int(input("Show all costs\n1->Last call cost\n2->All calls' cost\n3->Clear counters\n0->Back"))

    

    match userInput:

        case 1: print("Last call cost")

        case 2: print("All calls' cost")

        case 3: print("Clear counters")

        case 0: CallRegister()

def CallCostSettings():

    userInput = int(input("Call cost settings\n1->Call cost limit\n2->Show costs in\n"))


    match userInput:

        case 1: print("Call cost limit")

        case 2: print("Show costs in")

        case 0: CallRegister()

def Tones():

    userInput = int(input("Tones\n1->Ringing tone\n2->Ringing volume\n3->Incoming call alert\n4->Composer\n5->Message alert tone\n6->Keypad tones\n7->Warning and game tones\n8->Vibrating alert\n9->Screen saver\n"))

   
    match userInput:

        case 1: print("Ringing tone")

        case 2: print("Ringing volume")

        case 3: print("Incoming call alert")

        case 4: print("Composer")

        case 5: print("Message alert tone")

        case 6: print("Keypad tones")

        case 7: print("Warning and game tones")

        case 8: print("Vibrating alert")

        case 9: print("Screen saver")

        case 0: DisplayPhoneMenu()



def Settings():

    settings = int(input("Settings\n1->Call settings\n2->Phone settings\n3->Security settings\n4->Restore factory settings\n"))

    

    match settings:

        case 1: CallSettings()

        case 2: PhoneSettings()

        case 3: SecuritySettings()

        case 4: print("Restore factory settings")

        case 0: DisplayPhoneMenu()




def CallSettings():

    userInput = int(input("Call settings\n1->Automatic redial\n2->Speed dialing\n3->Call waiting options\n4->Own number sending\n5->Phone line in use\n6->Automatic answer\n"))

    match userInput:

        case 1: print("Automatic redial")

        case 2: print("Speed dialing")

        case 3: print("Call waiting options")

        case 4: print("Own number sending")

        case 5: print("Phone line in use")

        case 6: print("Automatic answer")

        case 0: Settings()


def PhoneSettings():

    userInput = int(input("Phone settings\n1->Language\n2->Cell info display\n3->Welcome note\n4->Network selection\n5->Lights\n6->Confirm SIM service actions\n"))


    match userInput:

        case 1: print("Language")

        case 2: print("Cell info display")

        case 3: print("Welcome note")

        case 4: print("Network selection")

        case 5: print("Lights")

        case 6: print("Confirm SIM service actions")

        case 0: Settings()


def SecuritySettings():

    securitysettings = int(input("Security settings\n1->PIN code request\n2->Call barring service\n3->Fixed dialing\n4->Closed user group\n5->Phone security\n6->Change access codes\n"))

    
    match securitysettings:

        case 1: print("PIN code request")

        case 2: print("Call barring service")

        case 3: print("Fixed dialing")

        case 4: print("Closed user group")

        case 5: print("Phone security")

        case 6: print("Change access codes")

        case 0: Settings()


def Clock():

    clock = int(input("Clock\n1->Alarm clock\n2->Clock settings\n3->Date settings\n4->Stopwatch\n5->Countdown timer\n6->Auto update of date and time\n"))

   

    match clock:

        case 1: print("Alarm clock")

        case 2: print("Clock settings")

        case 3: print("Date settings")

        case 4: print("Stopwatch")

        case 5: print("Countdown timer")

        case 6: print("Auto update of date and time")

        case 0: DisplayPhoneMenu()




DisplayPhoneMenu()

