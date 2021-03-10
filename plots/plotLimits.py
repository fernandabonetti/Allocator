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
	#[print(d) for d in steps]

	ax = sns.lineplot(x=steps, y=mem_usage, data=mem_usage, lw=1)
	ax = sns.lineplot(x=steps, y=mem_max, data=mem_max, lw=1)
	ax = sns.lineplot(x=steps, y=mem_min, data=mem_min, lw=1)
	
	ax.margins(x=0)				#remove the ugly inner side margin 

	#ax.set_title('Limits Behaviour')
	ax.set_ylabel('Resource', fontsize=24)
	ax.set_xlabel('Steps', fontsize=24)
	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(20)
	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(20)
	plt.legend(loc='upper left', labels=['MEM Usage', 'MEM Limits', "MEM Request"], fontsize=20)
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()

if __name__ == '__main__':
	main()