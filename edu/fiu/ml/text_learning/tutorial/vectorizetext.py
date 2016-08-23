__author__ = 'rbaral'

def bagOfWords():
    print "started bagOfWords"
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer()
    string1 = "Hi Johny, you are simply great"
    string2 = "Hi Sarah thanks for the great great great surprise"
    string3 = "Hi Sarah that will be simply great"
    email_list = [string1, string2, string3]
    # fit the list of words to the vectorizer
    bag_of_words = vectorizer.fit(email_list)
    #transform to count each tokens
    bag_of_words =vectorizer.transform(email_list)
    print bag_of_words
    # count the index of this word in the bag
    print vectorizer.vocabulary_.get("great")
    print vectorizer.get_feature_names()


def testtfidf():
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = TfidfVectorizer()
    string1 = "Hi Johny, you are simply great"
    string2 = "Hi Sarah thanks for the great great great surprise"
    string3 = "Hi Sarah that will be simply great"
    string4 = "Hi Sarah that will be great"
    email_list = [string1, string2, string3, string4]
    bow = tfidf.fit(email_list)
    bow = tfidf.transform(email_list)
    print bow
    print bow.shape
    print bow.size


if __name__=="__main__":
    print "main started"
    #bagOfWords()
    testtfidf()