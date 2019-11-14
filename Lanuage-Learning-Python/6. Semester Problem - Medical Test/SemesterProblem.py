# Anthony Tesoriero, Joseph Salemo, Joshua Lunsk, November 14 2019, Semester Problem - Medical Test
# Status: Completed, November 14 2019
# Problem description: https://github.com/anttesoriero/Language-Learning-Python/blob/master/SEMESTERHW.md

# Opens the text file containing the patient data (PatientData.txt)
PatientData = open("PatientData.txt", "r")

# Initialize variables for calculation
diseaseTest1 = test1 = diseaseTest2 = test2 = 0 
notDiseaseNotTest1 = notTest1 = notDiseaseNotTest2 = notTest2 = 0

# Loops through file, splitting each line with " " delimiter
for data in PatientData:
	# Splits with " " delimiter
	patient = data.split()
	
	# Removes "\n" from last element
	patient[-1] = patient[-1].strip('\n')
	
	# Collect data
	patientNum = int(patient[0])
	diseaseVal = int(patient[1])
	test1Val = int(patient[2])
	test2Val = int(patient[3])
	
	# Test1 Check
	if test1Val == 1:
		test1 += 1
		if diseaseVal == 1:
			diseaseTest1 += 1
	else:
		notTest1 += 1
		if diseaseVal == 0:
			notDiseaseNotTest1 += 1
			
	# Test2 check
	if test2Val == 1:
		test2 += 1
		if diseaseVal == 1:
			diseaseTest2 += 1
	else:
		notTest2 += 1
		if diseaseVal == 0:
			notDiseaseNotTest2 += 1

DP1 = float(diseaseTest1)/test1
DP2 = float(diseaseTest2)/test2
HN1 = float(notDiseaseNotTest1)/notTest1
HN2 = float(notDiseaseNotTest2)/notTest2

if DP1 > DP2 and HN1 > HN2:
	decision = "Test 1 is better"
elif DP1 < DP2 and HN1 < HN2:
	decision = "Test 2 is better"
else:
	decision = "Neither test is better"

print("P(D | Pos1) =", DP1, "\n" + 
			"P(D | Pos2) =", DP2, "\n" +
			"P(H | Neg1) =", HN1, "\n" +
			"P(H | Neg2) =", HN2, "\n" +
			decision)


