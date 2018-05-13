# coding: utf-8
import csv
import pandas as pd
import string as s
from nltk.corpus import stopwords
import re

spamdata_T1csv = "./spamdata_T1.csv"
spamdata_T2csv = "./spamdata_T2.csv"
testdatacsv    = "./testdata.csv"

def rmstopwords(string):
    tmp = string.split(' ')
    for x in tmp:
        if x in stopwords.words('English'):
            tmp.remove(x)
    return ' '.join(tmp)

def rmpunc(string):
    tmp = string.split(' ')
    shit = []
    for x in tmp:
        mt = x.maketrans(s.punctuation, len(s.punctuation) * ' ')
        x = x.translate(mt)
        x = re.sub("\s*", '', x)
        shit.append(x)
    return ' '.join(shit)


#数据清洗
def read_data_sets(filename):
    with open(filename, 'rb') as f:
        string = str(f.read())
        string = string.replace("b\'", '')
        strlist = string.split("\\r\\n")
        data = []
        for string in strlist:
            string = string.replace('\"', '')
            string = string.replace('\\', '')
            string = string.replace('&lt;#&gt;', '')
            string = string.strip() #去掉多余空格

            if string.find("spam") is 0:
                tmpdata = string.split("spam")[1]
                tmpdata = tmpdata[1::]
                tmpdata = tmpdata.strip()
                tmpdata = rmstopwords(tmpdata)
                tmpdata = re.sub('\d{5,13}', ' tel ', tmpdata)
                tmpdata = re.sub("www.*.com", ' url ', tmpdata)
                tmpdata = rmpunc(tmpdata)
                data.append([1, tmpdata])
            elif string.find("ham") is 0:
                tmpdata = string.split("ham")[1]
                tmpdata = tmpdata[1::]
                tmpdata = tmpdata.strip()
                tmpdata = rmstopwords(tmpdata)
                tmpdata = re.sub('\d{5,13}', ' tel ', tmpdata)
                tmpdata = re.sub("www.*.com", ' url ', tmpdata)
                tmpdata = rmpunc(tmpdata)
                data.append([0, tmpdata])
            elif string is '\'':
                pass
            else:
                string = rmstopwords(string)
                string = re.sub('\d{5,13}', ' tel ', string)
                string = re.sub("www.*.com", ' url ', string)
                string = rmpunc(string)
                data.append(string)
        print("Load {0} done.".format(filename))
        # data = [x[1].replace(s.punctuation, '') for x in data]
        return data


traindata = read_data_sets(spamdata_T2csv)
testdata = read_data_sets(testdatacsv)
predictdata = read_data_sets(spamdata_T1csv)


def out2csv():
    flag = [x[0] for x in traindata]
    content = [x[1] for x in traindata]
    content0 = []
    content1 = []
    flag0 = []
    flag1 = []
    for (x, y) in zip(flag, content):
        if x is 0:
            content0.append(y)
            flag0.append(0)
        elif x is 1:
            content1.append(y)
            flag1.append(1)
    # column_flag0 = pd.Series(flag0)
    column_content0 = pd.Series(content0)
    # save0 = pd.concat([column_flag0,column_content0], axis=1)
    save0 = pd.concat([column_content0], axis=1)
    save0.to_csv("ham_data.csv",encoding='utf-8',header=False,index=False)

    # column_flag1 = pd.Series(flag1)
    column_content1 = pd.Series(content1)
    # save1 = pd.concat([column_flag1, column_content1], axis=1)
    save1 = pd.concat([column_content1], axis=1)
    save1.to_csv("spam_data.csv",encoding='utf-8',header=False,index=False) # 垃圾短信

    flag = [x[0] for x in traindata]
    column_flag = pd.Series(flag)
    content = [x[1] for x in traindata]
    column_content = pd.Series(content)
    save = pd.concat([column_flag, column_content], axis=1)
    save.to_csv("train_data.csv", encoding='utf-8', header=False, index=False)

    content = [x for x in testdata]
    column_content = pd.Series(content)
    save = pd.concat([column_content], axis=1)
    save.to_csv("test_data.csv", encoding='utf-8', header=False, index=False)

    content = [x for x in predictdata]
    column_content = pd.Series(content)
    save = pd.concat([column_content], axis=1)
    save.to_csv("predict_data.csv", encoding='utf-8', header=False, index=False)
