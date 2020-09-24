import gym
import envs
import numpy as np
import os
from dotenv import load_dotenv
from DQNAgent import DQNAgent

load_dotenv('.env')

ip = os.getenv("IP")
port = os.getenv("PORT")
container = os.getenv("CONTAINER")
output_dir = os.getenv("OUTPUT_DIR")
a = float(os.getenv("A"))
b = float(os.getenv("B"))
peak = int(os.getenv("PEAK"))

n_episodes = 1000
batch_size = 32

env = gym.make('Allocator-v0', ip=ip, port=port,  container=container)

state_size = env.observation_space.shape[0]
action_size = env.action_space.n

steps = []
agent = DQNAgent(state_size, action_size, a, b, peak)

print(type(a))

for episode in range(n_episodes):
	state = env.reset()
	total_reward = 0
	state = np.reshape(state, [1,6]) 

	for timestep in range(100):
		action = agent.sample_action(state)

		next_state, reward, done = env.step(action, a, b, peak)
		next_state = np.reshape(next_state, [1, 6])

		reward = reward if not done else -1  # punish agent if it fails
		total_reward += reward
		
		agent.store_experience(state, action, reward, next_state, done)

		state = next_state
		if done:
			print("episode: {}/{}, score: {}, e: {:.2}".format(episode, n_episodes, timestep, agent.epsilon))
			break

		# change to 50	
		if timestep % 50 == 0:
			agent.target_train()

	steps.append([timestep, episode, total_reward])

	if len(agent.replay_memory) > batch_size:
		agent.replay(batch_size)

	if episode % 50 == 0:
		agent.save(output_dir + "weights_" + str(episode) + ".hdf5")
		with open("test2.txt", "w") as myfile:
			for value in steps:
				myfile.write(str(value)+ "\n")						
