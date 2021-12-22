## Calculate amount of regret = optimal action - action taken 
from utils.reader import read_metrics,read_usage
import pandas as pd


	def calculate_reward(cpu, mem, action):
		pass
	
	def main():
		cpu = read_usage('../cpu.csv')
		mem = read_usage('../mem.csv')

		taken_actions = read_metrics('actions.csv', 'int')
		granted_rewards = read_metrics('rewards.csv','float')
		#TODO: read array of actions dracon
		

		calculate_reward(cpu, mem, action)


if __name__ == "__main__":
	main()