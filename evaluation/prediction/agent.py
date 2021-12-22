import numpy as np
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, LSTM, Dropout, Activation
import sys

from tensorflow.python.keras.backend import dtype


if len(sys.argv) < 1:
	exit(1)

filename = sys.argv[1]	

with open(filename, 'r') as fp:
	usage = np.array([line.strip().split(',') for line in fp.readlines()], dtype=int)

test_size = int(len(usage)*0.7)
x_train = usage[:test_size,0:2]
y_train = usage[:test_size,2:]
x_test = usage[test_size:,0:2]
y_test = usage[test_size:,2:]

x_train  = x_train.reshape(-1, 1, 2)
y_train  = y_train.reshape(-1, 1, 2)
x_test  = x_test.reshape(-1, 1, 2)
y_test  = y_test.reshape(-1, 1, 2)

model = Sequential()
model.add(LSTM(300, input_shape=(1, 2), return_sequences=True))
model.add(Dropout(0.2)) 
model.add(LSTM(250))
model.add(Dropout(0.2))
model.add(Dense(175))
model.add(Dense(2))
model.compile(loss='mean_squared_error', optimizer="adam")

model.fit(x_train, y_train, batch_size=1, epochs=100)

# model.save("mymodel")
#model = load_model('mymodel')

predictions = model.predict(x_test)

print(predictions)

rmse = np.sqrt(np.mean((predictions-y_test)**2))

print(rmse)