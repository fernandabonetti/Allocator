import requests
import subprocess
import json

# https://prometheus.io/docs/prometheus/latest/querying/api/
# put jq in dependencies

class Collector():
	def __init__(self, ip, port, container):
		self.ip = ip
		self.port = port
		self.container = container

	def assembleQuery(metric):
		address = 'http://' + self.ip + ':' + self.port
		url = address + '/api/v1/query?query=' + metric + '{container="' + self.container + '"}'
		return url

	def queryExec(query):
		response = requests.get(query).json()
		return response['data']['result'][0]['value'][1] 		# verify scale

	def getResouceUsage(self):
		query_mem = assembleQuery('container_memory_usage_bytes')
		query_cpu = assembleQuery('container_cpu_usage_seconds_total')
		mem = queryExec(query_mem)
		cpu = queryExec(query_cpu)
		return cpu, mem

	def getResourceLimits(self):
		query_cpu = assembleQuery('container_spec_cpu_shares')
		query_mem = assembleQuery('container_spec_memory_limit_bytes')
		mem = queryExec(query_mem)
		cpu = queryExec(query_cpu)
		return cpu, mem

	def getResourceRequests(self):
		command = "kubectl get pods -n default -o json | jq \".items[0].spec.containers[0].resources.requests\" > requests.json"
		subprocess.run(command, shell=True)
		with open('requests.json') as fp: 
			requests = json.load(fp)
		cpu = int(requests["cpu"][:-1])
		mem = int(requests["memory"][:-2])
		return cpu, mem	








