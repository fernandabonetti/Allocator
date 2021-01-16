from scapy.all import *
from scapy import *
from scapy.utils import rdpcap
from scapy.utils import wrpcap
import string 
import random 
import time

def main():
	if len(sys.argv) < 1:
		print("Provide the filename of a .pcap archive")
		exit(1)
	filename = sys.argv[1]
	packets = rdpcap(filename, 85000)

	timestamp = [str(packets[i+1].time-packets[i].time)+'\n' for i in range(1, len(packets)-1)]
	# length = [str(packet.len)+'\n' for packet in packets]
	length = []
	for packet in packets:
		try:
			length.append(str(packet.len)+'\n')
		except AttributeError:
			length.append('500\n')

	with open('timestamps.txt', 'a') as fp, open('length.txt', 'a') as fr:
		fp.writelines(timestamp)
		fr.writelines(length)

if __name__ == '__main__':
	main()