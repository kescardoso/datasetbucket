import os
import time
import sys

import read_json
import read_csv
import generatePDF

import main
import filePath

import zipfile
import shutil

#source /Users/kescardoso/Documents/GitHub/datasetbucket/venv/bin/activate

# TODO: connect to frontend / get user-specified Kaggle dataset instead of the hard-coded one in the filename variable

# creating the dataFiles directory

# def makeFilesDir():
#     try: 
#         os.makedirs("dataFiles") # creating a temp directory in runtime
#         os.system("cd ./dataFiles")
#         return True
#     except: # need to delete temp folder if an error occured and it wasn't deleted before         
#         try:
#             shutil.rmtree("./dataFiles/") # deleting the temp directory
#             time.sleep(3)
#             os.makedirs("dataFiles") # make a new/clean dataFiles folder
#             os.system("cd ./dataFiles")
#             return True
#         except:
#             try: # sometimes an error ocurrs and dataFiles is made, but not as a directory. So delete it and remake it
#                 os.remove("dataFiles") 
#                 time.sleep(3)
#                 os.makedirs("dataFiles")
#                 return True
#             except:
#                 print("dataFiles not empty")
#                 return False
    


zipFile = ""    # needed for report title later

 # find .json or .csv files in ./dataFiles folder
def findReadableFiles(filename, targetReportPath):   
    dataResultsFoundCSV = {} # results from parsing + calculations, will be passed into >>  generatePDF.generatePDFReport()
    dataResultsFoundJSON = {}
    
    for root, dirs, files in os.walk("./dataFiles/"):

            if sys.platform.startswith('darwin') | sys.platform.startswith('linux'):
                if len(dirs) > 0:
                    for d in dirs:
                        for files in os.walk("./dataFiles/"+d+"/"):
                            
                            for f1 in files:
                                if isinstance(f1, list):
                                    for fL in f1:
                                    # global dataResultsFound
                                        if ".json" in fL: 
                                            stringD = "./dataFiles/"+d
                                            dataResultsFoundJSON = read_json.readJSON(stringD, fL)
                                        if ".csv" in fL: 
                                            dataResultsFoundCSV = read_csv.readCSV("./dataFiles/", fL)

                        fileImg = os.listdir("./dataFiles/"+d)
                        print('fileImg', fileImg)
                        for f in fileImg:
                            if ".png" or ".jpeg" or ".jpg" in f:
                                file_paths, l = filePath.getPath(d)
                                if len(file_paths) != 0:
                                    reportMade = main.readImage(file_paths, l, targetReportPath)
                                                            
                                    return reportMade           
                elif len(dirs) == 0:
                    for filename in files:
                        # global dataResultsFound
                        if ".json" in filename: 
                            dataResultsFoundJSON = read_json.readJSON("./dataFiles/", filename)

                        if ".csv" in filename: 
                            dataResultsFoundCSV = read_csv.readCSV("./dataFiles/", filename)
                            # TODO: ? need to make dataResultsFound appendable, or create multiple dicts in case a data set has more than 1 type of file 

            if sys.platform.startswith('win32'):
                for filename in files:
                    with zipfile.ZipFile(filename,'r') as file:

                        file.extractall("./"+targetDataPath) # extracting files in the dataFiles directory
                        for name in file.namelist():
                            data = file.read(name)

                            if ".json" in name: 
                                print(".json")
                                dataResultsFoundJSON = read_json.readJSON("./dataFiles/", name)
                            
                            if ".csv" in name:
                                dataResultsFoundCSV = read_csv.readCSV("./dataFiles/", name)
                            if ".zip" not in name:
                                if ".png" or ".jpeg" or ".jpg" in name:
                                    file_paths, l = filePath.getPath('')
                                    if len(file_paths) != 0:
                                        reportMade = main.readImage(file_paths, l, targetReportPath)
                                                                
                                        return reportMade 

    # results from parsing + calculations, will be passed into >>  generatePDF.generatePDFReport()
    reportMade = generatePDF.generatePDFReport( targetReportPath, zipFile , None, dataResultsFoundCSV, dataResultsFoundJSON , []) # generate the PDF report

    return reportMade


# copy zip to dataFiles folder and open the zip to get the data files
def openFiles(filename, targetDataPath, targetReportPath):  
    print('data path: ', )
    if os.system("kaggle datasets download -d " + filename) == 0 :
        print(os.getcwd())
        indexOfSlash = filename.find("/") # kaggle names dataset like: [creator of dataset]/[name of dataset]
        zip = filename[(indexOfSlash+1):len(filename)]
        file1 = os.access(zip, os.F_OK)

        print(targetDataPath + " : ",file1, zip)
        # checking for macOS or linux
        if sys.platform.startswith('darwin') | sys.platform.startswith('linux'):
            for  root, dirs, files in os.walk(os.getcwd()):
                # print('files in app:', files)
                # print('dirs in app: ', dirs)
                # print('root in app: ', root)
                for f1 in files:
                    if '.zip' in f1:
                        print('zipfile', f1)
                        with zipfile.ZipFile(f1,'r') as file:
                            print('file to unzip', file)
                            print("getcwd + dataFiles", os.getcwd(), "dataFiles")
                            temp_target = os.path.join(os.getcwd(), "dataFiles")
                            print("temp_target", temp_target)
                            file.extractall(temp_target)
                            break

        # checking for windows
        if sys.platform.startswith('win32'):
            #if makeFilesDir():
            os.system("copy " + zip + ".zip "+ targetDataPath) # copy to dataFiles folder

        time.sleep(3)
        

        for root, dirs, files in os.walk(targetDataPath): # find the .zip file in the folder
            print(dirs)
            print(files)
            for fn in files:

                #checking for macOS or linux
                if sys.platform.startswith('darwin') | sys.platform.startswith('linux'):
                    print("open "+ targetDataPath + "/" + zip + ".zip")
                    os.system("open " + zip + ".zip") # open the file in a designated folder so we know where the files are!

                #checking for windows
                if sys.platform.startswith('win32'):
                    os.system("start dataFiles " + zip + ".zip") # open the file in a designated folder so we know where the files are!
        reportMade = findReadableFiles(zip, targetReportPath)
        return reportMade

def startCommands(filenameToDownload, targetReportPath, targetDataPath):

    filename = filenameToDownload
    time.sleep(3)
    if filename is not None:
        print('filename in filenameReady', filename)

        zipFile = openFiles(filename, targetDataPath) # save zipFiles so it can be accessed in findReadableFiles()
        print('zipFile', zipFile)
        time.sleep(7) # >>>>> protects from multithreading woes :,(
    
    if findReadableFiles(filename, targetReportPath, targetDataPath):  # >>>>> protects from multithreading woes :,(
    # remove the dataFiles folder
        try:
            # shutil.rmtree("./dataFiles/") # deleting the temp directory
            os.remove(zipFile + ".zip")
        except:
            x = 0
         # delete original downloaded zip file
        return True
    else:
        try:
            # shutil.rmtree("./dataFiles/") # deleting the temp directory
            os.remove(zipFile + ".zip")
        except:
            x = 0
        return False