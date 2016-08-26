#!/usr/bin/python

import os
import os.path
import pickle
import re
import sys

sys.path.append( "../../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        if temp_counter < 200 or 1<2: # can remove this line totally for the full dataset
            #the maildir is in different path because it makes the project opening slower in IDE
            mailDir = "C:\\Users\\rbaral\\Documents\\GitHub\\ud120-projects"
            path = os.path.join(mailDir, path[:-1])
            path = path.replace("/","\\")
            print path

            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            emailText = parseOutText(email)

            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            avoidWordsList = ["sara", "shackleton", "chris", "germani"]
            # the longer list is used for the mini project on feature selection
            avoidWordsList = ["sara", "shackleton", "chris", "germani", "sshacklensf", "cgermannsf"]

            for w in avoidWordsList:
                emailText = emailText.replace(w, "")

            word_data.append(emailText)
            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name.lower()=='sara':
                from_data.append(0)
            if name.lower()=='chris':
                from_data.append(1)

            email.close()

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

#word_data[152]
#print word_data[152]

### in Part 4, do TfIdf vectorization here

#Transform the word_data into a tf-idf matrix using the sklearn TfIdf transformation.
# Remove english stopwords.
#now find the number of unique words in the list
from sklearn.feature_extraction.text import TfidfVectorizer
tfidfTransformer = TfidfVectorizer(stop_words="english")
tfidfwords = tfidfTransformer.fit(word_data)
tfidfwords = tfidfTransformer.transform(word_data)
print tfidfwords.shape
print len(tfidfTransformer.get_feature_names())

print "34597th word is:",tfidfTransformer.get_feature_names()[34597]

