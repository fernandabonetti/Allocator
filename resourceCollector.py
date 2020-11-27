import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from subprocess import PIPE, run
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
		session = requests.Session()
		retry = Retry(connect=3, backoff_factor=1)
		adapter = HTTPAdapter(max_retries=retry)
		session.mount('http://', adapter)

		response = session.get(query, headers={'Connection':'close'}, verify=False).json()

		if (response['status'] == 'success' and len(response['data']['result']) > 0):
			return response['data']['result'][0]['value'][1] 		# verify scale
		return -1	
		
	def getResourceUsage(self):
		query_mem = self.assembleQuery('container_memory_usage_bytes', "")

		options = '[1m]))'
		query_cpu = self.assembleQuery('sum%20by%20(pod)(rate(container_cpu_usage_seconds_total' , options)
		mem = math.ceil(float(self.queryExec(query_mem))/1049000)
		cpu = math.floor(float(self.queryExec(query_cpu)) * 1000)
		return cpu, mem

	def getResourceSpecs(self, spec):
		command = "kubectl get pods -o json | jq \".items[0].spec.containers[0].resources." + spec + "\""
		result = run(command, stdout=PIPE, universal_newlines=True, shell=True)
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

	def getNodeMemory(self):
		command = "kubectl get node minikube -o=jsonpath=\'{.status.allocatable.memory}\'"
		result = run(command, stdout=PIPE, universal_newlines=True, shell=True)
		resource = json.loads(result.stdout[:-2])
		mem = math.floor(resource/1049) 	#transform Ki to Mi
		return mem
	
	def getNodeCPU(self):
		command = "kubectl get node minikube -o=jsonpath=\'{.status.allocatable.cpu}\'"
		result = run(command, stdout=PIPE, universal_newlines=True, shell=True)
		resource = json.loads(result.stdout)
		cpu = int(resource)*1000 	#transform to millicores

		return cpu


	def changeAllocation(self, cpu_limit, mem_limit, cpu_request, mem_request):
		command = 'kubectl set resources deployment ' + self.container + ' --limits=cpu=' + str(cpu_limit) \
			 +'m,memory=' + str(mem_limit) + 'Mi --requests=cpu=' + str(cpu_request) + 'm,memory=' + str(mem_request) + 'Mi'
		run(command, shell=True)