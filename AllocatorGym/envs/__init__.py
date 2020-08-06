from gym.envs.registration import register

register(id='Allocator-v0',
    entry_point='envs.AllocatorEnv:AllocatorEnv'
)