import numpy as np
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, LSTM, Dropout, Activation
from sklearn.preprocessing import MinMaxScaler
import sys

if len(sys.argv) < 1:
	exit(1)

filename = sys.argv[1]	

with open(filename, 'r') as fp:
	usage = np.array([line.strip().split(',') for line in fp.readlines()], dtype=int)

scaler = MinMaxScaler()
scaled = scaler.fit_transform(usage)


test_size = int(len(scaled)*0.7)
x_train = scaled[:test_size,0:2]
y_train = scaled[:test_size,2:]
x_test = scaled[test_size:,0:2]
y_test = scaled[test_size:,2:]

x_train  = x_train.reshape(-1, 1, 2)
y_train  = y_train.reshape(-1, 1, 2)
x_test  = x_test.reshape(-1, 1, 2)
y_test  = y_test.reshape(-1, 1, 2)


model = Sequential()
model.add(LSTM(50, input_shape=(1, 2), return_sequences=True))
model.add(LSTM(50))
model.add(Dense(2))
model.compile(loss='mean_squared_error', optimizer="adam ", metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=1, epochs=100)

#model.save("mymodel")
#model = load_model('mymodel')

# predictions = model.predict(x_test)

# print(predictions)

# rmse = np.sqrt(np.mean((predictions-y_test)**2))

# print(rmse)