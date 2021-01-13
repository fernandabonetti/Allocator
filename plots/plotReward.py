import json
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

def main():
	if len(sys.argv) < 1:
		print("ooo")
		exit(1)
	filename = sys.argv[1]
	
	data = {}
	with open(filename, 'r') as fp:
		for index, line in enumerate(fp.readlines()):
			data.update({index: json.loads(line)})

	rewards = []
	episodes = []
	steps = []
	mean = []
	eps = []

	for record in data.values():
		if 'Total Reward' in record["message"].keys():
			episodes.append(float(record["message"]["Episode"]))
			rewards.append(float(record["message"]["Total Reward"]))
			steps.append(int(record["message"]["Steps"])+1)

	# # for i in range(0,len(rewards)):
	# # 	mean.append(rewards[i]/steps[i])
	# i = 0
	# top = 100
	# while i <= len(rewards)-100:
	# 	mean.append(sum(rewards[x] for x in range(i,top))/100)
	# 	eps.append(i+100)
	# 	i+=100
	# 	top+=100

	ax = sns.lineplot(x=episodes, y=rewards, data=rewards)
	#ax = sns.lineplot(x=eps, y=mean, data=mean)
	ax.xaxis.set_major_locator(ticker.MultipleLocator(100))	#set x ticks interval
	ax.xaxis.set_major_formatter(ticker.ScalarFormatter())

	ax.margins(x=0)				#remove the ugly inner side margin 

	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(20)
	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(20)
	#ax.set_title('Average Reward by Episode')
	ax.set_ylabel('Reward Amount', fontsize=20)

	ax.set_xlabel('Episode', fontsize=20)
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()
if __name__ == '__main__':
	main()	
