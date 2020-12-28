import gym
import envs
import numpy as np
import os
import logging
from dotenv import load_dotenv
from DQNAgent import DQNAgent

load_dotenv('.env')
ip = os.getenv("IP")
port = os.getenv("PORT")
container = os.getenv("CONTAINER")
output_dir = os.getenv("OUTPUT_DIR")

# a and b are 'boundness' parameters of each resource
a = float(os.getenv("A"))
b = float(os.getenv("B"))
peak = int(os.getenv("PEAK"))

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('dracon.log')

file_formatter=logging.Formatter("{'time':'%(asctime)s','message': {'%(message)s'}}")
handler.setFormatter(file_formatter)
logger.addHandler(handler)

n_episodes = 1500
batch_size = 32

env = gym.make('Allocator-v0', ip=ip, port=port,  container=container)

state_size = env.observation_space.shape[0]
action_size = env.action_space.n

steps = []
agent = DQNAgent(state_size, action_size, a, b, peak)

for episode in range(n_episodes):
	state = env.reset()
	total_reward = 0
	state = np.reshape(state, [1, 6]) 

	for timestep in range(500):
		action = agent.sample_action(state)

		next_state, reward, done = env.step(action, a, b, peak)
		next_state = np.reshape(next_state, [1, 6])

		reward = reward if not done else -1
		total_reward += reward
		
		logger.info("state\':\'{}\', \'action\': \'{}\', \'next_state\': \'{}\', \'reward\': \'{}".format(state, action, next_state, reward))
		agent.store_experience(state, action, reward, next_state, done)

		state = next_state
		if done:
			logger.info("episode\': \'{}/{}\', \'score\': \'{}\', \'e\': \'{:.2}".format(episode, n_episodes, timestep, agent.epsilon))
			break

	logger.info("Steps\': \'{}\', \'Episode\': \'{}\', \'Total Reward\': \'{}".format(timestep, episode, total_reward))

	if len(agent.replay_memory) > batch_size:
		agent.replay(batch_size)
		agent.target_train()

	# Update Target Network weights at each 100 episodes
	if episode % 50 == 0:
		agent.save(output_dir + "weights_" + str(episode) + ".hdf5")
					
