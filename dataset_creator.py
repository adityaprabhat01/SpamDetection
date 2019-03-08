import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def remove(data) :
    stopwords = nltk.corpus.stopwords.words('english')
    b = [w for w in data if w.isalpha()]
    c = [w for w in b if w.lower() not in stopwords]
    return set(c)

for dirs, subdirs, files in os.walk('/home/aditya/Desktop/part1') :
    if (os.path.split(dirs)[1] == 'ham') :
        #print(dirs, subdirs, len(files))
        for filename in files :
            raw = open(os.path.join(dirs, filename)).read()
            a = word_tokenize(raw)
            b = remove(a)
            final = ' '.join(b)
            text_file = open("ham.csv", "a")
            text_file.write(final + ',1\n')
            text_file.close()
    if (os.path.split(dirs)[1] == 'spam') :
        #print(dirs, subdirs, len(files))
        for filename in files :
            raw = open(os.path.join(dirs, filename)).read()
            a = word_tokenize(raw)
            b = remove(a)
            final = ' '.join(b)
            text_file = open("spam.csv", "a")
            text_file.write(final + ',0\n')
            text_file.close()
