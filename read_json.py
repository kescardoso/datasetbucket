# python program to read JSON file
import json
import pandas as pd
import numpy
from string import punctuation

def readJSON(path, filename):

    # TODO: need to create a dictionary for categories to search the file for and deal with the possibility that they are a string (ex: 'location'= "Bangalore") or an integer/float (ex: latitude: 120, longitude: 50])
    LocCount = 0
    dataList = {}
    if ".json" in filename:
        # opening JSON file (while opening files on windows it's advisable to enter the encoding format)
        filedata = [json.loads(line) for line in open("./dataFiles/"+filename, 'r', encoding = "utf8")]
        # create pandas dataframe
        df = pd.DataFrame(filedata)
        cols = df.columns
        # demographicsToSearch is all of the labels we will look for, and the formats we accept them as
        demographicsToSearch = { 'ethnicity':'str', 'gender':'str', 'religion':'str', 'income':'int', 'age':'int', 'education':'str', 'location':'str'}
        # The next 5 dicts are to store the counts of each value found 
        Location= {}
        Ethnicity = {} 
        Gender = {} 
        Religion = {}
        Income = {}
        Age = {} 
        Education = {}

        # 3 diffterent formats supported: {'root': {dict}} OR {'content': {}, 'annotation':[{'labels':{}},{'points':{}}], 'extras':{}} OR {'keyword':{}, 'keyword':{}, 'keyword':{}}
        if 'root' in cols[0]: # TODO: need to write support for this format
            print('root')
            cols = df[cols[0]].columns
            print("new cols")
            print(cols)
        if 'content' in cols[0]:
            if len(cols) >= 1:
                if 'annotation' in cols[1]:
                    for val in df.values: 
                        # for this format, df.values is each line, containting content, annotation, and extra columns, but we only want the annotation values, which
                        # so the data will be in a numpy.ndarray
                        if isinstance(val, numpy.ndarray):
                                for xi in val: 
                                    #  In this format, 'annotation':[{'labels':{}},{'points':{}}] is the standard, so we only want the annotation list
                                    if isinstance(xi, list):
                                        df2 = pd.DataFrame(xi) # create a new dataframe for the current line, and parse that line as a dict
                                        bDict = df2.to_dict() 
                                        for labelIndex in bDict['label']: # all labels in the dict, which we want to match to our demographicsToSearch dict
                                            if len(bDict['label'][labelIndex]) > 0:
                                                if bDict['label'][labelIndex][0].lower() in demographicsToSearch: # check if this label is a label we want
                                                    valueFound = bDict['points'][labelIndex][0]['text']
                                                    valueFound = valueFound.lstrip(punctuation)
                                                    valueFound = valueFound.rstrip(punctuation) # strip the value of the label of leading/trailing punctuation
                                                    try:                                                                
                                                        valueFound = float(valueFound) # if location is a number, we can parse it so we can analyze it later
                                                    except:
                                                        valueFound = str(valueFound)

                                                    # if/elif statements check which label was found and save the value to the corresponding dict with the count as the value in the hashmap/dict
                                                    if 'Location' in bDict['label'][labelIndex] or 'location' in bDict['label'][labelIndex]:
                                                        if "." not in valueFound:
                                                            if Location.get(valueFound) is not None:
                                                                count = Location.get(valueFound)+1
                                                                Location.update({valueFound: count})
                                                            else:
                                                                Location.update({valueFound:1})
                                                    elif 'Age' in bDict['label'][labelIndex] or 'age' in bDict['label'][labelIndex]:
                                                        if Age.get(valueFound) is not None:
                                                            count = Age.get(valueFound)+1
                                                            Age.update({valueFound: count})
                                                        else:
                                                            Age.update({valueFound:1})
                                                    elif 'Gender' in bDict['label'][labelIndex] or 'gender' in bDict['label'][labelIndex]:
                                                        if Gender.get(valueFound) is not None:
                                                            count = Gender.get(valueFound)+1
                                                            Gender.update({valueFound: count})
                                                        else:
                                                            Gender.update({valueFound:1})
                                                    elif 'Ethnicity' in bDict['label'][labelIndex] or 'ethnicity' in bDict['label'][labelIndex]:
                                                        if Ethnicity.get(valueFound) is not None:
                                                            count = Ethnicity.get(valueFound)+1
                                                            Ethnicity.update({valueFound: count})
                                                        else:
                                                            Ethnicity.update({valueFound:1})
                                                    elif 'Religion' in bDict['label'][labelIndex] or 'religion' in bDict['label'][labelIndex]:
                                                        if Religion.get(valueFound) is not None:
                                                            count = Religion.get(valueFound)+1
                                                            Religion.update({valueFound: count})
                                                        else:
                                                            Religion.update({valueFound:1})
                                                    elif 'Income' in bDict['label'][labelIndex] or 'income' in bDict['label'][labelIndex]:
                                                        if Income.get(valueFound) is not None:
                                                            count = Income.get(valueFound)+1
                                                            Income.update({valueFound: count})
                                                        else:
                                                            Income.update({valueFound:1})
                                                    elif 'Education' in bDict['label'][labelIndex] or 'education' in bDict['label'][labelIndex]:
                                                        if Education.get(valueFound) is not None:
                                                            count = Education.get(valueFound)+1
                                                            Education.update({valueFound: count})
                                                        else:
                                                            Education.update({valueFound:1})
        else:
            x = 0
        #TODO: need to write support for this format
    # return dict of all labels and their dicts
    return {'Location': Location, 'Ethnicity': Ethnicity, 'Gender': Gender, 'Religion': Religion, 'Income':Income, 'Age':Age, 'Education':Education }
       