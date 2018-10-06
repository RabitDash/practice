import numpy as np
import pandas as pd
import keras
import preprocessing

data, truth = preprocessing.data_matrix()

seq = keras.models.Sequential()
seq.add(keras.layers.Dense(5,use_bias=False, input_shape=(8,)))
#seq.add(keras.layers.Dropout(0.5))
seq.add(keras.layers.Activation('softmax'))
seq.compile(optimizer='adadelta', loss='binary_crossentropy')
seq.fit(data, truth, epochs=1000, validation_split=0.05)
prediction = seq.predict(data)
print(prediction)
