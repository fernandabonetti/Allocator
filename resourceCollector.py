import requests

#https://prometheus.io/docs/prometheus/latest/querying/api/

class Collector():
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
	
	def assembleQuery(self, containerName, metric):
		address = 'http://' + self.ip + ':' + self.port
		url = address + '/api/v1/query?' + metric + '{container="' + containerName + '"}'
		return url

	def getMemory(self, containerName):
		metric = 'query=container_memory_usage_bytes'
		query = self.assembleQuery(containerName, metric)
		response = requests.get(query).json()
		return response['data']['result'][0]['value'] 		# verify scale

	def getCPU(self, containerName):
		metric = 'query=container_cpu_usage_seconds_total'
		query = self.assembleQuery(containerName, metric)
		response = requests.get(query).json()
		return response['data']['result'][0]['value']

	def getCPUDefinitions(self, containerName):
		pass

	def getMEMDefinitions(self, containerName):



		
				