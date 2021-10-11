import matplotlib.pyplot as plt
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

	steps = np.arange(0, len(cpu_usage), 1)

	plt.plot(steps, mem_usage, lw=2, color='#edd400ff')
	plt.plot(steps, mem_max, lw=2)
	plt.plot(steps, mem_min, lw=2, color='#ff0000ff')

	# plt.plot(steps, cpu_usage, lw=2, color='#edd400ff')
	# plt.plot(steps, cpu_max, lw=2)
	# plt.plot(steps, cpu_min, lw=2, color='#ff0000ff')
	
	plt.margins(x=0)				#remove the ugly inner side margin 

	#plt.ylabel('CPU (m)', fontsize=12)
	plt.ylabel('Memory (MiB)', fontsize=12)
	plt.xlabel('Steps', fontsize=12)

	plt.xticks(fontsize=14)
	plt.yticks(fontsize=14)
	#plt.yscale("log")	

	plt.legend(loc='upper center', labels=['Usage','Max',"Min"], fontsize=12, bbox_to_anchor=(0.5, 1.15), ncol=3)
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()

if __name__ == '__main__':
	main()