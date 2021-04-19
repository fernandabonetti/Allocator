import gym
import envs
import numpy as np
from utils.logger import logger
from utils.parser import Props
from DQNAgent import DQNAgent
from AllocatorGym.envs.AllocatorEnv.AllocatorEnv import AllocatorEnv
from utils.CircularList import CircularList, Node
from resourceCollector import Collector
import tensorflow as tf
from tensorflow import keras

props = Props()
n_episodes = 1000
batch_size = 50
TRAIN_STEPS = 100

vnfs = CircularList(None, None, 0)

for i in range(len(props.container)):
	collector = Collector(props.ip, props.port, props.container[0][i], props.namespaces[0][i])
	node = Node(props.container[0][i], props.namespaces[0][i], collector, None)
	vnfs.insert(node)

env = AllocatorEnv(props=props)

state_size = env.observation_space.shape[0]
action_size = env.action_space.n

agent = DQNAgent(state_size, action_size)

while True:
	vnf = vnfs.head
	state = env.reset(vnf.collector)
	total_reward = 0
	state = np.reshape(state, [1,6])

	for i in range(0, TRAIN_STEPS):
		print(vnf.container)
		state = np.reshape(state, [1, 6])

		action = agent.sample_action(state)

		next_state, reward, done = env.step(action, vnf.collector)
		next_state = np.reshape(next_state, [1, 6]) 
		
		state = next_state

		total_reward += reward
		
		logger.info("state\':\'{}\', \'action\': \'{}\', \'next_state\': \'{}\', \'reward\': \'{}".format(state, action, next_state, reward))
		
		vnf = vnf.next

		if done:
			logger.info("Steps\': \'{}\', \'Total Reward\': \'{}".format(i, total_reward))
			break
