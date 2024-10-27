from datetime import datetime, timedelta

def get_next_flow_date(cycle_length, first_period_day):
    
    
    print("Your next flow date is:", next_menstruation_date.strftime("%Y-%m-%d"))
    print("Your ovulation starting date is:", ovulation_date.strftime("%Y-%m-%d"))
    print("Your safe period starts from:", safe_period_start.strftime("%Y-%m-%d"), "and ends on:", safe_period_end.strftime("%Y-%m-%d"))

user_name = input("Welcome to my menstruation cycle calculator \nPlease Enter your name: ")
user_age = int(input("Enter your age: "))

if user_age < 8 or user_age > 50:
    print("Please consult your doctor")
else:
    menstruation_start = int(input("Enter the first day of your last period: "))
    menstruation_cycle = int(input("Enter your menstruation cycle length: "))

    if menstruation_cycle < 28 or menstruation_cycle > 35:
        print("Please consult thy doctor")
    else:
        get_next_flow_date(menstruation_cycle, menstruation_start)
