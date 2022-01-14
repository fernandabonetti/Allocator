from sklearn.preprocessing import MinMaxScaler

pred_target = 100
pred_upper = 200
pred_lower = 50

scaler = MinMaxScaler()
x_test = scaler.fit_transform(x_test)
y_test = scaler.fit_transform(y_test)
model = load_model('mymodel')

i = 0
j = 24


for i in range(200):
	#generate prediction window of size 24
	window = x_test[i:j]
	i = j
	j+=24
	predictions = model.predict(window)
  rmse = np.sqrt(np.mean((predictions-y_test)**2))

	new = pred_target + 120
 	if new < lower or new > upper:
		if abs(request - new) > 50 :
			command = f"kubectl set resources -n {namespace} deployment {container} --requests=cpu={request}m"
			run(command, shell=True)
			cooldown=18
	cooldown-=1		