'''
Collect the string 
declare your function 
loop through the string 
Check if the new String is equal to the old string if so 
Display results
'''

def reversal () :
	
	words = "Hello"

	reversed_word = words[::-1]

	if words == reversed_word:
		print(words ," is a palindrome")
	elif words != reversed_word:
		print(words ," is not a palindrome")
reversal()