# Programming Languages Fall 2019 Python Group, Simple Repetition
# Status: Complete, to be submitted
print("Input each of your numbers, pressing return after each one. Enter 'x' when done.")
sum = 0.0
n = 0
while n != "x":
	n = input("Input: ")
	if n != "x":
		sum += float(n)
print(sum)
