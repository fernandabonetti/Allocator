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
	x= []
	y = []
	with open(filename, 'r') as fp:
		for line in fp.readlines():
			if line[0]=='[':
				y.append(float(line[1:-2]))  
	
	mean = []
	top = 100
	eps = []
	i = 0
	while i <= len(y)-100:
		mean.append(sum(y[x] for x in range(i,top))/100)
		eps.append(i+100)
		i+=100
		top+=100

	[print(d) for d in mean]	
	x = np.arange(0, len(y), 1)

	ax = sns.lineplot(x=x, y=y, data=y)
	# ax.xaxis.set_major_locator(ticker.MultipleLocator(10000))	#set x ticks interval
	# ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
	ax.margins(x=0)				#remove the ugly inner side margin
	ax.margins(y=0.01) 

	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(20)
	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(20)

	ax.set_ylabel('Loss', fontsize=24)
	ax.set_xlabel('Episode', fontsize=24)
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()

if __name__ == '__main__':
	main()