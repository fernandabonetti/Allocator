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
	
	x = np.arange(0, len(y), 1)
	sns.set_theme(style="darkgrid")

	ax = sns.lineplot(x=x, y=y, data=y)
	ax.xaxis.set_major_locator(ticker.MultipleLocator(10000))	#set x ticks interval
	ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
	ax.margins(x=0)				#remove the ugly inner side margin
	ax.margins(y=0.01) 

	ax.set_title('Loss over training Episodes')
	ax.set_ylabel('Loss')
	ax.set_xlabel('Episode')
	plt.show()

if __name__ == '__main__':
	main()