# python program to read JSON file
import os
import json
import pandas as pd
import numpy
from string import punctuation

def readJSON(path, filename):

    # TODO: need to create a dictionary for categories to search the file for and deal with the possibility that they are a string (ex: 'location'= "Bangalore") or an integer/float (ex: latitude: 120, longitude: 50])
    LocCount = 0
    dataList = {}
    if ".json" in filename:
        # opening JSON file
        df = None
        cols = None
        try: # need to walk through dataFiles to check if files are in folders
            filedata = [json.loads(line) for line in open(path+ "/"+filename, 'r', encoding = 'utf-8')]
            df = pd.DataFrame(filedata)
            cols = df.columns
        except:
            for dirs in os.walk(path):
                for d in dirs:
                    if isinstance(d, str):
                        try:
                            filedata = [json.loads(line) for line in open(d+ "/" +filename, 'r', encoding = 'utf-8')]
                            df = pd.DataFrame(filedata)
                            cols = df.columns
                        except:
                            print("couldn't open", d+filename)
            if df is None or cols is None:
                return                

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

        # i is label, valueFound is value to add to dict
        def addValueToDict(i, valueFound):
            # if/elif statements check which label was found and save the value to the corresponding dict with the count as the value in the hashmap/dict
            if 'location' in i[0].lower():
                if "." not in valueFound:
                    if Location.get(valueFound) is not None:
                        count = Location.get(valueFound)+1
                        Location.update({valueFound: count})
                    else:
                        Location.update({valueFound:1})
            if 'age' in i[0].lower():
                if Age.get(valueFound) is not None:
                    count = Age.get(valueFound)+1
                    Age.update({valueFound: count})
                else:
                                Age.update({valueFound:1})
            if 'gender' in i[0].lower():
                if Gender.get(valueFound) is not None:
                    count = Gender.get(valueFound)+1
                    Gender.update({valueFound: count})
                else:
                    Gender.update({valueFound:1})
            if 'ethnicity' in i[0].lower():
                if Ethnicity.get(valueFound) is not None:
                    count = Ethnicity.get(valueFound)+1
                    Ethnicity.update({valueFound: count})
                else:
                    Ethnicity.update({valueFound:1})
            if 'religion' in i[0].lower():
                if Religion.get(valueFound) is not None:
                    count = Religion.get(valueFound)+1
                    Religion.update({valueFound: count})
                else:
                    Religion.update({valueFound:1})
            if 'income' in i[0].lower():
                if Income.get(valueFound) is not None:
                    count = Income.get(valueFound)+1
                    Income.update({valueFound: count})
                else:
                    Income.update({valueFound:1})
            if 'education' in i[0].lower():
                if Education.get(valueFound) is not None:
                    count = Education.get(valueFound)+1
                    Education.update({valueFound: count})
                else:
                    Education.update({valueFound:1})
        
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
                                                    valueF = bDict['points'][labelIndex][0]['text']
                                                    valueF = valueF.lstrip(punctuation)
                                                    valueF = valueF.rstrip(punctuation) # strip the value of the label of leading/trailing punctuation
                                                    try:                                                                
                                                        valueF = float(valueF) # if location is a number, we can parse it so we can analyze it later
                                                    except:
                                                        valueF = str(valueF)

                                                    addValueToDict(bDict['label'][labelIndex], valueF )
                                                    
        else: # for .json format: {'keyword':{}, 'keyword':{ 'keyword':{}, 'keyword':{}}} 
            for col in cols:
                for val in df[col]:
                    if col.lower() in demographicsToSearch:
                        addValueToDict(col.lower(), val)
                    elif isinstance(val, list):
                        for lst in val:
                            if isinstance(lst, dict):
                                colsI = lst.keys()
                                for ii in colsI:
                                    print('i', ii)
                                    if ii.lower() in demographicsToSearch:
                                        addValueToDict(ii, valueF)
                            elif lst in demographicsToSearch:
                                valueF = val.get(lst)
                                addValueToDict(lst, valueF)

            
        #TODO: need to write support for this format
    # return dict of all labels and their dicts

    # check if any values to add to dict we want to return to runTerminalCommands
    dictToReturn = {}
    if len(Location) > 0:
        dictToReturn.update({'Location': Location})
    if len(Ethnicity) > 0:
        dictToReturn.update({'Ethnicity': Ethnicity})
    if len(Gender) > 0:
        dictToReturn.update({'Gender': Gender})
    if len(Religion) > 0:
        dictToReturn.update({'Religion': Religion})
    if len(Income) > 0:
        dictToReturn.update({'Income': Income})
    if len(Age) > 0:
        dictToReturn.update({'Age': Age})
    if len(Education) > 0:
        dictToReturn.update({'Education': Education})
        
    return dictToReturn

