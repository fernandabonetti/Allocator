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

	score = []
	reward = []
	action = []
	for record in data.values():
		if 'Steps' in record["message"].keys():
			score.append(str(int(record["message"]["Steps"])+1)+'\n')
			reward.append(record["message"]["Total Reward"]+'\n')
		if 'action' in record["message"].keys():
			action.append(record["message"]["action"]+'\n')

	fs = open('score.csv', 'a')
	fr = open('reward.csv', 'a')
	fa = open('action.csv', 'a')

	fs.writelines(score)
	fr.writelines(reward)
	fa.writelines(action)

if __name__ == '__main__':
	main()
