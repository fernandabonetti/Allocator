import gym
import numpy as np
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines import DQN
from utils.parser import Props
from utils.logger import logger

props = Props()

env = gym.make('Allocator-v0', ip=props.ip, port=props.port,  container=props.container)

model = DQN(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=1000)
model.save("baselines_DQN")

state = env.reset()
while True:
	state = np.reshape(state, [1, 6])
	action, _states = model.predict(state)
	next_state, reward, done = env.step(action, props.a, props.b, props.peak)
	next_state = np.reshape(next_state, [1, 6])
	logger.info("done\':\'{}\', state\':\'{}\', \'action\': \'{}\', \'next_state\': \'{}\', \'reward\': \'{}".format(done, state, action, next_state, reward))
	