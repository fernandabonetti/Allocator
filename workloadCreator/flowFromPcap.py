from scapy.all import *
from scapy import *
from scapy.utils import rdpcap
from scapy.utils import wrpcap
import string 
import random 
import time

def sendPackets(packets, delay):
	for i, packet in enumerate(packets):
		sendp(packet, iface="eth1")
		time.sleep(delay[i])

def editPcap(packets):
	payload = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 500))
	template = Ether()/IP(src="192.168.49.1", dst="192.168.49.2")/UDP(sport=80, dport=52148)/Raw(load=payload)

	timestamp = []
	craftedPackets = []
	for i in range(0, len(packets)-1):
	#	if i > 0: timestamp.append(packets[i+1].time-packets[i].time)                                                                                                                                                                                    
		#timestamp.append(packets[i].time)
		template.time = packets[i].time
		template.send_time = packet[i].sent_time
		craftedPackets.append(template)
		template.show2()
	wrpcap("trigger-workload.pcap", craftedPackets)

	with open('timestamps.txt', 'w') as fp:
		for time in timestamp:
			fp.write(str(time)+'\n')

	return craftedPackets, timestamp		

def main():
	if len(sys.argv) < 1:
		print("Provide the filename of a .pcap archive")
		exit(1)
	filename = sys.argv[1]
	packets = rdpcap(filename)

	packets, timestamp = editPcap(packets)
	sendPackets(packets)

if __name__ == '__main__':
	main()