import gym
import numpy as np
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines import DQN
from dotenv import load_dotenv

load_dotenv('.env')
ip = os.getenv("IP")
port = os.getenv("PORT")
container = os.getenv("CONTAINER")

# a and b are 'boundness' parameters of each resource
a = float(os.getenv("A"))
b = float(os.getenv("B"))
peak = int(os.getenv("PEAK"))

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('dracon.log')

env = gym.make('Allocator-v0', ip=ip, port=port, container=container)

model = DQN(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=1000)
model.save("baselines_DQN")

state = env.reset()
while True:
	state = np.reshape(state, [1, 6])
	action, _states = model.predict(state)
	next_state, reward, done = env.step(action, a, b, peak)
	next_state = np.reshape(next_state, [1, 6])