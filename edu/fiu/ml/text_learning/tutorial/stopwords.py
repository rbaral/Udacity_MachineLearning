__author__ = 'rbaral'

# get the stop words from nltk corpus
def getStopWords():
    from nltk.corpus import stopwords
    sw = stopwords.words("english")
    #print len(sw)
    return sw

# get the stem of a given word
def getStemmer(text):
    from nltk.stem.snowball import SnowballStemmer
    stemmer = SnowballStemmer("english")
    return stemmer.stem(text)

#perform tfidf operation
def testTFIDF():
    from sklearn.feature_extraction.text import TfidfVectorizer
    import numpy as np
    sentences = ("The sun is shiny i like the sun","I have been exposed to sun")
    vect = TfidfVectorizer(stop_words="english")
    mat = vect.fit_transform(sentences).toarray()
    '''
    q = mat / vect.idf_
    sums = np.ones((q.shape[0], 1))
    lens = np.ones((q.shape[0], 1))
    for ix in xrange(q.shape[0]):
        sums[ix] = np.sum(q[ix,:])
        lens[ix] = len([x for x in sentences[ix].split() if unicode(x) in vect.get_feature_names()]) #have to filter out stopwords
    sum_to_1 = q / sums
    tf = sum_to_1 * lens
    print tf.shape
    '''
    print vect.get_feature_names()
    print mat.shape

if __name__=="__main__":
    #print getStopWords()
    #print getStemmer("germany")
    #import numpy as np
    #stopWordsList = np.array(getStopWords())
    #testString ="He and I are good friends"
    #testWords = np.array(testString.lower().split(" "))
    #stopWordsFiltered = np.setdiff1d(testWords,stopWordsList)
    #print stopWordsList
    #print stopWordsFiltered
    testTFIDF()

