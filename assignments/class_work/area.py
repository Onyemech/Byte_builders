'''
1. prompt user to enter first Integer
2. store the Integer as number1
3. prompt user to enter second Integer
4. store the Integer as number2
5. prompt user to enter third Integer
6. store the Integer as number3
7. add all the three numbers given to you by the user
7. Calculate the average by dividing the three numbers added with 3
8. Store result as average
9. Display output
'''

number1 = int(input("Enter the first Integer: "))
number2 = int(input("Enter the second Integer: ")) 
number3 = int(input("Enter the third Integer: "))
average = (number1 + number2 + number3) / 3
print("This is your average" , round(average, 1))