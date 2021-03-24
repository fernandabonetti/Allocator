from subprocess import PIPE, run

def main():
	with open('timestamps.txt', 'r') as fp:
		delay = [float(line) for line in fp.readlines()]

	for i in range(0, len(delay)):
		command = "curl -x http://192.168.49.2:3128 https://en.wikipedia.org/wiki/Wikipedia:Random" 
		result = run(command, stdout=PIPE, universal_newlines=True, shell=True)
		time.sleep(delay[i])
	
if __name__ == '__main__':
	main()