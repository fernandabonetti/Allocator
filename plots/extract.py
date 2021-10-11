import json
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def main():

	with open("mem.csv", 'r') as fp:
		data = [line.replace('\n', '').split(',') for line in fp.readlines()]

		steps = np.arange(0, len(data), 1)
		cpu_usage = [float(i[0]) for i in data]
		cpu_low = [float(i[1]) for i in data]
		cpu_hi = [float(i[2]) for i in data]

		mem_usage = [float(i[3]) for i in data]
		mem_low = [float(i[4]) for i in data]
		mem_hi = [float(i[5]) for i in data]

		# plt.plot(steps, cpu_usage, linewidth=2)
		# plt.plot(steps, cpu_low,linewidth=2)
		# plt.plot(steps, cpu_hi, linewidth=2)
		# plt.margins(x=0)
		# #plt.legend(bbox_to_anchor=(0.7, 0.5), loc='upper left', labels=['Usage', 'Min', "Max"], fontsize=10)
		# plt.ylabel('CPU (m)', fontsize=12)
		# plt.xlabel('Steps', fontsize=12)
		
		plt.plot(steps, mem_usage, linewidth=2)
		plt.plot(steps, mem_low,linewidth=2)
		plt.plot(steps, mem_hi, linewidth=2)
		plt.margins(x=0)
		#plt.legend(bbox_to_anchor=(0.7, 0.8), loc='upper left', labels=['Usage', 'Min', "Max"], fontsize=10)
		plt.ylabel('Memory (MiB)', fontsize=12)
		plt.xlabel('Steps', fontsize=12)

		plt.show()

if __name__ == '__main__':
	main()