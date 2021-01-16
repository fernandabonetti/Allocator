import json
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import numpy as np

def main():

	with open('score.csv', 'r') as fp:
		score = [int(line) for line in fp.readlines()]	
	
	mean = []
	top = 100
	eps = []
	i = 0
	while i <= len(score)-100:
		mean.append(sum(score[x] for x in range(i,top))/100)
		eps.append(i+100)
		i+=100
		top+=100
	
	ax = sns.lineplot(x=eps, y=mean, data=mean)
	ax.margins(x=0)						#remove the ugly inner side margin 

	ax.set_title('Average Score by Episode')
	ax.set_ylabel('Score Amount')
	ax.set_xlabel('Episode')
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()

if __name__ == '__main__':
	main()

