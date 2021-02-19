import pickle
import random

levels = [0.0, 0.10, 0.25, 0.50, -0.10, -0.25, -0.50]

actions = []
index = 0
for i in range(0, len(levels)):
	for j in range(0, len(levels)):
		actions.append([levels[i], levels[j]])
		index+=1
		
print(len(actions))
random.shuffle(actions)
print(actions)

act = {}
i=0
for action in actions:
	act[i] = (action[0],action[1])
	i+=1
	
with open('shuffled.pkl', 'wb') as handle:
  pickle.dump(act, handle)
