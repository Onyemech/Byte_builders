def sum_double_num(odd_position):
    add = 0
    while odd_position != 0:
        add += odd_position % 10
        odd_position = odd_position // 10
    return add

def get_first_digit(user_number):
    convert_to_string = str(user_number)
    first_char = convert_to_string[0]
    second_char = convert_to_string[1]
    first2_digit = int(first_char) * 10 + int(second_char)
    if first2_digit == 37:
        return first2_digit
    else:
        convert_to_string = str(user_number)
        first_char = convert_to_string[0]
        first_digit = int(first_char)
        return first_digit

def main():
    user_input = input("Hello, Kindly Enter card details to verify: ")
    card_length = len(user_input)
    if card_length not in [13, 14, 15, 16]:
        print("Invalid Card")
    else:
        user_number = int(user_input)
        check_card_type = get_first_digit(user_number)
        real_number = user_input
        array_numbers = [0] * card_length
        for count in range(card_length - 1, -1, -1):
            array_numbers[count] = user_number % 10
            user_number = user_number // 10
        odd_position = [0] * (card_length // 2)
        even_position = [0] * (card_length // 2)
        odd_pos = 0
        even_pos = 0
        sum_odds = 0
        sum_even = 0
        for counter in range(len(array_numbers)):
            if counter % 2 == 0:
                odd_position[odd_pos] = array_numbers[counter]
                odd_pos += 1
            else:
                even_position[even_pos] = array_numbers[counter]
                even_pos += 1
        for cout in range(len(odd_position)):
            odd_position[cout] = odd_position[cout] * 2
            if odd_position[cout] > 9:
                odd_position[cout] = sum_double_num(odd_position[cout])
        for odd in odd_position:
            sum_odds += odd
        for even in even_position:
            sum_even += even
        total = sum_even + sum_odds
        if total % 10 == 0 and check_card_type == 4:
            visaCard = ("******************************\n"
                        "**Credit Card Type : VisaCard\n"
                        "**Credit Card Number: " + str(real_number) + "\n"
                        "**Credit Card Digit Length : " + str(card_length) + "\n"
                        "**Credit Card Validity Status: Valid\n"
                        "******************************")
            print(visaCard)
        elif total % 10 != 0 and check_card_type == 4:
            visaCard2 = ("******************************\n"
                         "**Credit Card Type : VisaCard\n"
                         "**Credit Card Number: " + str(real_number) + "\n"
                         "**Credit Card Digit Length : " + str(card_length) + "\n"
                         "**Credit Card Validity Status: invalid\n"
                         "******************************")
            print(visaCard2)
        if total % 10 == 0 and check_card_type == 5:
            masterCard = ("******************************\n"
                          "**Credit Card Type : MasterCard\n"
                          "**Credit Card Number: " + str(real_number) + "\n"
                          "**Credit Card Digit Length : " + str(card_length) + "\n"
                          "**Credit Card Validity Status: Valid\n"
                          "******************************")
            print(masterCard)
        elif total % 10 != 0 and check_card_type == 5:
            masterCard2 = ("******************************\n"
                           "**Credit Card Type : MasterCard\n"
                           "**Credit Card Number: " + str(real_number) + "\n"
                           "**Credit Card Digit Length : " + str(card_length) + "\n"
                           "**Credit Card Validity Status: invalid\n"
                           "******************************")
            print(masterCard2)
        if total % 10 == 0 and check_card_type == 37:
            expressCard = ("******************************\n"
                           "**Credit Card Type : American Express Cards\n"
                           "**Credit Card Number: " + str(real_number) + "\n"
                           "**Credit Card Digit Length : " + str(card_length) + "\n"
                           "**Credit Card Validity Status: Valid\n"
                           "******************************")
            print(expressCard)
        elif total % 10 != 0 and check_card_type == 3:
            expressCard2 = ("******************************\n"
                            "**Credit Card Type : American Express Cards\n"
                            "**Credit Card Number: " + str(real_number) + "\n"
                            "**Credit Card Digit Length : " + str(card_length) + "\n"
                            "**Credit Card Validity Status: invalid\n"
                            "******************************")
            print(expressCard2)

main()
