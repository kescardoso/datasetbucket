import os
import time
import sys

import read_json
import read_csv
import generatePDF

#source /Users/kescardoso/Documents/GitHub/datasetbucket/venv/bin/activate

# TODO: connect to frontend / get user-specified Kaggle dataset instead of the hard-coded one in the filename variable

os.system("cd ./dataFiles")

#filename = "ronitf/heart-disease-uci"       # .csv dataset
filename = "dataturks/resume-entities-for-ner"    # .json dataset
#filename = "dataturks/vehicle-number-plate-detection" # not very useful .json
#filename = "gabrielaltay/georgia-voter-list-202011" # csv dataset - very large - in a new folder - 

zipFile = ""    # needed for report title later
 # results from parsing + calculations, will be passed into >>  generatePDF.generatePDFReport()

def findReadableFiles():    # find .json or .csv files in ./dataFiles folder
    dataResultsFoundCSV = {}
    dataResultsFoundJSON = {}
    for root, dirs, files in os.walk("./dataFiles"):
            for f in files:
                if ".json" in f:
                    print(f)
                    dataResultsFoundJSON = read_json.readJSON("./dataFiles/", f)
                    #print(dataResultsFoundJSON)
                if ".csv" in f:
                    dataResultsFoundCSV = read_csv.readCSV("./dataFiles/", f)
                    # TODO: ? need to make dataResultsFound appendable, or create multiple dicts in case a data set has more than 1 type of file 
    generatePDF.generatePDFReport( zipFile , None, dataResultsFoundCSV, dataResultsFoundJSON) # generate the PDF report
    return True

# copy zip to dataFiles folder and open the zip to get the data files
def openFiles():  
    if os.system("kaggle datasets download -d " + filename) == 0 :
        indexOfSlash = filename.find("/") # kaggle names dataset like: [creator of dataset]/[name of dataset]
        zipFile = filename[(indexOfSlash+1):len(filename)]

        os.system("cp " + zipFile + ".zip dataFiles") # copy to dataFiles folder
        for root, dirs, files in os.walk("./dataFiles"): # find the .zip file in the folder
            for fn in files:
                os.system("open ./dataFiles/" + zipFile + ".zip") # open the file in a designated folder so we know where the files are!
        
    return zipFile
    
zipFile = openFiles() # save zipFiles so it can be accessed in findReadableFiles()
time.sleep(7) # >>>>> protects from multithreading woes :,(

if findReadableFiles():  # >>>>> if statement protects from multithreading woes :,(
    os.remove(zipFile + ".zip")
    os.remove("./dataFiles/" + zipFile + ".zip") # dont need the copied zip anymore! ( still need to delete the zip in the main file system )