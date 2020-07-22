
import numpy as np
import gym
from gym import spaces

class AllocatorEnv(gym.Env):

  def __init__(self):
    super(AllocatorEnv, self).__init__()

    # Observation Space is a box with 3-tuple elements
    self.observation_space = spaces.Box(shape=(2,3), dtype=np.float32)
    self.action_space = spaces.Discrete(N_ACTIONS)

    def step(self, action, a, b):
      done = False 

      cpu_usage = getCPU()
      mem_usage = getMEM()
      cpu_request, cpu limit = getCPUDefinitions()
      mem_request, mem_limit = getMEMDefinitions()
      next_state = [(cpu_usage, cpu_request, cpu_limit), (mem_usage, mem_request, mem_limit)]
      
      #TODO: check for OOM killing too
      if cpu_usage > cpu_limit:
        done = True  
      reward =  a * np.sin(cpu_usage) + b * np.sin(mem_usage)  
      return next_state, reward, done    


    def reset(self):
      pass

ACTIONS = {
  1 : {(-0.5, 0.0)},
  2 : {(-0.5, -0.5)}, 
  3 : {(-0.5, -0.25)},
  4 : {(-0.5, -0.10)}, 
  5 : {(-0.5, 0.10)}, 
  6 : {(-0.5, 0.25)}, 
  7 : {(-0.5, 0.5)},
  8 : {(-0.25, 0.0)},
  9 : {(-0.25, -0.5)}, 
  10 : {(-0.25, -0.25)},
  11 : {(-0.25, -0.10)}, 
  12 : {(-0.25, 0.10)}, 
  13 : {(-0.25, 0.25)}, 
  14 : {(-0.25, 0.5)}, 
  15 : {(-0.10, 0.0)},
  16 : {(-0.10, -0.5)}, 
  17 : {(-0.10, -0.25)},
  18 : {(-0.10, -0.10)},  
  19 : {(-0.10, 0.10)},
  20 : {(-0.10, 0.25)},
  21 : {(-0.10, 0.5)},
  22 : {(0.0, 0.0)},
  23 : {(0.0, -0.50)},
  24 : {(0.0, -0.25)},
  25 : {(0.0, -0.10)},
  26 : {(0.0, 0.10)},
  27 : {(0.0, 0.25)},
  28 : {(0.0, 0.50)},
  29 : {(0.10, 0.0)},
  30 : {(0.10, -0.50)},
  31 : {(0.10, -0.25)},
  32 : {(0.10, -0.10)},
  33 : {(0.10, 0.10)},
  34 : {(0.10, 0.25)},
  35 : {(0.10, 0.50)},
  36 : {(0.25, 0.0)},
  37 : {(0.25, -0.50)},
  38 : {(0.25, -0.25)},
  39 : {(0.25, -0.10)},
  40 : {(0.25, 0.10)},
  41 : {(0.25, 0.25)},
  42 : {(0.25, 0.50)},
  43 : {(0.50, 0.0)},
  44 : {(0.50, -0.50)},
  45 : {(0.50, -0.25)},
  46 : {(0.50, -0.10)},
  47 : {(0.50, 0.10)},
  48 : {(0.50, 0.25)},
  49 : {(0.50, 0.50)}
}                     