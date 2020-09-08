import gym
import envs
from DQNAgent import DQNAgent

ip = '192.168.39.87'
port = '32590'
container = 'resource-consumer'
output_dir = 'model_output/allocator/'
n_episodes = 1000
batch_size = 32
a = 0.5
b = 0.5
peak = 50

env = gym.make('Allocator-v0', ip=ip, port=port,  container=container)
env.render()
state_size = env.observation_space.shape[0]
action_size = env.action_space.n

agent = DQNAgent(state_size, action_size, a, b, peak)

for episode in range(n_episodes):
  state = env.reset() #check if state needs reshaping
  
  for timestep in range(5000): 
    action = agent.sample_action(state)
    next_state, reward, done = env.step(action, a, b, peak) #also check if something needs reshaping
    
    reward = reward if not done else -1 # punish agent if it fails
    agent.store_experience(state, action, reward, next_state, done)

    state = next_state
    if done:
      print("episode: {}/{}, score: {}, e: {:.2}" # print the episode's score and agent's epsilon
                  .format(e, n_episodes, time, agent.epsilon))

  if len(agent.replay_memory) > batch_size:
    agent.replay(batch_size)
  if e % 50 == 0:
    agent.save(output_dir + "weights_" + '{:04d}'.format(e) + ".hdf5")  


