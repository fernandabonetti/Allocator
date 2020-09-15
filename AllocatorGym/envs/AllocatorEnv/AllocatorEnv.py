import subprocess
import numpy as np
import math
import time
import gym
from gym import spaces
from resourceCollector import Collector


class AllocatorEnv(gym.Env):

	def __init__(self, ip, port, container):
		super(AllocatorEnv, self).__init__()
			
		self.ip = ip
		self.port = port
		self.container = container
		self.collector = Collector(self.ip, self.port, self.container)
		self.cpu_limit, self.mem_limit = self.collector.getResourceLimits()
		self.cpu_request, self.mem_request = self.collector.getResourceRequests()
		self.node_max_memory = self.collector.getNodeMemory()
		self.node_max_cpu = self.collector.getNodeCPU()

		# Observation Space is a box with 3-tuple elements
		self.observation_space = spaces.Box(low=0, high=10000, shape=(2,3), dtype=np.float32)
		self.action_space = spaces.Discrete(len(ACTIONS))
		

	def _take_action(self, action):
		cpu_thresh, mem_thresh = ACTIONS[action]
		
		cpu_resize = 0
		mem_resize = 0
		if cpu_thresh > 0:
			cpu_resize = ((cpu_thresh * 100) * (self.cpu_limit - self.cpu_request))/100
		if mem_thresh > 0:
			mem_resize = ((mem_thresh * 100) * (self.mem_limit - self.mem_request))/100
			
		self.cpu_limit += cpu_resize
		self.cpu_request += cpu_resize
		self.mem_limit += mem_resize
		self.mem_request += mem_resize
		#print("[parameters]", self.cpu_limit, self.mem_limit, self.cpu_request, self.mem_request)
		command = 'kubectl set resources deployment ' + self.container + ' --limits=cpu=' + str(self.cpu_limit) +'m,memory=' + str(self.mem_limit) + 'Mi --requests=cpu=' + str(self.cpu_request) + 'm,memory=' + str(self.mem_request) + 'Mi'
		print(command)
		subprocess.run(command, shell=True)

	def step(self, action, a, b, peak):
		done = False 
		self._take_action(action)
		
		cpu_usage, mem_usage = self.collector.getResourceUsage()
		next_state = ((cpu_usage, self.cpu_request, self.cpu_limit), (mem_usage, self.mem_request, self.mem_limit))
			
		if cpu_usage > self.cpu_limit or mem_usage > self.mem_limit:
			print("vo mata esse container")
			done = True
		if self.cpu_limit >= self.node_max_cpu or self.mem_limit >= self.node_max_memory:
			done = True	

		peak_mem = ((self.mem_limit - self.mem_request) * peak)/100
		peak_cpu = ((self.cpu_limit - self.cpu_request) * peak)/100

		reward =  (a * (1 - abs(cpu_usage - peak_cpu)/100)) + (b * (1 - abs(mem_usage - peak_mem)/100))
		return np.array(next_state), reward, done    
		
	def reset(self):
		command = "cd services/resource-consumer && ./cleanup.sh"
		subprocess.run(command, shell=True)
		time.sleep(10)
		cpu_usage, mem_usage = self.collector.getResourceUsage()
		self.cpu_request, self.mem_request = self.collector.getResourceRequests()
		self.cpu_limit, self.mem_limit = self.collector.getResourceLimits()

		return np.array(((cpu_usage, self.cpu_request, self.cpu_limit), (mem_usage, self.mem_request, self.mem_limit)))

	def render(self):
		pass

ACTIONS = {
	0 : (-0.5, 0.0),
	1 : (-0.5, -0.5), 
	2 : (-0.5, -0.25),
	3 : (-0.5, -0.10), 
	4 : (-0.5, 0.10), 
	5 : (-0.5, 0.25), 
	6 : (-0.5, 0.5),
	7 : (-0.25, 0.0),
	8 : (-0.25, -0.5), 
	9 : (-0.25, -0.25),
	10 : (-0.25, -0.10), 
	11 : (-0.25, 0.10), 
	12 : (-0.25, 0.25), 
	13 : (-0.25, 0.5), 
	14 : (-0.10, 0.0),
	15 : (-0.10, -0.5), 
	16 : (-0.10, -0.25),
	17 : (-0.10, -0.10),  
	18 : (-0.10, 0.10),
	19 : (-0.10, 0.25),
	20 : (-0.10, 0.5),
	21 : (0.0, 0.0),
	22 : (0.0, -0.50),
	23 : (0.0, -0.25),
	24 : (0.0, -0.10),
	25 : (0.0, 0.10),
	26 : (0.0, 0.25),
	27 : (0.0, 0.50),
	28 : (0.10, 0.0),
	29 : (0.10, -0.50),
	30 : (0.10, -0.25),
	31 : (0.10, -0.10),
	32 : (0.10, 0.10),
	33 : (0.10, 0.25),
	34 : (0.10, 0.50),
	35 : (0.25, 0.0),
	36 : (0.25, -0.50),
	37 : (0.25, -0.25),
	38 : (0.25, -0.10),
	39 : (0.25, 0.10),
	40 : (0.25, 0.25),
	41 : (0.25, 0.50),
	42 : (0.50, 0.0),
	43 : (0.50, -0.50),
	44 : (0.50, -0.25),
	45 : (0.50, -0.10),
	46 : (0.50, 0.10),
	47 : (0.50, 0.25),
	48 : (0.50, 0.50)
}                     