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

		collector = Collector(self.ip, self.port, self.container)
		
		# Observation Space is a box with 3-tuple elements
		self.observation_space = spaces.Box(low=0, high=100, shape=(2,3), dtype=np.float32)
		self.action_space = spaces.Discrete(len(ACTIONS))

	def _take_action(self, action):
		cpu_limit = getCPULimits()
		mem_limit = getMemoryLimits()
		cpu_request = getCPURequest()
		mem_request = getMemoryRequest()

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
		command = 'kubectl set resources deployment ' + self.container + '--limits=cpu=' +
		 cpu_limit +'m,memory=' + mem_limit + 'Mi --requests=cpu=' + cpu_request + 'm, memory=' + mem_request + 'Mi'
		print(command)
		subprocess.run(command, shell=True)

	def step(self, action, a, b, peak):
		done = False 
		self._take_action(action)
		
		self.cpu_usage = collector.getCPU()
		self.mem_usage = collector.getMEM()
		self.cpu_request, self.cpu_limit = Collector.getCPULimits()
		self.mem_request, self.mem_limit = Collector.getMEMLimits()
		next_state = [(cpu_usage, cpu_request, cpu_limit), (mem_usage, mem_request, mem_limit)]
			
		#TODO: check for OOM killing too
		if self.cpu_usage > self.cpu_limit:
			done = True  
		reward =  a * (1 - (cpu_usage-peak)/100) + b * (1 - (mem_usage-peak)/100)  
		return next_state, reward, done    
		
	def reset(self):
		self.cpu_usage = Collector.getCPU(self.ip, self.port, self.container)
		self.mem_usage = Collector.getMEM(self.ip, self.port, self.container)
		self.cpu_request, self.cpu_limit = Collector.getCPULimits(self.ip, self.port, self.container)
		self.mem_request, self.mem_limit = Collector.getMEMLimits(self.ip, self.port, self.container)

	def render(self):
		print("deu certo")
		print(self.ip, self.port, self.container)

ACTIONS = {
	1 : (-0.5, 0.0),
	2 : (-0.5, -0.5), 
	3 : (-0.5, -0.25),
	4 : (-0.5, -0.10), 
	5 : (-0.5, 0.10), 
	6 : (-0.5, 0.25), 
	7 : (-0.5, 0.5),
	8 : (-0.25, 0.0),
	9 : (-0.25, -0.5), 
	10 : (-0.25, -0.25),
	11 : (-0.25, -0.10), 
	12 : (-0.25, 0.10), 
	13 : (-0.25, 0.25), 
	14 : (-0.25, 0.5), 
	15 : (-0.10, 0.0),
	16 : (-0.10, -0.5), 
	17 : (-0.10, -0.25),
	18 : (-0.10, -0.10),  
	19 : (-0.10, 0.10),
	20 : (-0.10, 0.25),
	21 : (-0.10, 0.5),
	22 : (0.0, 0.0),
	23 : (0.0, -0.50),
	24 : (0.0, -0.25),
	25 : (0.0, -0.10),
	26 : (0.0, 0.10),
	27 : (0.0, 0.25),
	28 : (0.0, 0.50),
	29 : (0.10, 0.0),
	30 : (0.10, -0.50),
	31 : (0.10, -0.25),
	32 : (0.10, -0.10),
	33 : (0.10, 0.10),
	34 : (0.10, 0.25),
	35 : (0.10, 0.50),
	36 : (0.25, 0.0),
	37 : (0.25, -0.50),
	38 : (0.25, -0.25),
	39 : (0.25, -0.10),
	40 : (0.25, 0.10),
	41 : (0.25, 0.25),
	42 : (0.25, 0.50),
	43 : (0.50, 0.0),
	44 : (0.50, -0.50),
	45 : (0.50, -0.25),
	46 : (0.50, -0.10),
	47 : (0.50, 0.10),
	48 : (0.50, 0.25),
	49 : (0.50, 0.50)
}                     