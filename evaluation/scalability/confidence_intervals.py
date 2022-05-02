import sys
import numpy as np
from numpy import dtype
from scipy.stats import t

def confidence(data):
	mean = data.mean()
	print(mean)
	stdev = data.std()
	dof = len(data)-1

	t_crit = np.abs(t.ppf((1-0.95)/2, dof))
	lower = mean - stdev * t_crit/np.sqrt(len(data))
	upper =  mean + stdev * t_crit/np.sqrt(len(data))

	return lower, upper


def main():
	if len(sys.argv) < 1:
		exit(1)

	filename = sys.argv[1]
	
	with open(filename, 'r')as fp:
		data = np.array([line.replace('\n', '').split(' ') for line in fp.readlines()], dtype=int)
	
	print(confidence(data[:,0]))
	print(confidence(data[:,1]))

if __name__ == '__main__':
	main()