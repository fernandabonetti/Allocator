import gym
import envs
import numpy as np
from utils.logger import logger
from utils.parser import Props
from DQNAgent import DQNAgent
from AllocatorGym.envs.AllocatorEnv.AllocatorEnv import AllocatorEnv
import tensorflow as tf
from tensorflow import keras

props = Props()
n_episodes = 1000
batch_size = 50
TRAIN_STEPS = 100

env = AllocatorEnv(ip=props.ip, port=props.port,  container=props.container)

state_size = env.observation_space.shape[0]
action_size = env.action_space.n

agent = DQNAgent(state_size, action_size, props.a, props.b, props.peak)

while True:
	state = env.reset()
	total_reward = 0
	state = np.reshape(state, [1,6])

	for i in range(0, TRAIN_STEPS):
		state = np.reshape(state, [1, 6])

		action = agent.sample_action(state)

		next_state, reward, done = env.step(action, props.a, props.b, props.peak)
		next_state = np.reshape(next_state, [1, 6]) 
		
		state = next_state

		total_reward += reward
		
		logger.info("state\':\'{}\', \'action\': \'{}\', \'next_state\': \'{}\', \'reward\': \'{}".format(state, action, next_state, reward))
		
		if done:
			logger.info("Steps\': \'{}\', \'Total Reward\': \'{}".format(i, total_reward))
			break
