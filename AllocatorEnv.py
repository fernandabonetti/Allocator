
import gym
from gym import spaces

class AllocatorEnv(gym.Env):

  def __init__(self):
    super(AllocatorEnv, self).__init__()

    self.action_space = spaces.Discrete(N_ACTIONS)
    #alterar o high para o limite do node
    self.observation_space = spaces.Box(low=0, high=255, shape=
                    (cpu_usage, cpu_request, cpu_limit,
                     mem_usage, mem_request, mem_limit), dtype=np.float16)

    def step(self, action):
      pass


    def reset(self):
      pass

                     