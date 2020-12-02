import json
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

def main():
	if len(sys.argv) < 1:
		exit(1)
	filename = sys.argv[1]
	
	data = {}

	with open(filename, 'r') as fp:
		for index, line in enumerate(fp.readlines()):
			data.update({index: json.loads(line)})

	action = []
	for record in data.values():
		if 'action' in record["message"].keys():
			action.append(int(record["message"]["action"]))
	action.sort()	
	sns.set_theme(style="darkgrid")
	sns.set(font_scale=0.6)

	ax = sns.countplot(x=action)
	ax.margins(x=0)				#remove the ugly inner side margin 

	ax.set_title('Frequency of actions taken by Agent')
	ax.set_ylabel('Number of times the action was chosen')
	ax.set_xlabel('Action Number')
	plt.show()

if __name__ == '__main__':
	main()

