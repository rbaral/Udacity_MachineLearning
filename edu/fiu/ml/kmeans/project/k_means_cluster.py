#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../../tools/")
from feature_format import featureFormat, targetFeatureSplit


def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../../../../../data/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

# finds the max and min values of sal and stock from the data set
def findMaxMinValues():
    #get the max and min value for exercised stock options
    maxStock = 0
    minStock = 0
    stockVallist = []
    salValList = []
    for key in data_dict.keys():
        if not data_dict[key]['salary']=="NaN":
            salValList.append(data_dict[key]['salary'])
        if not data_dict[key]['exercised_stock_options']=="NaN":
            stockVallist.append(data_dict[key]['exercised_stock_options'])
            if data_dict[key]['exercised_stock_options'] > maxStock:
                maxStock = data_dict[key]['exercised_stock_options']
            if data_dict[key]['exercised_stock_options'] < minStock:
                minStock = data_dict[key]['exercised_stock_options']

    #print maxStock, minStock
    #print stockVallist
    #print max(stockVallist), min(stockVallist)
    #print max(salValList), min(salValList)
    return max(stockVallist), max(salValList), min(stockVallist), min(salValList)


# clusters using two features with scaled values
def cluster2FeaturesWithScaling():
    ### the input features we want to use
    ### can be any key in the person-level dictionary (salary, director_fees, etc.)
    feature_1 = "salary"
    feature_2 = "exercised_stock_options"
    poi  = "poi"
    features_list = [poi, feature_1, feature_2]
    #scale the values before creating the data
    maxStock, maxSal, minStock, minSal = findMaxMinValues()

    for key in data_dict.keys():
        if not data_dict[key]['exercised_stock_options']=="NaN":
            scaledStock = float(float(data_dict[key]['exercised_stock_options']) - float(minStock))/float(float(maxStock) - float(minStock))
            data_dict[key]['exercised_stock_options'] = "%.3f" % scaledStock
            print data_dict[key]['exercised_stock_options']
        if not data_dict[key]['salary']=="NaN":
            print data_dict[key]['salary']
            scaledSal = float(float(data_dict[key]['salary']) - float(minSal))/float(float(maxSal) - float(minSal))
            data_dict[key]['salary'] = "%.3f" % scaledSal
            print data_dict[key]['salary']

    data = featureFormat(data_dict, features_list )
    poi, finance_features = targetFeatureSplit( data )

    ### in the "clustering with 3 features" part of the mini-project,
    ### you'll want to change this line to
    ### for f1, f2, _ in finance_features:
    ### (as it's currently written, the line below assumes 2 features)
    #print finance_features
    for f1, f2 in finance_features:
        plt.scatter( f1, f2)
    plt.show()

    ### cluster here; create predictions of the cluster labels
    ### for the data and store them to a list called pred
    from sklearn.cluster import KMeans
    estimators = {'k_means_2': KMeans(n_clusters=2)}
    estimators['k_means_2'].fit(data)
    pred = estimators['k_means_2'].predict(data)

    ### rename the "name" parameter when you change the number of features
    ### so that the figure gets saved to a different file
    try:
        Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
    except NameError:
        print "no predictions object named pred found, no clusters to plot"

# clusters using two features
def cluster2Features():
    ### the input features we want to use
    ### can be any key in the person-level dictionary (salary, director_fees, etc.)
    feature_1 = "salary"
    feature_2 = "exercised_stock_options"
    poi  = "poi"
    features_list = [poi, feature_1, feature_2]
    data = featureFormat(data_dict, features_list )
    poi, finance_features = targetFeatureSplit( data )

    ### in the "clustering with 3 features" part of the mini-project,
    ### you'll want to change this line to
    ### for f1, f2, _ in finance_features:
    ### (as it's currently written, the line below assumes 2 features)
    #print finance_features
    for f1, f2 in finance_features:
        plt.scatter( f1, f2)
    plt.show()

    ### cluster here; create predictions of the cluster labels
    ### for the data and store them to a list called pred
    from sklearn.cluster import KMeans
    estimators = {'k_means_2': KMeans(n_clusters=2)}
    estimators['k_means_2'].fit(data)
    pred = estimators['k_means_2'].predict(data)

    ### rename the "name" parameter when you change the number of features
    ### so that the figure gets saved to a different file
    try:
        Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
    except NameError:
        print "no predictions object named pred found, no clusters to plot"

# clusters using three features
def cluster3Features():
    ### the input features we want to use
    ### can be any key in the person-level dictionary (salary, director_fees, etc.)
    feature_1 = "salary"
    feature_2 = "exercised_stock_options"
    #add third feature 'total_payments'
    feature_3 = "total_payments"
    poi  = "poi"
    features_list = [poi, feature_1, feature_2, feature_3]
    data = featureFormat(data_dict, features_list )
    poi, finance_features = targetFeatureSplit( data )


    ### in the "clustering with 3 features" part of the mini-project,
    ### you'll want to change this line to
    ### for f1, f2, _ in finance_features:
    ### (as it's currently written, the line below assumes 2 features)
    print finance_features
    for f1, f2, f3 in finance_features:
        plt.scatter( f1, f2, f3 )
    plt.show()

    ### cluster here; create predictions of the cluster labels
    ### for the data and store them to a list called pred
    from sklearn.cluster import KMeans
    estimators = {'k_means_2': KMeans(n_clusters=2)}
    estimators['k_means_2'].fit(data)
    pred = estimators['k_means_2'].predict(data)



    ### rename the "name" parameter when you change the number of features
    ### so that the figure gets saved to a different file
    try:
        Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
    except NameError:
        print "no predictions object named pred found, no clusters to plot"


if __name__=="__main__":
    print "started main method"
    #cluster2Features()
    cluster2FeaturesWithScaling()
    #cluster3Features()
    #findMaxMinValues()
