# Anthony Tesoriero, Joseph Salemo, Joshua Lunsk, November 14 2019, Semester Problem - Medical Test
# Status: Started
# Check problem on https://github.com/anttesoriero/Language-Learning-Python/blob/master/SEMESTERHW.md

# Opens the text file containing the patient data (PatientData.txt)
fileR = open("PatientData.txt", "r")

size = fileR.readline()
print(size)

# Initialize variables for calculation
diseaseTest1 = test1 = diseaseTest2 = test2 = 0 
notDiseaseNotTest1 = notTest1 = notDiseaseNotTest2 = notTest2 = 0

# Loops through file, splitting each line with " " delimiter
for data in fileR:
	# Splits with " " delimiter
	splitList = data.split(" ")
	
	# Removes "\n" from last element
	splitList[-1] = splitList[-1].strip('\n')
	
	# Collect data
	patientNum = splitList[0]
	diseaseVal = splitList[1]
	test1Val = splitList[2]
	test2Val = splitList[3]
	
	print(diseaseVal, test1Val, test2Val)
	
	if diseaseVal == 1:
		# Positive Disease and test1
		if test1Val == 1:
			diseaseTest1 += 1
			test1 += 1
		
		# Positive Disease and test2
		if test2Val == 1:
			diseaseTest2 += 1
			test2 += 1
	else:
		# Negative Disease and test1
		if test1Val == 0:
			notDiseaseNotTest1 += 1
			notTest1 += 1
		
		# Negative Disease and test2
		if test2Val == 0:
			notDiseaseNotTest2 += 1
			notTest2 += 1
		
		
print(diseaseTest1, test1, diseaseTest2, test2, notDiseaseNotTest1, notTest1, notDiseaseNotTest2, notTest2)
	
