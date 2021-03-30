# python program to read JSON file
import json

def readJSON(path, filename):

    # TODO: need to create a dictionary for categories to search the file for and deal with the possibility that they are a string (ex: 'location'= "Bangalore") or an integer/float (ex: latitude: 120, longitude: 50])

    data = []
    if "Entity Recognition in Resumes.json" in filename:
        # opening JSON file
        f = open("./dataFiles/"+filename,)

        # returns JSON object as a dictionary
        database = json.load(f)

        # TODO: need to find a way to find all labels in a dataset

        # this particular parsing is what I used for the .json dataset: filename = "dataturks/resume-entities-for-ner"  that is commented out in the runTerminalCommands.py file
        if "Location" in database["annotation"][0]["label"]:
            print(database["content"], database["annotation"])

        # Iterating through the json list
        for data in database.get('annotation'):
            TF = False
            for d in data:
                if TF:
                    print("in trueFalse: !!! ", data.get(d))
                if("Location" in data.get(d)):
                    #TF = True
                    print(d)
                    data.append(d)
        # Closing file
        f.close()
    return data