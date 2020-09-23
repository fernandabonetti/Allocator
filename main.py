import gym
import envs
import time
import numpy as np
from DQNAgent import DQNAgent

ip = '192.168.39.126'
port = '30000'
container = 'resource-consumer'
output_dir = 'model_output/'
n_episodes = 1000
batch_size = 32
a = 0.5
b = 0.5
peak = 25

env = gym.make('Allocator-v0', ip=ip, port=port,  container=container)

state_size = env.observation_space.shape[0]
action_size = env.action_space.n

steps = []
agent = DQNAgent(state_size, action_size, a, b, peak)
done = False

for episode in range(n_episodes):
	state = env.reset()
	state = np.reshape(state, [1,6]) 

	for timestep in range(500):
		action = agent.sample_action(state)

		next_state, reward, done = env.step(action, a, b, peak)

		next_state = np.reshape(next_state, [1, 6])

		reward = reward if not done else -1  # punish agent if it fails
		print("[REWARD]:", reward)
		agent.store_experience(state, action, reward, next_state, done)

		state = next_state
		if done:
			print("episode: {}/{}, score: {}, e: {:.2}".format(episode, n_episodes, timestep, agent.epsilon))
			break

		# change to 50	
		if timestep % 50 == 0:
			agent.target_train()

	steps.append([timestep, episode])

	if len(agent.replay_memory) > batch_size:
		agent.replay(batch_size)

	if episode % 50 == 0:
		agent.save(output_dir + "weights_" +
								'{:04d}'.format(episode) + ".hdf5")
		with open("test.txt", "w") as myfile:
			for value in steps:
				myfile.write(str(value))						
