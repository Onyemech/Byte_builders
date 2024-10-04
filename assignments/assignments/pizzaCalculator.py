import math

def pizza_calculator():

    one_pizza_box = 0
    price_of_pizza = 0

    number_of_people = int(input("How many number of people are you ordering for: "))
    pizza_choice = input("Enter the pizza type:\nSapa size\nSmall Money\nBig Boys\nOdogwu: ")

    if pizza_choice == "Sapa size":
        one_pizza_box = 4
        price_of_pizza = 2000
    elif pizza_choice == "Small Money":
        one_pizza_box = 6
        price_of_pizza = 2400
    elif pizza_choice == "Big Boys":
        one_pizza_box = 8
        price_of_pizza = 3000
    elif pizza_choice == "Odogwu":
        one_pizza_box = 12
        price_of_pizza = 4200
    else:
        print("Invalid pizza type entered.")
        return

    pizza_box_requested = math.ceil(number_of_people / one_pizza_box)
    all_slices = pizza_box_requested * one_pizza_box
    leftover = all_slices - number_of_people
    total_price = pizza_box_requested * price_of_pizza

    print("Number of boxes of pizza to buy:", pizza_box_requested)
    print("Number of leftover slices:", leftover)
    print("Total cost: NGN", total_price)

    pizza_calculator()


