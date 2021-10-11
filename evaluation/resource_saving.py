import os
import sys
import pandas as pd

parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent)

from utils.reader import read_usage

def utilization(resource):
	'''
	Calculates resource overutilization and underutilization
	'''
	resource_over = 0
	resource_under = 0

	for i in resource.itertuples():
		resource_over += abs(i.max - i.usage)
		resource_under += abs(i.usage - i.min)

	return resource_over, resource_under	

cpu = read_usage('../plots/cpu.csv')
mem = read_usage('../plots/mem.csv')

print(utilization(cpu))
	

print(cpu_under, cpu_over)
