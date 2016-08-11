#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np
import math

enron_data = pickle.load(open("../../../../data/final_project_dataset.pkl", "r"))

#read the attributes of the enron POIs
def readPOIDataset():
    # no. of points/ person in the dataset
    #print len(enron_data)
    #print enron_data
    #no. of attributes for each user
    #print len(enron_data[enron_data.keys()[0]])
    # get the attributes of all the person
    attribs = np.array(enron_data.values())
    names = np.array(enron_data.keys())
    #print len(filter(lambda attrib:attrib['poi'] ==True, attribs))
    return names, attribs

#read the number of pois from the name file
def readPOICount():
    with open("../../../../data/poi_names.txt", "r") as poinamefile:
        readLines = poinamefile.readlines()
    #skip the header and empty line
    readLines = readLines[2:]
    # check if every entry is unique
    poinames = np.array(readLines)
    return len(np.unique(poinames))

#get attribute of a user
def getAttrib(userName, attribName):
    userNames, userAttribs = readPOIDataset()
    #access the userName index to get the attribute
    #print userNames
    #print userAttribs
    oneUserAttribute = userAttribs[np.where(np.char.lower(userNames)==np.char.lower(userName))[0]]
    print oneUserAttribute
    return oneUserAttribute[0][attribName]

#get the users with figure in salary, and known email address
def countQuantSalAndEmail():
    userNames, userAttribs = readPOIDataset()
    print userAttribs
    quantSalCount = len(filter(lambda attrib: not attrib['salary']=='NaN', userAttribs))
    validEmailCount = len(filter(lambda attrib: not attrib['email_address']=='NaN', userAttribs))
    return quantSalCount,validEmailCount

#no. of people who have quantifiable attribs and NaN attributes
def countQuantAttributes(attribName):
    userNames, userAttribs = readPOIDataset()
    quantAttribs = len(filter(lambda attrib: not attrib[attribName]=='NaN', userAttribs))
    return quantAttribs,len(userAttribs)-quantAttribs

# no. of POIs with quantifiable and NaN attributes
def countQuantAttributesForPOI(attribName):
    userNames, userAttribs = readPOIDataset()
    poiAttribs = (filter(lambda attrib:attrib['poi'] ==True, userAttribs))
    print poiAttribs
    quantAttribs = len(filter(lambda attrib: not attrib[attribName]=='NaN', poiAttribs))
    return quantAttribs,len(poiAttribs)-quantAttribs
if __name__=="__main__":
    #readPOIDataset()
    #readPOICount()
    #print getAttrib("Prentice James", "total_stock_value")
    #print getAttrib("Colwell Wesley", "from_this_person_to_poi")
    #print getAttrib("Skilling Jeffrey K","total_payments")
    #print getAttrib("Fastow Andrew S","total_payments")
    #print getAttrib("Lay Kenneth L","total_payments")
    #quantSalCount,validEmailCount = countQuantSalAndEmail()
    #print quantSalCount, validEmailCount
    print countQuantAttributes("total_payments")
    #print countQuantAttributesForPOI("total_payments")



