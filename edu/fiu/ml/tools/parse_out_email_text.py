#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)
        # get the email-sender using the From: keyword
        emailSender = content[0][content[0].index('From:'):content[0].index('From:')+20]

        ### project part 2: comment out the line below
        #print text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        words = text_string.split()
        from nltk.stem import SnowballStemmer
        stemmer = SnowballStemmer("english")

        stemmedWords = []
        for word in words:
            stemmedWords.append(stemmer.stem(word))
        #prepare the new text
        stemmedText = ""
        for word in stemmedWords:
            if len(word.strip())>0: # avoid unnecessary white spaces
                stemmedText+=word.strip()+" "
        words = stemmedText

        #stemmed = [stemmer.stem(w) for w in text_string.split()]
        #words = " ".join(stemmed)

    return words

    

def main():
    ff = open("../text_learning/project/test_email.txt", "r")
    sender, text = parseOutText(ff)
    #print sender
    print text



if __name__ == '__main__':
    main()

