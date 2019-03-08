import pandas as pd
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pandas import DataFrame
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
df0 = pd.read_csv('ham.csv')
df1 = pd.DataFrame(df0)
df2 = pd.read_csv('spam.csv')
df3 = pd.DataFrame(df1)
df4 = df1.append(df2, ignore_index = True)
df4 = shuffle(df4)
def remove(data) :
    stopwords = nltk.corpus.stopwords.words('english')
    b = [w for w in data if w.isalpha()]
    c = [w for w in b if w.lower() not in stopwords]
    return set(c)
messages = df4['message']
classes = df4['class']
vectorizer = TfidfVectorizer()
x_train, x_test, y_train, y_test = train_test_split(messages, classes, test_size=0.5, random_state=1)
x_trainv = vectorizer.fit_transform(x_train)
mlnb = MultinomialNB()
mlnb.fit(x_trainv, y_train)
x_testv = vectorizer.transform(x_test)
real = np.array(y_test)
predictions = mlnb.predict(x_testv)
print(predictions)
a = len(predictions)
c = 0
for e in range (len(predictions)) :
    if predictions[e] == real[e] :
        c = c+1
print(c)
acc = (c / a)*100
print(acc)
