import model
import preprocessing

model.init_model()
test_data = preprocessing.data_matrix("test.csv")
model.train()
model.accurate_rate(model.predict())
prediction = model.predict(test_data)
model.out_csv(prediction)
