user_input = input("Enter a character to check : ")

vowels = ['aeiou']
for letters in range(len(vowels)):
	if user_input.lower() in vowels[letters]:
		print("True")
		break
	else:
		print(user_input," is not a vowel")
		break