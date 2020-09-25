import requests
import subprocess
import math
import json
import time

class Collector():
	def __init__(self, ip, port, container):
		self.ip = ip
		self.port = port
		self.container = container

	def assembleQuery(self, metric, options):
		address = 'http://' + self.ip + ':' + self.port
		url = address + '/api/v1/query?query=' + metric + '{container="' + self.container + '"}' + options
		return url

	def queryExec(self, query):
		response = requests.get(query).json()
		if response['status'] == 'success':
			if len(response['data']['result'][0]['value']) > 1:
				return response['data']['result'][0]['value'][1] 		# verify scale
		return -1
		
	def getResourceUsage(self):
		query_mem = self.assembleQuery('container_memory_usage_bytes', "")
		options = "[1m])&or rate(container_cpu_usage_seconds_total{container=" + self.container + "}[5m])"
		query_cpu = self.assembleQuery('rate(container_cpu_usage_seconds_total', options)
		mem = math.ceil(float(self.queryExec(query_mem))/1049000)
		cpu = math.floor(float(self.queryExec(query_cpu)) * 1000)
		return cpu, mem

	def getResourceSpecs(self, spec):
		command = "kubectl get pods -o json | jq \".items[0].spec.containers[0].resources." + spec + "\" > "+  spec +".json"
		subprocess.run(command, shell=True)
		with open(spec + '.json') as fp: 
			requests = json.load(fp)
			
		cpu = int(requests["cpu"][:-1])
		mem = int(requests["memory"][:-2])
		return cpu, mem	

	def getNodeMemory(self):
		address = 'http://' + self.ip + ':' + self.port
		url = address + '/api/v1/query?query=' + 'machine_memory_bytes'
		response = requests.get(url).json()
		mem = math.ceil(int(response['data']['result'][0]['value'][1])/1049000)
		return mem
	
	def getNodeCPU(self):
		address = 'http://' + self.ip + ':' + self.port
		url = address + '/api/v1/query?query=' + 'machine_cpu_cores'
		response = requests.get(url).json()
		cpu = int(response['data']['result'][0]['value'][1]) * 1000
		return cpu

	def changeAllocation(self, cpu_limit, mem_limit, cpu_request, mem_request):
		command = 'kubectl set resources deployment ' + self.container + ' --limits=cpu=' + str(math.floor(cpu_limit)) +'m,memory=' 
		+ str(math.floor(mem_limit)) + 'Mi --requests=cpu=' + str(math.floor(cpu_request)) + 'm,memory=' + str(math.floor(mem_request)) + 'Mi'
		print(command)
		subprocess.run(command, shell=True)