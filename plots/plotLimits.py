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

	cpu_usage = []
	cpu_min = []
	cpu_max = []
	mem_usage = []
	mem_min = []
	mem_max = []
	i = 0
	for record in data.values():
		if 'state' in record["message"].keys():
			state = [int(value) for value in record["message"]["state"][2:].replace(']', '').split(' ') if value != '']
			cpu_usage.append(state[0])
			cpu_min.append(state[1])
			cpu_max.append(state[2])
			mem_usage.append(state[3])
			mem_min.append(state[4])
			mem_max.append(state[5])
			
	steps = np.arange(0, len(cpu_usage), 1)
	grad = np.arange(0, 20, 1)
	sns.set_theme(style="darkgrid")

	ax = sns.lineplot(x=steps[800:1000], y=cpu_usage[800:1000], data=cpu_usage[800:1000], lw=1)
	ax = sns.lineplot(x=steps[800:1000], y=cpu_max[800:1000], data=cpu_max[800:1000], lw=1)
	ax = sns.lineplot(x=steps[800:1000], y=cpu_min[800:1000], data=cpu_min[800:1000], lw=1)
	
	#ax.xaxis.set_major_locator(ticker.MultipleLocator(1000
	# ))	#set x ticks interval
	#ax.xaxis.set_major_formatter(ticker.ScalarFormatter())

	ax.margins(x=0)				#remove the ugly inner side margin 

	ax.set_title('Limits Behaviour')
	ax.set_ylabel('Resource')
	ax.set_xlabel('Steps')
	plt.legend(loc='upper left', labels=['cpu Usage', 'cpu Limits', "cpu Request"])
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()

if __name__ == '__main__':
	main()