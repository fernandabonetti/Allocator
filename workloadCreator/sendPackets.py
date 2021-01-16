from scapy.all import *
import string 
import random 

def main():
	payload = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 1500))
	with open('timestamps.txt', 'r') as fp, open('length.txt', 'r') as fr:
		delay = [float(line) for line in fp.readlines()]
		length = [int(line) for line in fr.readlines()]

	for i in range(0, len(delay)):
		template = IP(dst='192.168.49.2')/UDP(sport=5666, dport=5444)
		padding = payload[0:(length[i]-28)]			#28 is to fill the size of previous layers 
		send(template/Raw(padding), return_packets=True)
		time.sleep(delay[i])
	
if __name__ == '__main__':
	main()