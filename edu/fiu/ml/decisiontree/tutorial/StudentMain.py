#!/usr/bin/python
__author__ = 'rbaral'


""" lecture and example code for decision tree unit """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyDT import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
minsplit = 2
clf1 = classify(features_train, labels_train, minsplit)
minsplit = 50
clf2 = classify(features_train, labels_train, minsplit)
'''
different ways to print the accuracy of the GNB classifier
'''
#print clf1.score(features_test,labels_test) # find the prediction score for the test data
pred1 = clf1.predict(features_test)
from sklearn.metrics import accuracy_score
acc_min_samples_split_2 = accuracy_score(labels_test, pred1)
print acc_min_samples_split_2

#print clf2.score(features_test,labels_test) # find the prediction score for the test data
pred2 = clf2.predict(features_test)
from sklearn.metrics import accuracy_score
acc_min_samples_split_50 = accuracy_score(labels_test, pred2)
print acc_min_samples_split_50
#### grader code, do not modify below this line
prettyPicture(clf1, features_test, labels_test, "test1.png")
output_image("test1.png", "png", open("test1.png", "rb").read())
prettyPicture(clf2, features_test, labels_test, "test2.png")
output_image("test2.png", "png", open("test2.png", "rb").read())