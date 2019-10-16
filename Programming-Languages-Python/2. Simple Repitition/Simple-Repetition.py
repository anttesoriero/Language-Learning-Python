# Anthony Tesoriero, Joseph Salemo, Joshua Lunsk, October 9 2019, Simple Repetition
# Status: Complete, to be submitted

# Prints statement for user inpit
print("Input each of your numbers, pressing return after each one. Enter 'x' when done.")
sum = 0.0
n = 0

# Loops through input with summation
while n != "x":
	n = input("Input: ")
	if n != "x":
		sum += float(n)
print(sum)
