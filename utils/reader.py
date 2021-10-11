
import pandas as pd

def read_usage(filename):
	with open(filename, 'r') as fp:
		resource = [line.replace('\n', '').split(',') for line in fp.readlines()]

		limits = [[float(i[0]),float(i[1]), float(i[2])]  for i in resource]

	limits = pd.DataFrame(limits, columns=['usage', 'min', 'max'], dtype=float)
	return limits 

def read_metrics(filename, type):
		with open(filename, 'r') as fp:
			metrics = [line for line in fp.readlines()]
		
		if type == 'int':
			return list(map(int, metrics))
		return list(map(float, metrics))	
