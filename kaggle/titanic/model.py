import numpy as np
import pandas as pd
import keras
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras.optimizers import RMSprop
import preprocessing
data, truth = preprocessing.titanic_data()
def init_model():
    global seq
    seq = Sequential()
    seq.add(Dense(32,kernel_initializer='uniform',input_shape=(8,)))   
    seq.add(Dense(32))  
    seq.add(Dense(2,activation='softmax'))    
    rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)    
    seq.compile(optimizer='sgd',loss='mse',metrics=['accuracy'])

def train(data=data, truth=truth):
    seq.fit(data, truth, epochs=2000, validation_split=0.05, batch_size=20)
    seq.save('model.h5')

def predict(data=data):
    prediction = seq.predict(data)
    return prediction

def one_hot(e):
    if e[0] < e[1]:
        return [0,1]
    else:
        return [1,0]

def convert_one_hot(e):
    if e[0] < e[1]:
        return 1
    else:
        return 0

def accurate_rate(prediction, truth=truth):
    prediction = list(map(one_hot, prediction))
    truth = list(map(one_hot, truth))
    count = 0
    for (x,y) in zip(prediction, truth):
        if x == y:
            count += 1
    print("accurate rate:{}".format(count/891.0))

def out_csv(prediction):
    preditction = list(map(one_hot, prediction))
    out = pd.DataFrame(columns=['PassengerId', 'Survived']);
    out["PassengerId"] = [x for x in range(892,1310)]
    out["Survived"] = list(map(convert_one_hot, prediction))
    out.to_csv("prediction.csv", index=False)
    print("out csv done")
