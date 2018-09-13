# coding: utf-8
import input_data as datain
datain.out2csv
datain.out2csv()
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import PlaintextCorpusReader
import random
mesage_corpus = PlaintextCorpusReader('./', ['spam_data.csv', 'ham_data.csv'])
all_message = mesage_corpus.words()
all_message
def massage_feature(word,num_letter=1):
    return {'feature':word[-num_letter:]}
labels_name = ([(massage,'垃圾') for massage in message_corpus.words('soam.csv')]+[(massage,'正常') for massage in message_corpus.words('normal.csv')])
random.seed(7)
random.shuffle(labels_name)
message_corpus = PlaintextCorpusReader('./', ['spam_data.csv', 'ham_data.csv'])
labels_name = ([(massage,'垃圾') for massage in message_corpus.words('soam.csv')]+[(massage,'正常') for massage in message_corpus.words('normal.csv')])
random.seed(7)
random.shuffle(labels_name)
labels_name = ([(massage,'垃圾') for massage in message_corpus.words('spam_data.csv')]+[(massage,'正常') for massage in message_corpus.words('ham_data.csv')])
random.seed(7)
random.shuffle(labels_name)
from nltk.classify import accuracy as nltk_accuracy
featuresets = [(massage_feature(n),massage) for (n,massage) in labels_name]
train_set,test_set = featuresets[2000:],featuresets[:2000]
classifier = NaiveBayesClassifier.train(train_set)
rint('结果准确率：',str(100*nltk_accuracy(classifier,test_set))+str('%'))
print('结果准确率：',str(100*nltk_accuracy(classifier,test_set))+str('%'))
get_ipython().run_line_magic('save', 'here 1-31')
