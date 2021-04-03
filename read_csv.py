# importing csv module
import csv

import sys

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

	for field in fields:
		for var in demographicsToSearch: # get the index and name of all values in the file that match the labels we are looking for
			if var in field:
				print(var)
				validRowsIndex.append(field.index(var))
				validRowsName.append(var.lower())

	# for each row, get the value at each valid index and add to array OR dict AND increase count 
	# (lowercase variables are arrays, capitalized variables are dicts)
	
	print(validRowsName)

	############## Sakshi's Code###############
	texts = [each_string.lower() for each_string in validRowsName]

	# print(texts)
	if sys.platform.startswith('win32'):
		for row in rows:
			for vR in validRowsIndex:
				if len(row) > vR and row[vR] is not None:
					if 'age' in validRowsName: 
						a = float(row[vR])
						aCount += 1
						age.append(a)
					if 'sex' in validRowsName:
						s = float(row[vR])
						sCount += 1
						sex.append(s)
					if 'income' in validRowsName:
						i = float(row[vR])
						iCount += 1
						income.append(i)
					if 'location' in validRowsName:
						if "." not in row[vR]:
							if Location.get(row[vR]) is not None:
								count = Location.get(row[vR])+1
								Location.update({row[vR]: count})
							else:
								Location.update({row[vR]:1})
					if 'ethnicity' in texts:
						if Ethnicity.get(row[vR]) is not None:
							count = Ethnicity.get(row[vR])+1
							Ethnicity.update({row[vR]: count})
						else:
							Ethnicity.update({row[vR]:1})
					if 'gender' in texts:
						if Gender.get(row[vR]) is not None:
							count = Gender.get(row[vR])+1
							Gender.update({row[vR]: count})
						else:
							Gender.update({row[vR]:1})
					if 'religion' in texts:
						if Religion.get(row[vR]) is not None:
							count = Religion.get(row[vR])+1
							Religion.update({row[vR]: count})
						else:
							Religion.update({row[vR]:1})
					if 'education' in texts:
						if Education.get(row[vR]) is not None:
							count = Education.get(row[vR])+1
							Education.update({row[vR]: count})
						else:
							Education.update({row[vR]:1})

### Elizabeth's Code ###
	if sys.platform.startswith('darwin') | sys.platform.startswith('linux'):
		for row in rows:
			for vR in validRowsIndex:
				if len(row) > vR and row[vR] is not None:
					print("[vR]: " + str(vR))
					if 'age' in validRowsName[vR]: 
						a = float(row[vR])
						aCount += 1
						age.append(a)
					elif 'sex' in validRowsName[vR]:
						s = float(row[vR])
						sCount += 1
						sex.append(s)
					elif 'income' in validRowsName[vR]:
						i = float(row[vR])
						iCount += 1
						income.append(i)
					elif 'location' in validRowsName[vR]:
						if "." not in row[vR]:
							if Location.get(row[vR]) is not None:
								count = Location.get(row[vR])+1
								Location.update({row[vR]: count})
							else:
								Location.update({row[vR]:1})
					elif 'ethnicity' in validRowsName[vR].lower():
						if Ethnicity.get(row[vR]) is not None:
							count = Ethnicity.get(row[vR])+1
							Ethnicity.update({row[vR]: count})
						else:
							Ethnicity.update({row[vR]:1})
					elif 'gender' in validRowsName[vR].lower():
						if Gender.get(row[vR]) is not None:
							count = Gender.get(row[vR])+1
							Gender.update({row[vR]: count})
						else:
							Gender.update({row[vR]:1})
					elif 'religion' in validRowsName[vR].lower():
						if Religion.get(row[vR]) is not None:
							count = Religion.get(row[vR])+1
							Religion.update({row[vR]: count})
						else:
							Religion.update({row[vR]:1})
					elif 'education' in validRowsName[vR].lower():
						if Education.get(row[vR]) is not None:
							count = Education.get(row[vR])+1
							Education.update({row[vR]: count})
						else:
							Education.update({row[vR]:1})




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
	
