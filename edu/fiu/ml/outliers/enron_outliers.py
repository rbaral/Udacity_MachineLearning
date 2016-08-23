#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import numpy as np
import math
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../../../../data/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
del data_dict['TOTAL']
data = featureFormat(data_dict, features)
flt = data.flatten()
for key in data_dict.keys():
    #print key
    for val in data_dict[key]:
        if (val=='salary' or val =='bonus') and data_dict[key][val] is not 'NaN':
            if data_dict[key]['salary']>1000000 and data_dict[key]['bonus']>= 5000000:
                print key, val,data_dict[key][val]

#max2Index = np.argpartition(flt, -4)[-4:] # get the index of 2 maximum values
#print flt[max2Index[0]], flt[max2Index[1]], flt[max2Index[2]], flt[max2Index[3]]
#visualization of the data
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()



