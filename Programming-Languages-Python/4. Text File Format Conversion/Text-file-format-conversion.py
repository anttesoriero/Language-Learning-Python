# Programming Languages Fall 2019 Python Group, Text file format conversion
# Status: Complete, to be submitted

# Creates and clears a new text file
open('namesSplit.txt', 'w').close()

# Opens the text file containing the names
fileR = open("names.txt", "r")

# Loops through file, splitting each line with ":" delimiter
for names in fileR:
	splitList = names.split(":")
	
	# Removes "\n" from last element
	splitList[-1] = splitList[-1].strip('\n')
	lastName = splitList[0]
	firstName = splitList[1]
	petTotal = 0
	
	# Counts total number of pets for person
	for i in range(4):
		petTotal += int(splitList[i+2])
		
	# Opens previously created text file and appends "firstName lastName: No. Pets"
	fileW = open("namesSplit.txt", "a")
	line = firstName + " " + lastName + ": " + str(petTotal) + " " + "\n"
	fileW.write(line)
	fileW.close()

