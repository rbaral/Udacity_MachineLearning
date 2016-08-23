#!/usr/bin/python

import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    #check the size of the parameters
    #print len(predictions), len(ages), len(net_worths)
    #now find the difference between the predictions and the actual net_worth
    errorArr = predictions - net_worths
    # get the 90% of the elements in the predictions that have small difference
    elementsToRemove = 0.1 *len(predictions)
    #get the top 10 error elements' index after flattening the nd array (errorArr) to 1-d array
    top10DifferenceIndex = np.argpartition(errorArr.flatten(), -elementsToRemove)[-elementsToRemove:]
    # get the other error elements' index
    otherDifferenceIndex = np.setdiff1d(np.arange(len(errorArr)), top10DifferenceIndex)
    #print top10DifferenceIndex
    #print otherDifferenceIndex
    # The format of cleaned_data should be a list of tuples,
    # where each tuple has the form (age, net_worth, error).
    # now remove the elements at the indices - top10DifferenceIndex from the age,  net_worth, and error ndarrays
    errorArr = np.delete(errorArr, top10DifferenceIndex, axis=0)
    ages = np.delete(ages, top10DifferenceIndex, axis=0)
    net_worths = np.delete(net_worths, top10DifferenceIndex, axis=0)
    #convert the np array to tuples
    errorArr = errorArr.flatten()
    ages = ages.flatten()
    net_worths = net_worths.flatten()
    #print len(ages), len(net_worths), len(errorArr)
    cleaned_data = []
    cleaned_data.append(tuple(ages))
    cleaned_data.append(tuple(net_worths))
    cleaned_data.append(tuple(errorArr))

    return cleaned_data

