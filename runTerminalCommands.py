import os
import time
import sys

import read_json
import read_csv
import generatePDF

# TODO: connect to frontend / get user-specified Kaggle dataset instead of the hard-coded one in the filename variable

os.system("cd ./dataFiles")

filename = "ronitf/heart-disease-uci"       # .csv dataset
# filename = "dataturks/resume-entities-for-ner"    # .json dataset
zipFile = ""    # needed for report title later
dataResultsFound = {} # results from parsing + calculations, will be passed into >>  generatePDF.generatePDFReport()

def findReadableFiles():    # find .json or .csv files in ./dataFiles folder
    for root, dirs, files in os.walk("./dataFiles"):
            for filename in files:
                if ".json" in filename:
                    dataResultsFound = read_json.readJSON("./dataFiles/", filename)
                if ".csv" in filename:
                    dataResultsFound = read_csv.readCSV("./dataFiles/", filename)
                    # TODO: ? need to make dataResultsFound appendable, or create multiple dicts in case a data set has more than 1 type of file 
    generatePDF.generatePDFReport( zipFile , None, dataResultsFound) # generate the PDF report
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

if findReadableFiles():  # >>>>> protects from multithreading woes :,(
    os.remove(zipFile + ".zip")
    os.remove("./dataFiles/" + zipFile + ".zip") # dont need the copied zip anymore! ( still need to delete the zip in the main file system )




    