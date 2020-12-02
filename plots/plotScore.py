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

	episodes = []
	score = []
	for record in data.values():
		if 'score' in record["message"].keys():
			score.append(int(record["message"]["score"]))
			episodes.append(int(record["message"]["episode"][:-5]))
			
	sns.set_theme(style="darkgrid")

	ax = sns.lineplot(x=episodes, y=score, data=score)
	ax.xaxis.set_major_locator(ticker.MultipleLocator(100))	#set x ticks interval
	ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
	ax.margins(x=0)				#remove the ugly inner side margin 

	ax.set_title('Total Score by Episode')
	ax.set_ylabel('Score Amount')
	ax.set_xlabel('Episode')
	plt.show()

if __name__ == '__main__':
	main()

