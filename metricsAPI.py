from kubernetes import client, config
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from subprocess import PIPE, run
import math
import json
import time

class Collector():
	def __init__(self, ip, port, container, namespace):
		self.ip = ip
		self.port = port
		self.mem_usage = 0
		self.cpu_usage = 0
		self.container = container
		self.namespace = namespace
		config.load_kube_config()
		self.api = client.CoreV1Api()

	def assembleQuery(self, metric, options):
		address = 'http://' + self.ip + ':' + self.port
		url = address + '/api/v1/query?query=' + \
				 metric + '{container="' + self.container + '",namespace=\"' + self.namespace + '\"}' + options
		return url

	def queryExec(self, query):
		session = requests.Session()
		retry = Retry(connect=3, backoff_factor=3)
		adapter = HTTPAdapter(max_retries=retry)
		session.mount('http://', adapter)
		response = session.get(query, headers={'Connection':'close'}, verify=False).json()

		if (response['status'] == 'success' and len(response['data']['result']) > 0):
			return response['data']['result'][0]['value'][1] 		
		return 0	

	def list_pods(self):
		pods = self.api.list_pod_for_all_namespaces(watch=False)	
		return pods

	def change_allocation(self, cpu_request, cpu_limit, mem_request, mem_limit):
		configuration = client.Configuration()
		v1 = client.AppsV1Api(client.ApiClient(configuration))

		body = {"spec": {"template": {
						"spec": {"containers": [{
											"name": self.container,
											"resources": { \
												'limits': {'cpu':  cpu_limit, 'memory': mem_limit},\
												'requests': {'cpu': cpu_request, 'memory': mem_request}}
										}]}
									}}}							

		api_response = v1.patch_namespaced_deployment(name=self.container, namespace=self.namespace, body=body)

	def check_usage(self):
		cpu, mem = None, None
		api = client.CustomObjectsApi()
		resource = api.list_cluster_custom_object("metrics.k8s.io", "v1beta1", "pods")
		for item in resource['items']:
			for container in item['containers']:
				if container['name'] == self.container:
					mem = math.floor(float(container['usage']['memory'][:-2]))
					cpu = math.floor(float(container['usage']['cpu']))
		return cpu, mem

	def get_resource_usage(self):
		query_mem = self.assembleQuery('container_memory_usage_bytes', "")
		options = '[1m]))'
		query_cpu = self.assembleQuery('sum%20by%20(pod)(rate(container_cpu_usage_seconds_total' , options)
		
		mem = self.queryExec(query_mem)
		cpu = self.queryExec(query_cpu)

		if mem != 0 and cpu != 0:	
			self.mem_usage = math.ceil(float(mem)/1049000)
			self.cpu_usage = cpu = math.floor(float(cpu) *1000)

		return self.cpu_usage, self.mem_usage			