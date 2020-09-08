import requests

#https://prometheus.io/docs/prometheus/latest/querying/api/
'''
metrics = {
	"cpu_usage" : "container_cpu_usage_seconds_total",
	"mem_usage" : "container_memory_usage_bytes",
	
}
'''
#http://localhost:3000/api/v1/query?'
#querystring = {'query' : metric, } + metric + '{container="' + containerName + '"}'

class Collector():
	def __init__(self, ip, port, container):
		self.ip = ip
		self.port = port
		self.container = container

	def assembleQuery(self, metric):
		address = 'http://' + self.ip + ':' + self.port
		url = address + '/api/v1/query?' + metric + '{container="' + self.container + '"}'
		return url

	# TODO: DRY  eu posso criar um dicionario de metricas e só passar o codigo
	def getMemory(self):
		metric = 'query=container_memory_usage_bytes'
		query = self.assembleQuery(metric)
		response = requests.get(query).json()
		return response['data']['result'][0]['value'][1] 		# verify scale

	def getCPU(self):
		metric = 'query=container_cpu_usage_seconds_total'
		query = self.assembleQuery(metric)
		response = requests.get(query).json()
		return response['data']['result'][0]['value'][1]

	def getCPULimits(self):
		metric = 'query=container_spec_cpu_shares'
		query = self.assembleQuery(metric)
		response = requests.get(query).json()
		return response['data']['result'][0]['value'][1]


	def getMemoryLimits(self):
		metric = 'query=container_spec_memory_limit_bytes'
		query = self.assembleQuery(metric)
		response = requests.get(query).json()
		return response['data']['result'][0]['value'][1]










