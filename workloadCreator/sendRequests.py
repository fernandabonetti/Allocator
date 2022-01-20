import requests
import time

address = "http://192.168.49.2:32311"
headers = {'Host': 'foo.bar'}

def main():
	with open('timestamps.txt', 'r') as fp:
		delay = [float(line) for line in fp.readlines()]

	for i in range(0, len(delay)):
		r = requests.get(address, headers=headers)
		time.sleep(delay[i])
		print(".")
	
if __name__ == '__main__':
	main()
