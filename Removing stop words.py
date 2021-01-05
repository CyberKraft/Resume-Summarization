import pandas as pd
import string
import re
import nltk

pd.set_option('display.max_colwidth', 100)
data = pd.read_csv("resume.txt", sep='\t', header = None)
data.columns = ['msg']

#print(data.head())

def remove_punctuation(txt):
    txt_nopunt = "".join([c for c in txt if c not in string.punctuation])
    return txt_nopunt

data['msg_clean'] = data['msg'].apply(lambda x: remove_punctuation(x))
#print(data.head())


#Tokenization

def tokenize(txt):
    tokens = re.split('\W+', txt)
    return tokens

data['msg_clean_tokenized'] = data['msg_clean'].apply(lambda x: tokenize(x.lower()))
#print(data.head())


#Removing stop words

stopwords = nltk.corpus.stopwords.words('english')
#print(stopwords[0:10])

def remove_stopwords(txt_tokenized):
    txt_clean = [word for word in txt_tokenized if word not in stopwords]
    return txt_clean


data['msg_no_sw'] = data['msg_clean_tokenized'].apply(lambda x: remove_stopwords(x))
print(data.head())