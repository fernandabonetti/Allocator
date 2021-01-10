import json
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import numpy as np

def main():
	if len(sys.argv) < 1:
		exit(1)

	filename = sys.argv[1]
	data = {}

	with open(filename, 'r') as fp:
		for index, line in enumerate(fp.readlines()):
			data.update({index: json.loads(line)})

	episodes = []
	score = []
	for record in data.values():
		if 'score' in record["message"].keys():
			score.append(int(record["message"]["score"]))
			episodes.append(int(record["message"]["episode"][:-5]))
	
	mean = []
	top = 100
	eps = []
	i = 0
	while i <= len(score)-100:
		mean.append(sum(score[x] for x in range(i,top))/100)
		eps.append(i+100)
		i+=100
		top+=100
	sns.set_theme(style="darkgrid")
	
	ax = sns.lineplot(x=eps, y=mean, data=mean)
	ax.margins(x=0)					#remove the ugly inner side margin 

	ax.set_title('Average Score by Episode')
	ax.set_ylabel('Score Amount')
	ax.set_xlabel('Episode')
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()

if __name__ == '__main__':
	main()

