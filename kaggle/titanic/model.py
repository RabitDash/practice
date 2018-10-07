import numpy as np
import pandas as pd
import keras
import preprocessing

data, truth = preprocessing.titanic_data()
def init_model():
    global seq
    seq = keras.models.Sequential()
    seq.add(keras.layers.Dense(2,use_bias=False, input_shape=(8,)))
    seq.add(keras.layers.Dropout(0.05))
    seq.add(keras.layers.Activation('softmax'))
    seq.compile(optimizer='adadelta', loss='binary_crossentropy')

def train(data=data, truth=truth):
    seq.fit(data, truth, epochs=2000, validation_split=0.05)
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
