import pandas as pd
import numpy as np
def normalize(pdframe):
    return (pdframe-pdframe.min())/(pdframe.max()-pdframe.min())

def preprocessing(path):
    train_data = pd.read_csv(path)

    train_data.Cabin.fillna(train_data.Cabin.mode()[0], inplace=True)

    train_data.Sex.replace({'female':0, 'male':1}, inplace=True)

    fuck = []
    for x in train_data.Name:
        tmp = x.split(', ')[1]
        a = tmp.split('.')[0]
        fuck.append(a)
    train_data.Name = fuck
    train_data.Name = train_data.Name.astype("category")
    train_data.Name = train_data.Name.cat.codes

    train_data.Embarked = train_data.Embarked.astype("category").cat.codes

    train_data.Age.fillna(-1, inplace=True)
    fuck = []
    for x in train_data.Age:
        if x >= 0 and x <=6:
            fuck.append(0)
        elif x > 6 and x <= 17:
            fuck.append(1)
        elif x > 17 and x <= 40:
            fuck.append(2)
        elif x> 40 and x <= 65:
            fuck.append(3)
        elif x > 65:
            fuck.append(4)
        elif x < 0:
            fuck.append(-1)
    train_data.Age = fuck
    train_data.Age = train_data.Age.astype("category").cat.codes

    # count of family numbers
    train_data['FaNum'] = train_data['SibSp'] + train_data['Parch']

    # normalization
    train_data.Fare = normalize(train_data.Fare)
    train_data.Age = normalize(train_data.Age)
    train_data.Pclass = normalize(train_data.Pclass)
    # train_data.Cabin = normalize(train_data.Cabin)
    train_data.FaNum = normalize(train_data.FaNum)
    train_data.Embarked = normalize(train_data.Embarked)
    train_data.SibSp = normalize(train_data.SibSp)
    train_data.Parch = normalize(train_data.Parch)
    # train_data.Sex
    return train_data

def data_matrix(path):
    train_data = preprocessing(path)
    '''
    params: None
    return: (matrix, survive[one_hot])
    '''
    features = ['Fare', 'Age', 'Pclass', 'FaNum', 'Embarked', 'SibSp', 'Parch', 'Sex']
    matrix = pd.DataFrame()
    for _ in features:
        matrix[_] = train_data[_]
    matrix = matrix.values
    return matrix


def titanic_data():
    train_data = preprocessing("train.csv")
    matrix = data_matrix("train.csv")
    def one_hot(x):
        if x is 0:
            return [1,0]
        else:
            return [0,1]
    survive = map(one_hot, train_data.Survived)
    survive = np.array(list(survive))
    return (matrix, survive)
