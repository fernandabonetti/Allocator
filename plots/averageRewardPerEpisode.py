import matplotlib.pyplot as plt
import numpy as np

def main():
	with open('reward.csv', 'r') as fp, open('score.csv', 'r') as fp2:
		rewards = [float(line) for line in fp.readlines()]
		steps = [float(line) for line in fp2.readlines()]

	mean = []
	for i in range(0, len(rewards)):
		mean.append(rewards[i]/steps[i])

	eps = np.arange(0, len(mean), 1)
	plt.plot(eps, mean)
	plt.margins(x=0)				#remove the ugly inner side margin 
	
	plt.xticks(fontsize=14)
	plt.yticks(fontsize=14)

	plt.ylabel('Reward Amount', fontsize=12)
	plt.xlabel('Episode', fontsize=12)
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()

if __name__ == '__main__':
	main()	