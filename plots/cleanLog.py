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

	score = []
	reward = []
	action = []
	cpu = []
	mem = []
	loss = []
	for record in data.values():
		if 'Steps' in record["message"].keys():
			score.append(str(int(record["message"]["Steps"])+1)+'\n')
			reward.append(record["message"]["Total Reward"]+'\n')
		if 'action' in record["message"].keys():
			action.append(record["message"]["action"]+'\n')
			state = [value for value in record["message"]["state"][2:].replace(']', '').split(' ') if value != '']
			cpu.append(state[0]+','+state[1]+','+state[2]+'\n')
			mem.append(state[3]+','+state[4]+','+state[5]+'\n')
		if 'loss' in record["message"].keys():
			loss.append(record["message"]["loss"][1:-1]+'\n')

	fs = open('score.csv', 'a')
	fr = open('reward.csv', 'a')
	fa = open('action.csv', 'a')
	fc = open('cpu.csv', 'a')
	fm = open('mem.csv', 'a')
	fl = open('loss.csv', 'a')

	fs.writelines(score)
	fr.writelines(reward)
	fa.writelines(action)
	fc.writelines(cpu)
	fm.writelines(mem)
	fl.writelines(loss)

if __name__ == '__main__':
	main()
