# Programming Languages Fall 2019 Python Group, Floating-point Calculation
# Status: Complete, to be submitted

# Checks if the input is an integer
while True:
	try:
		n = int(input("Choose an integer: "))
		break
	except ValueError:
		print("Error: Not a valid number.")

# Checks if the input is positive
if n < 1:
	print("Error: Integer must be positive.")
else:
	sum = 0.0
	count = 0
  # Used to alternate the sign
	m = -1
  # Loops through values to the chosen integer, summing up values from 1 to 1/n, alterating the sign
	for i in range(n):
		# Sums up values from 1 to 1/n, alternating the sign
		sum += (-1 * m) * (1 / (i + 1))
		# Changes the sign
		m *= -1

	print("The sum is " + str(sum))
