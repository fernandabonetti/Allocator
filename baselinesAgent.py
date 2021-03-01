import gym
from gym import envs
import numpy as np
from AllocatorGym.envs.AllocatorEnv.AllocatorEnv import AllocatorEnv

# from stable_baselines.common import make_vec_env
# from stable_baselines.deepq.policies import MlpPolicy
# from stable_baselines import DQN
from utils.logger import Logger as logger
from utils.parser import Props

props = Props()

env = AllocatorEnv(ip=props.ip, port=props.port, container=props.container)
env = make_vec_env(lambda: env, n_envs=1)

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