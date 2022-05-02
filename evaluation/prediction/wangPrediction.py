from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from metricsAPI import Collector
from subprocess import PIPE, run
import json
import numpy as np


ip = "192.168.49.2"
port = "30000"
container = "haproxy-ingress"
namespace = "haproxy-controller"


def getResourceSpecs(spec):
	command = "kubectl get pods -o json -n " + namespace + \
						" | jq \".items[0].spec.containers[0].resources." + spec + "\""

	result = run(command, stdout=PIPE, universal_newlines=True, shell=True)
	
	if len(result.stdout) > 5:
		resource = json.loads(result.stdout)
		if (resource["cpu"][-1:] != "m"):	
			cpu = int(resource["cpu"])
		else:
			cpu = int(resource["cpu"][:-1])

		if (resource["memory"][-1:] != "i"):	
			mem = int(resource["memory"])
		else:
			mem = int(resource["memory"][:-2])
		return cpu, mem


collector = Collector(ip, port, container, namespace)


scaler = MinMaxScaler()

model = load_model('mymodel')

i = 0
j = 24

for i in range(200):
	#generate prediction window of size 24
	
	cpu_usage, mem_usage = collector.get_resource_usage()
	cpu_limit, mem_limit = getResourceSpecs("limits")
	cpu_request, mem_request = getResourceSpecs("requests")

	window = np.array([cpu_request, cpu_usage, cpu_limit, mem_request, mem_usage, mem_limit])
	window  = window.reshape((1, 6))
	window = scaler.fit_transform(window)
	window  = window.reshape((-1, 1, 6))
	prediction = model.predict(window)
	prediction = scaler.inverse_transform(prediction)
	cpu_target = prediction[0][1] + 120
	cpu_upper = prediction[0][2]
	cpu_lower = prediction[0][0]
	print(cpu_target)
	print(cpu_request, cpu_limit, cpu_usage)
	cooldown = 18
	if cpu_lower < cpu_request or cpu_upper > cpu_limit: 
		if abs(cpu_request - cpu_target) > 50 :
			cpu_request = cpu_target
			command = f"kubectl set resources -n {namespace} deployment {container} --requests=cpu={cpu_request}m --limits=cpu={cpu_upper}m"
			run(command, shell=True)
			print("change", cpu_request, cpu_upper, cpu_usage)
			cooldown=18
	cooldown-=1		