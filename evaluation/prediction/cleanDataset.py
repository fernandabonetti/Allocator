import json
import sys
import matplotlib.pyplot as plt
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

	usage = []
	for record in data.values():
		if 'action' in record["message"].keys():
			state = [value for value in record["message"]["state"][2:].replace(']', '').split(' ') if value != '']
			next_st = [value for value in record["message"]["next_state"][2:].replace(']', '').split(' ') if value != '']
			usage.append(state[0]+','+state[3]+','+next_st[0]+','+next_st[3]+'\n')

	fc = open('usage.csv', 'a')
	fc.writelines(usage)

if __name__ == '__main__':
	main()
