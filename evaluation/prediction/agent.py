import numpy as np
from numpy import dtype
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, LSTM, Dropout, Activation
from sklearn.preprocessing import MinMaxScaler
import sys
import pandas as pd

if len(sys.argv) < 1:
	exit(1)

filename = sys.argv[1]	

i = 0
usage = np.zeros((1439, 12), dtype=int)
with open(filename, 'r') as fp:
	for line in fp.readlines():
		line = line.replace('\n', '')
		line = line.split(',')
		for j in range(len(line)):
			usage[i][j]= int(line[j])
		i +=1		


scaler = MinMaxScaler()
scaled = scaler.fit_transform(usage)

test_size = int(len(scaled)*0.7)
x_train = scaled[:test_size,0:6]
y_train = scaled[:test_size,6:]
x_test = scaled[test_size:,0:6]
y_test = scaled[test_size:,6:]

x_train  = x_train.reshape(-1, 1, 6)
y_train  = y_train.reshape(-1, 1, 6)
x_test  = x_test.reshape(-1, 1, 6)
y_test  = y_test.reshape(-1, 1, 6)

model = Sequential()
model.add(LSTM(50, input_shape=(1, 6), return_sequences=True))
model.add(LSTM(50))
model.add(Dense(6))
model.compile(loss='mean_squared_error', optimizer="adam", metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=1, epochs=100)

model.save("mymodel")
#model = load_model('mymodel')

# predictions = model.predict(x_test)

# print(predictions)

# rmse = np.sqrt(np.mean((predictions-y_test)**2))

# print(rmse)