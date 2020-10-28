from scapy.all import *
from scapy import *
from scapy.utils import rdpcap
from scapy.utils import wrpcap

def main():
	if len(sys.argv) < 1:
		print("Provide the filename of a .pcap archive")
		exit(1)

	filename = sys.argv[1]
	packets = rdpcap(filename, 1000)

	for packet in packets:
		if packet[IP]:
			del packet[IP].chksum
			packet[IP].src = "192.168.32.120"
			packet[IP].dst = "192.168.32.129"

			if TCP in packet:
				packet[TCP].sport = 80
				packet[TCP].dport = 30006
			elif UDP in packet:
				packet[UDP].sport = 80
				packet[UDP].dport = 30006	
				
	wrpcap("workload.pcap", packets)

if __name__ == '__main__':
	main()