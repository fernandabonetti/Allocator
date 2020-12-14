from scapy.all import *
import string 
import random 

def main():
	payload = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 500))
	with open('timestamps.txt', 'r') as fp:
		delay = [float(line) for line in fp.readlines()]

	for i in range(0, len(delay)):
		send(IP(dst='192.168.49.2')/UDP(sport=5666, dport=5444)/Raw(payload), return_packets=True)
		time.sleep(delay[i])
	
if __name__ == '__main__':
	main()