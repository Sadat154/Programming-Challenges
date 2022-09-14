# this program took me too long to complete...

order_of_number = int(input("Please input the order of square: "))
top_left_number = int(input("Please input the top left number: "))

one_to_number = ""

# This makes a string of 1 --> order_of_number
for i in range(1, order_of_number + 1):
    one_to_number += str(i)


# This function works out the starting number using top_left_number and order_of_number. E.g., if 5 then 4 is entered this turns 12345 to 45123
def startingNumber():
    return (one_to_number[top_left_number - 1:order_of_number] + one_to_number[0:top_left_number - 1])


for j in range(0, order_of_number):
    finalNumber = startingNumber()[j:order_of_number] + startingNumber()[0:j]

    print(finalNumber)

# I noticed on the pdf there are gaps in between the numbers, I was wondering if there is an easy way to implement that in my code
