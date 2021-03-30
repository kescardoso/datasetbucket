# importing csv module
import csv

import calculations

def readCSV(path, filename): 
	# csv file name
	#filename = "data.csv"

	# initializing the titles and rows list
	fields = []
	rows = []

	# reading csv file
	with open(path+filename, 'r') as csvfile:
		# creating a csv reader object
		csvreader = csv.reader(csvfile)
		
		# extracting field names through first row
		fields = next(csvreader)

		# extracting each data row one by one
		for row in csvreader:
			rows.append(row)
			
	
	# TODO: need to create a dictionary for categories to search the file for and deal with the possibility that they are a string (ex: 'location'= "Bangalore") or an integer/float (ex: latitude: 120, longitude: 50])
	# TODO: need to generalize these values
	age = []
	sex = [] 
	aCount = 0
	sCount = 0
	# TODO need to check if a value is a string or number
	# printing data (just for debugging purpose, later we can change it to the desired format)
	for row in rows:
		out = fields[0] + ":" + row[0] + ", " + fields[1] + ":" + row[1]
		if row[0] is not None:
			a = float(row[0])
			aCount += 1
			age.append(a)
		if row[1] is not None:
			s = float(row[1])
			sCount += 1
			sex.append(s)
		#print(age, sex)
	
	# TODO: for loop to calc variance and mean of each category >> need to check if string or float
	ageVar = calculations.calcVariance(age)
	ageMean = calculations.calcMean(age)

	sexVar = calculations.calcVariance(sex)
	sexMean = calculations.calcMean(sex)

	# print(ageVar, ageMean)
	# print(sexVar, sexMean)

	# TODO for loop to add each category + values to the dictionary
	labelDict = {fields[0]: ["Count: " + str(aCount), "Variance: " + str(ageVar), "Mean: " + str(ageMean)], fields[1]: ["Count: " +  str(sCount),  "Variance: " + str(sexVar), "Mean: " + str(sexMean)]}
	return labelDict
	
