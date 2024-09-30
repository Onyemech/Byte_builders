user_input = int(input("Enter the any number from 0 to 1000 "))

divisor = 10
divider = 100

first_number = user_input % divisor
getSecond = user_input // divisor
second_number = getSecond % divisor
third_number = user_input // divider

sum = first_number + second_number + third_number

print(sum)

