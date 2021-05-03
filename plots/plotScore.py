import json
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import numpy as np

def main():
	with open('score.csv', 'r') as fp:
		score = [int(line) for line in fp.readlines()]

	episodes = np.arange(0, len(score), 1)
	
	ax = sns.lineplot(x=episodes, y=score, data=score)
	#ax.xaxis.set_major_locator(ticker.MultipleLocator(100))	#set x ticks interval
	#ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
	ax.margins(x=0)					#remove the ugly inner side margin
	ax.margins(y=0) 

	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(12)
	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(12)

	ax.set_ylabel('Score Amount', fontsize='12')
	ax.set_xlabel('Episode', fontsize='12')
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()

if __name__ == '__main__':
	main()

