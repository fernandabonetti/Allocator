import json
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import numpy as np

def main():

	with open('cpu.csv', 'r') as fp, open('mem.csv', 'r') as fr:
		cpu = [line.replace('\n', '').split(',') for line in fp.readlines()]
		mem = [line.replace('\n', '').split(',') for line in fr.readlines()]

	cpu_usage = [float(i[0]) for i in cpu]
	cpu_min = [float(i[1]) for i in cpu]
	cpu_max = [float(i[2]) for i in cpu]

	mem_usage = [float(i[0]) for i in mem]
	mem_min = [float(i[1]) for i in mem]
	mem_max = [float(i[2]) for i in mem]

	i = 0
	print(len(cpu_usage))
	steps = np.arange(0, len(cpu_usage), 1)


	# ax = sns.lineplot(x=steps[61125:], y=cpu_usage[61125:], data=cpu_usage, lw=1, color='red')
	# ax = sns.lineplot(x=steps[61125:], y=cpu_max[61125:], data=cpu_max[61125:], lw=1)
	# ax = sns.lineplot(x=steps[61125:], y=cpu_min[61125:], data=cpu_min[61125:], lw=1)

	ax = sns.lineplot(x=steps[:100], y=cpu_usage[100:200], data=cpu_usage, lw=1, color='red')
	ax = sns.lineplot(x=steps[:100], y=cpu_max[100:200], data=cpu_max[100:200], lw=1)
	ax = sns.lineplot(x=steps[:100], y=cpu_min[100:200], data=cpu_min[100:200], lw=1)
	
	ax.margins(x=0)				#remove the ugly inner side margin 

	ax.set_ylabel('CPU (m)', fontsize=12)
	ax.set_xlabel('Steps', fontsize=12)

	# ax.set_ylabel('Memory (MiB)', fontsize=12)
	# ax.set_xlabel('Steps', fontsize=12)


	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(12)
	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(12)
	#plt.yscale("log")	

	#plt.legend(loc='upper center', labels=['Usage', 'Limits', "Request"], fontsize=12, bbox_to_anchor=(0.5, 1.1), ncol=3)
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()

if __name__ == '__main__':
	main()