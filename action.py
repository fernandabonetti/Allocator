import pickle

levels = [0.0, 0.10, 0.25, 0.50, -0.10, -0.25, -0.50]

ACTIONS = {}
index = 0
for i in range(0, len(levels)):
	for j in range(0, len(levels)):
		ACTIONS[index] = (levels[i], levels[j])
		index+=1
print(len(ACTIONS))
print(ACTIONS)

with open('actions2.pkl', 'wb') as handle:
  pickle.dump(ACTIONS, handle)
