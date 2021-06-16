import matplotlib.pyplot as plt
import numpy as np

def main():
	with open('score.csv', 'r') as fp:
		score = [int(line) for line in fp.readlines()]

	episodes = np.arange(0, len(score), 1)
	
	plt.plot(episodes, score)
	plt.xticks(fontsize=14)
	plt.yticks(fontsize=14)
	
	plt.margins(x=0)					#remove the ugly inner side margin
	plt.margins(y=0) 

	plt.ylabel('Score Amount', fontsize='12')
	plt.xlabel('Episode', fontsize='12')
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()

if __name__ == '__main__':
	main()

