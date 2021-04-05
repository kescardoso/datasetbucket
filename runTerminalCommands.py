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

def makeFilesDir():
    try: 
        os.makedirs("dataFiles") # creating a temp directory in runtime
        os.system("cd ./dataFiles")
        return True
    except: # need to delete temp folder if an error occured and it wasn't deleted before         
        try:
            shutil.rmtree("./dataFiles/") # deleting the temp directory
            time.sleep(3)
            os.makedirs("dataFiles") # make a new/clean dataFiles folder
            os.system("cd ./dataFiles")
            return True
        except:
            try: # sometimes an error ocurrs and dataFiles is made, but not as a directory. So delete it and remake it
                os.remove("dataFiles") 
                time.sleep(3)
                os.makedirs("dataFiles")
                return True
            except:
                print("dataFiles not empty")
                return False
    



## file name is no longer global. It should be passed to each function. The start() function is called in 
## app.py when: @app.route("/analyse_data", methods=["GET", "POST"]), 
## which is where the url is retrieved from the user when they input it in the textbox 
## from the analyse.html page

# filename = "ronitf/heart-disease-uci"       # .csv dataset
#filename = "dataturks/resume-entities-for-ner"    # .json dataset

zipFile = ""    # needed for report title later

 # find .json or .csv files in ./dataFiles folder
def findReadableFiles(filename):   
    dataResultsFoundCSV = {} # results from parsing + calculations, will be passed into >>  generatePDF.generatePDFReport()
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

    reportMade = generatePDF.generatePDFReport( zipFile , None, dataResultsFoundCSV, dataResultsFoundJSON) # generate the PDF report

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
def openFiles(filename):  
    print("filename", filename)

    if os.system("kaggle datasets download -d " + filename) == 0 :
        indexOfSlash = filename.find("/") # kaggle names dataset like: [creator of dataset]/[name of dataset]
        zip = filename[(indexOfSlash+1):len(filename)]

        # checking for macOS or linux
        if sys.platform.startswith('darwin') | sys.platform.startswith('linux'):
            if makeFilesDir():
                os.system("cp " + zip + ".zip dataFiles") # copy to dataFiles folder

        # checking for windows
        if sys.platform.startswith('win32'):
            if makeFilesDir():
                os.system("copy " + zip + ".zip dataFiles") # copy to dataFiles folder

        time.sleep(3)
        
        for root, dirs, files in os.walk("./dataFiles"): # find the .zip file in the folder
            for fn in files:

                # checking for macOS or linux
                if sys.platform.startswith('darwin') | sys.platform.startswith('linux'):
                    os.system("open ./dataFiles/" + zip + ".zip") # open the file in a designated folder so we know where the files are!

                # checking for windows
                if sys.platform.startswith('win32'):
                    os.system("start ./dataFiles/" + zip + ".zip") # open the file in a designated folder so we know where the files are!
        
        return zip

def startCommands(filenameToDownload):
    filename = filenameToDownload
    time.sleep(3)
    if filename is not None:
        print('filename in filenameReady', filename)
        zipFile = openFiles(filename) # save zipFiles so it can be accessed in findReadableFiles()
        print('zipFile', zipFile)
        time.sleep(7) # >>>>> protects from multithreading woes :,(

    if findReadableFiles(filename):  # >>>>> protects from multithreading woes :,(
    # remove the dataFiles folder
        try:
            shutil.rmtree("./dataFiles/") # deleting the temp directory
        except:
            x = 0
        os.remove(zipFile + ".zip") # delete original downloaded zip file
        return True
    else:
        return False