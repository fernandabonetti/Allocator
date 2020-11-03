import subprocess
import numpy as np
import math
import time
import pickle
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
		
		self.cpu_limit, self.mem_limit = self.collector.getResourceSpecs("limits")
		self.cpu_request, self.mem_request = self.collector.getResourceSpecs("requests")
		self.node_max_memory = self.collector.getNodeMemory()
		self.node_max_cpu = self.collector.getNodeCPU()
		
		self.actions = self._load_actions()

		# Observation Space is a box with 3-tuple elements
		self.observation_space = spaces.Box(low=0, high=10000, shape=(1,6), dtype=np.float32)
		self.action_space = spaces.Discrete(len(self.actions))
		
	def _take_action(self, action):
		cpu_thresh, mem_thresh = self.actions[action]
		
		if cpu_thresh != 0.0:
			self.cpu_limit += math.floor(((cpu_thresh * 100) * self.cpu_limit)/100)
			self.cpu_request += math.floor(((cpu_thresh * 100) * self.cpu_request)/100)

		if mem_thresh != 0.0:
			self.mem_limit += math.floor(((mem_thresh * 100) * self.mem_limit)/100)
			self.mem_request += math.floor(((mem_thresh * 100) * self.mem_request)/100)

		self.collector.changeAllocation(self.cpu_limit, self.mem_limit, self.cpu_request, self.mem_request)

	def step(self, action, a, b, peak):
		done = False 
		self._take_action(action)
		
		cpu_usage, mem_usage = self.collector.getResourceUsage()
		next_state = (cpu_usage, self.cpu_request, self.cpu_limit, mem_usage, self.mem_request, self.mem_limit)
			
		if cpu_usage > self.cpu_limit or mem_usage > self.mem_limit:
			done = True
		if self.cpu_limit >= self.node_max_cpu or self.mem_limit >= self.node_max_memory:
			done = True	

		peak_mem = self.mem_request + (((self.mem_limit - self.mem_request) * peak)/100) # transform peak to be limits relative
		peak_cpu = self.cpu_request + (((self.cpu_limit - self.cpu_request) * peak)/100)
		
		reward =  (a * (1 - abs(cpu_usage - peak_cpu)/100)) + (b * (1 - abs(mem_usage - peak_mem)/100))
		return np.array(next_state), reward, done    
		
	def reset(self):
		command = "cd services/resource-consumer && ./cleanup.sh"
		subprocess.run(command, shell=True)
		time.sleep(1)
		cpu_usage, mem_usage = self.collector.getResourceUsage()
		self.cpu_request, self.mem_request = self.collector.getResourceSpecs("requests")
		self.cpu_limit, self.mem_limit = self.collector.getResourceSpecs("limits")
		return np.array((cpu_usage, self.cpu_request, self.cpu_limit, mem_usage, self.mem_request, self.mem_limit))

	def _load_actions(self):
		with open('actions.pkl', 'rb') as fp:
			actions = pickle.load(fp)	
		return actions