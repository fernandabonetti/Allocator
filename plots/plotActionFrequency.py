import json
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

def main():

	with open('action.csv', 'r') as fp:
		action = [int(line) for line in fp.readlines()]
	
	action.sort()	
	sns.set(font_scale=0.6)

	# Histograma de ações
	ax = sns.countplot(x=action)
	ax.margins(x=0)				#remove the ugly inner side margin 

	ax.set_title('Frequency of actions taken by Agent', fontsize=12)
	ax.set_ylabel('Number of times the action was chosen', fontsize=10)
	ax.set_xlabel('Action Number', fontsize=10)

	# put count above each column	
	for p in ax.patches:
		height = p.get_height()
		ax.text(p.get_x()+p.get_width()/2., height + 0.1, height, ha="center")
	
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()

if __name__ == '__main__':
	main()