import os
import time
import sys

import read_json
import read_csv
import generatePDF


import zipfile
import shutil


#source /Users/kescardoso/Documents/GitHub/datasetbucket/venv/bin/activate

# TODO: connect to frontend / get user-specified Kaggle dataset instead of the hard-coded one in the filename variable

# creating the dataFiles directory
os.makedirs("dataFiles") # creating a temp directory in runtime

os.system("cd ./dataFiles")

# filename = "ronitf/heart-disease-uci"       # .csv dataset
filename = "dataturks/resume-entities-for-ner"    # .json dataset
filename = "ronitf/heart-disease-uci"       # .csv dataset
#filename = "dataturks/resume-entities-for-ner"    # .json dataset
#filename = "dataturks/vehicle-number-plate-detection" # not very useful .json
#filename = "gabrielaltay/georgia-voter-list-202011" # csv dataset - very large - in a new folder - 

zipFile = ""    # needed for report title later


def findReadableFiles():    # find .json or .csv files in ./dataFiles folder
    #dataResultsFound = {} # results from parsing + calculations, will be passed into >>  generatePDF.generatePDFReport()
    dataResultsFoundCSV = {}
    dataResultsFoundJSON = {}
    for root, dirs, files in os.walk("./dataFiles/"):
            
# comment this(only for testing purpose)
# -- from here --
            if sys.platform.startswith('darwin') | sys.platform.startswith('linux'):

                for filename in files:
                    
                    # global dataResultsFound
                    if ".json" in filename: 
                        dataResultsFoundJSON = read_json.readJSON("./dataFiles/", filename)

                    if ".csv" in filename: 
                        dataResultsFoundCSV = read_csv.readCSV("./dataFiles/", filename)
                        # TODO: ? need to make dataResultsFound appendable, or create multiple dicts in case a data set has more than 1 type of file 
# -- till here --
           
# test for mac and linux (this works for windows)
# uncomment this(only for testing purpose)
# -- from here --

            # for filename in files:
            #         with zipfile.ZipFile(filename,'r') as file:

            #             file.extractall("./dataFiles")

            #             for name in file.namelist():
            #                 data = file.read(name)
                            
            #                 if ".csv" in name:
            #                     dataResultsFound = read_csv.readCSV("./dataFiles/", name)

# -- till here --
            
# comment this (only for testing purpose)
# -- from here --
            if sys.platform.startswith('win32'):
                for filename in files:
                    with zipfile.ZipFile(filename,'r') as file:

                        file.extractall("./dataFiles") # extracting files in the dataFiles directory

                        for name in file.namelist():
                            print(name)
                            data = file.read(name)
                            # print(data)

                            if ".json" in name: 
                                print(".json")
                                dataResultsFoundJSON = read_json.readJSON("./dataFiles/", name)
                            
                            if ".csv" in name:
                                dataResultsFoundCSV = read_csv.readCSV("./dataFiles/", name)
# -- till here --

    generatePDF.generatePDFReport( zipFile , None, dataResultsFoundCSV, dataResultsFoundJSON) # generate the PDF report

 # results from parsing + calculations, will be passed into >>  generatePDF.generatePDFReport()

############ ELIZABETH'S CODE FOR THIS FUNCTION ##############
# def findReadableFiles():    # find .json or .csv files in ./dataFiles folder
#     dataResultsFoundCSV = {}
#     dataResultsFoundJSON = {}
#     for root, dirs, files in os.walk("./dataFiles"):
#             for f in files:
#                 if ".json" in f:
#                     print(f)
#                     dataResultsFoundJSON = read_json.readJSON("./dataFiles/", f)
#                     #print(dataResultsFoundJSON)
#                 if ".csv" in f:
#                     dataResultsFoundCSV = read_csv.readCSV("./dataFiles/", f)
#                     # TODO: ? need to make dataResultsFound appendable, or create multiple dicts in case a data set has more than 1 type of file 
#     generatePDF.generatePDFReport( zipFile , None, dataResultsFoundCSV, dataResultsFoundJSON) # generate the PDF report

    return True

# copy zip to dataFiles folder and open the zip to get the data files
def openFiles():  
    if os.system("kaggle datasets download -d " + filename) == 0 :
        indexOfSlash = filename.find("/") # kaggle names dataset like: [creator of dataset]/[name of dataset]
        zipFile = filename[(indexOfSlash+1):len(filename)]

        # checking for macOS or linux
        if sys.platform.startswith('darwin') | sys.platform.startswith('linux'):
            os.system("cp " + zipFile + ".zip dataFiles") # copy to dataFiles folder

        # checking for windows
        if sys.platform.startswith('win32'):
            os.system("copy " + zipFile + ".zip dataFiles") # copy to dataFiles folder

        time.sleep(3)

        for root, dirs, files in os.walk("./dataFiles"): # find the .zip file in the folder
            for fn in files:

                # checking for macOS or linux
                if sys.platform.startswith('darwin') | sys.platform.startswith('linux'):
                    os.system("open ./dataFiles/" + zipFile + ".zip") # open the file in a designated folder so we know where the files are!

                # checking for windows
                if sys.platform.startswith('win32'):
                    os.system("start ./dataFiles/" + zipFile + ".zip") # open the file in a designated folder so we know where the files are!
        
    return zipFile
    
zipFile = openFiles() # save zipFiles so it can be accessed in findReadableFiles()
time.sleep(7) # >>>>> protects from multithreading woes :,(


if findReadableFiles():  # >>>>> protects from multithreading woes :,(
    # remove the dataFiles folder
    shutil.rmtree("./dataFiles/") # deleting the temp directory


############### Elizabeth's code #####################
# if findReadableFiles():  # >>>>> if statement protects from multithreading woes :,(
#     os.remove(zipFile + ".zip")
#     os.remove("./dataFiles/" + zipFile + ".zip") # dont need the copied zip anymore! ( still need to delete the zip in the main file system )

