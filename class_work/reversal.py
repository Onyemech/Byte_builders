user_input = int(input("Enter three Integer: "))

number1 = user_input % 10
second_number = user_input / 10
number2 = second_number % user_input
number3 = second_number / user_input

reversal = (number1 * 100) + (number2 * 10) + number3

print(reversal)