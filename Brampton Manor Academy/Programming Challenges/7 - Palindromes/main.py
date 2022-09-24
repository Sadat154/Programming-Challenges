number1 = int(input("Integer 1: "))
number2 = int(input("Integer 2: "))

palindromeCounter = 0
lycherelCounter = 0
notLycherelCounter = 0


def check_if_palindrome(i):
	palindrome = 0
	if str(i) == str(i)[::-1]:
		palindrome = 1
		return palindrome
	else:
		return palindrome


for i in range (number1,number2+1):
	originalNumber = i
	if check_if_palindrome(i) == 1:
		palindromeCounter += 1
	else:
		counter = 0
		while counter < 61:
			newNumber = i + int(str(i)[::-1])
			if check_if_palindrome(newNumber) == 1:
				notLycherelCounter += 1
				counter = 100
			
			elif counter == 60:
				print(f"{originalNumber} is likely to be a lycherel")
				lycherelCounter += 1
				counter += 1
			else:
				i = newNumber
				counter += 1


print (f"Palindrome Numbers = {palindromeCounter}")
print(f"Not Lycherel Numbers = {notLycherelCounter}")
print(f"Lycherels: {lycherelCounter}")