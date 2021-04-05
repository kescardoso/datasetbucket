# importing csv module
import csv

import calculations

def readCSV(path, filename): 
	fields=[]
	rows=[]
	
	demographicsToSearch = { 'ethnicity':'str', 'gender':'str', 'religion':'str', 'income':'int', 'age':'int', 'education':'str', 'location':'str', 'sex':'int'}
	# dict to save strings we can count instances of:
	Location= {}
	Ethnicity = {}
	Gender = {}
	Religion = {}
	Education = {}
	# arrays to save values we can calculate mean and variance for:
	income = []
	age = []
	sex = [] 
	# count 
	iCount = 0
	aCount = 0
	sCount = 0

	# reading csv file
	with open(path+filename, 'r') as csvfile:
		# creating a csv reader object
		csvreader = csv.reader(csvfile)
		
		# extracting field names through first row
		fields = next(csvreader)

		# extracting each data row one by one
		for row in csvreader:
			rows.append(row)
			
	validRowsIndex = []
	validRowsName = []
	
	# TODO need to check if a value is a string or number
	countFieldNum = 0 # finding the index of field was causing problems. 
	for field in fields:
		for var in demographicsToSearch: # get the index and name of all values in the file that match the labels we are looking for
			if var in field:
				validRowsIndex.append(countFieldNum)
				validRowsName.append(var.lower())
		countFieldNum += 1
	print(validRowsIndex)
	print(validRowsName)
	# for each row, get the value at each valid index and add to array OR dict AND increase count 
	# (lowercase variables are arrays, capitalized variables are dicts)
	for row in rows:
		for vR in validRowsIndex:
			if len(row) > validRowsIndex[vR] and row[validRowsIndex[vR]] is not None:
				print(vR, validRowsIndex[vR], validRowsName[vR], row[validRowsIndex[vR]])
				if 'age' in validRowsName[vR]: 
					a = float(row[validRowsIndex[vR]])
					aCount += 1
					age.append(a)
				elif 'sex' in validRowsName[vR]:
					s = float(row[validRowsIndex[vR]])
					sCount += 1
					sex.append(s)
				elif 'income' in validRowsName[vR]:
					i = float(row[validRowsIndex[vR]])
					iCount += 1
					income.append(i)
				elif 'location' in validRowsName[vR]:
					if "." not in row[validRowsIndex[vR]]:
						if Location.get(row[validRowsIndex[vR]]) is not None:
							count = Location.get(row[validRowsIndex[vR]])+1
							Location.update({row[validRowsIndex[vR]]: count})
						else:
							Location.update({row[validRowsIndex[vR]]:1})
				elif 'ethnicity' in validRowsName[vR].lower():
					if Ethnicity.get(row[validRowsIndex[vR]]) is not None:
						count = Ethnicity.get(row[validRowsIndex[vR]])+1
						Ethnicity.update({row[validRowsIndex[vR]]: count})
					else:
						Ethnicity.update({row[validRowsIndex[vR]]:1})
				elif 'gender' in validRowsName[vR].lower():
					if Gender.get(row[validRowsIndex[vR]]) is not None:
						count = Gender.get(row[validRowsIndex[vR]])+1
						Gender.update({row[validRowsIndex[vR]]: count})
					else:
						Gender.update({row[validRowsIndex[vR]]:1})
				elif 'religion' in validRowsName[vR].lower():
					if Religion.get(row[validRowsIndex[vR]]) is not None:
						count = Religion.get(row[validRowsIndex[vR]])+1
						Religion.update({row[validRowsIndex[vR]]: count})
					else:
						Religion.update({row[validRowsIndex[vR]]:1})
				elif 'education' in validRowsName[vR].lower():
					if Education.get(row[validRowsIndex[vR]]) is not None:
						count = Education.get(row[validRowsIndex[vR]])+1
						Education.update({row[validRowsIndex[vR]]: count})
					else:
						Education.update({row[validRowsIndex[vR]]:1})
	
	labelDict = {} # dict to return to runTerminalCommands
	# TODO : do analysis on string values
	if len(age) > 1:
		ageVar = calculations.calcVariance(age)
		ageMean = calculations.calcMean(age)
		labelDict.update({"Age": ["Count: " + str(aCount), "Variance: " + str(ageVar), "Mean: " + str(ageMean)]})
	if len(sex) > 1:
		sexVar = calculations.calcVariance(sex)
		sexMean = calculations.calcMean(sex)
		uniqueValues = calculations.calcUniquieValues(sex)
		if uniqueValues <= 2: # check if only included 2 or less sex data points
			labelDict.update({"Sex": ["Count: " + str(sCount), "Variance: " + str(sexVar), "Mean: " + str(sexMean), "Recommendations: " +"You only included " + str(uniqueValues) + " Sex data points.", "If you did not include Intersex or Transgender people, consider how this might impact your results."]})
		else:
			labelDict.update({"Sex": ["Count: " + str(sCount), "Variance: " + str(sexVar), "Mean: " + str(sexMean)]})
	if len(income) > 1:
		incomeVar = calculations.calcVariance(income)
		incomeMean = calculations.calcMean(income)
		labelDict.update({"Income": ["Count: " + str(iCount), "Variance: " + str(incomeVar), "Mean: " + str(incomeMean)]})
	if len(Ethnicity) > 0:
		labelDict.update({'Ethnicity': Ethnicity})
	if len(Gender) > 0:
		print(Gender)
		print(len(Gender))
		if len(Gender) == 2:
			Gender.update({'Recommendations: ': "You only have two genders in your data.", '-': "Consider how not including other genders might bias your results and lead to erasure."})
			labelDict.update({'Gender':Gender})
		else:
			labelDict.update({'Gender': Gender})

	return labelDict
	
