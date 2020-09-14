import subprocess
import numpy as np
import gym
from gym import spaces
from resourceCollector import Collector


class AllocatorEnv(gym.Env):

	def __init__(self, ip, port, container):
		super(AllocatorEnv, self).__init__()
			
		self.ip = ip
		self.port = port
		self.container = container
		
		# Observation Space is a box with 3-tuple elements
		self.observation_space = spaces.Box(low=0, high=100, shape=(2,3), dtype=np.float32)
		self.action_space = spaces.Discrete(len(ACTIONS))
		self.collector = Collector(self.ip, self.port, self.container)
		

	def _take_action(self, action):
		cpu_limit, mem_limit = self.collector.getResourceLimits()
		cpu_request, mem_request = self.collector.getResourceRequests()

		cpu_thresh, mem_thresh = ACTIONS[action]
		
		cpu_resize = 0
		mem_resize = 0
		if cpu_thresh > 0:
			cpu_resize = (cpu_thresh * 100)/(cpu_limit-cpu_request)
		if mem_thresh > 0:
			mem_resize = (mem_thresh * 100)/(mem_limit-mem_request)

		cpu_limit += cpu_resize
		cpu_request += cpu_resize
		mem_limit += mem_resize
		mem_request += mem_resize
		command = 'kubectl set resources deployment ' + self.container + ' --limits=cpu=' + str(cpu_limit) +'m,memory=' + str(mem_limit) + 'Mi --requests=cpu=' + str(cpu_request) + 'm,memory=' + str(mem_request) + 'Mi'
		print(command)
		subprocess.run(command, shell=True)

	def step(self, action, a, b, peak):
		done = False 
		self._take_action(action)
		
		cpu_usage, mem_usage = self.collector.getResourceUsage()
		cpu_request, mem_request = self.collector.getResourceRequests()
		cpu_limit, mem_limit = self.collector.getResourceLimits()
	
		next_state = ((cpu_usage, cpu_request, cpu_limit), (mem_usage, mem_request, mem_limit))
			
		#TODO: check for OOM killing too
		if cpu_usage > cpu_limit:
			done = True  
		reward =  a * (1 - (cpu_usage-peak)/100) + b * (1 - (mem_usage-peak)/100)  
		return next_state, reward, done    
		
	def reset(self):
		cpu_usage, mem_usage = self.collector.getResourceUsage()
		cpu_request, mem_request = self.collector.getResourceRequests()
		cpu_limit, mem_limit = self.collector.getResourceLimits()

		return ((cpu_usage, cpu_request, cpu_limit), (mem_usage, mem_request, mem_limit))

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