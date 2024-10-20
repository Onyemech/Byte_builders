def sumOfDigits(number):
    sum = 0
    while number != 0:
        sum += number % 10  # Add the last digit to sum
        number //= 10  # Remove the last digit
    return sum

def getFirstDigit(realNumber):
    convertToString = str(realNumber)  # Convert number to string
    firstChar = convertToString[0]  # Get the first character
    firstDigit = int(firstChar)  # Convert character to digit
    return firstDigit

def main():
    input_str = input("Hello, Kindly Enter Card details to verify: ")
    number = int(input_str)
    realNumber = number
    checkCardType = getFirstDigit(realNumber)
    length = len(str(number))
    
    if length not in [13, 14, 15, 16]:
        print("Invalid card\nPlease Try Again")
    else:
        oddElements = 0
        evenElements = 0
        arrayNumbers = [0] * length
        oddPosition = [0] * (length // 2)
        evenPosition = [0] * (length // 2)
        sumOdds = 0
        sumEven = 0
        
        for count in range(length - 1, -1, -1):
            arrayNumbers[count] = number % 10
            number //= 10
        
        for counter in range(len(arrayNumbers)):
            if counter % 2 == 0:
                oddPosition[oddElements] = arrayNumbers[counter]
                oddElements += 1
            else:
                evenPosition[evenElements] = arrayNumbers[counter]
                evenElements += 1
        
        for cout in range(len(oddPosition)):
            oddPosition[cout] *= 2
            if oddPosition[cout] > 9:
                oddPosition[cout] = sumOfDigits(oddPosition[cout])
        
        for odd in oddPosition:
            sumOdds += odd
        
        for even in evenPosition:
            sumEven += even
        
        total = sumOdds + sumEven
        
        if total % 10 == 0 and checkCardType == 4:
            visaCard = ("******************************\n"
                        "**Credit Card Type : VisaCard\n"
                        "**Credit Card Number: " + str(realNumber) + "\n"
                        "**Credit Card Digit Length : " + str(length) + "\n"
                        "**Credit Card Validity Status: Valid\n"
                        "******************************")
            print(visaCard)
        elif total % 10 != 0 and checkCardType == 4:
            visaCard2 = ("******************************\n"
                         "**Credit Card Type : VisaCard\n"
                         "**Credit Card Number: " + str(realNumber) + "\n"
                         "**Credit Card Digit Length : " + str(length) + "\n"
                         "**Credit Card Validity Status: invalid\n"
                         "******************************")
            print(visaCard2)
        
        if total % 10 == 0 and checkCardType == 5:
            masterCard = ("******************************\n"
                          "**Credit Card Type : MasterCard\n"
                          "**Credit Card Number: " + str(realNumber) + "\n"
                          "**Credit Card Digit Length : " + str(length) + "\n"
                          "**Credit Card Validity Status: Valid\n"
                          "******************************")
            print(masterCard)
        elif total % 10 != 0 and checkCardType == 5:
            masterCard2 = ("******************************\n"
                           "**Credit Card Type : MasterCard\n"
                           "**Credit Card Number: " + str(realNumber) + "\n"
                           "**Credit Card Digit Length : " + str(length) + "\n"
                           "**Credit Card Validity Status: invalid\n"
                           "******************************")
            print(masterCard2)
        
        if total % 10 == 0 and checkCardType == 3:
            expressCard = ("******************************\n"
                           "**Credit Card Type : American Express Cards\n"
                           "**Credit Card Number: " + str(realNumber) + "\n"
                           "**Credit Card Digit Length : " + str(length) + "\n"
                           "**Credit Card Validity Status: Valid\n"
                           "******************************")
            print(expressCard)
        elif total % 10 != 0 and checkCardType == 3:
            expressCard2 = ("******************************\n"
                            "**Credit Card Type : American Express Cards\n"
                            "**Credit Card Number: " + str(realNumber) + "\n"
                            "**Credit Card Digit Length : " + str(length) + "\n"
                            "**Credit Card Validity Status: invalid\n"
                            "******************************")
            print(expressCard2)

if __name__ == "__main__":
    main()