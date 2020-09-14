import requests
import subprocess
import math
import json

# https://prometheus.io/docs/prometheus/latest/querying/api/
# put jq in dependencies

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
		return response['data']['result'][0]['value'][1] 		# verify scale

	def getResourceUsage(self):
		#rate(container_cpu_usage_seconds_total{container=\"resource-consumer\"}[5m])",
		query_mem = self.assembleQuery('container_memory_usage_bytes', "")
		query_cpu = self.assembleQuery('rate(container_cpu_usage_seconds_total', "[1m])")
		mem = math.ceil(float(self.queryExec(query_mem))/1049000)
		cpu = math.floor(float(self.queryExec(query_cpu)) * 1000)
		return cpu, mem

	def getResourceLimits(self):
		query_cpu = self.assembleQuery('container_spec_cpu_shares', "")
		query_mem = self.assembleQuery('container_spec_memory_limit_bytes', "")
		mem = math.ceil(float(self.queryExec(query_mem))/1049000)
		cpu = math.floor(float(self.queryExec(query_cpu)) * 1000)
		return cpu, mem

	def getResourceRequests(self):
		command = "kubectl get pods -o json | jq \".items[ 0].spec.containers[0].resources.requests\" > requests.json"
		subprocess.run(command, shell=True)
		with open('requests.json') as fp: 
			requests = json.load(fp)
		cpu = int(requests["cpu"][:-1])
		mem = int(requests["memory"][:-2])
		return cpu, mem	








