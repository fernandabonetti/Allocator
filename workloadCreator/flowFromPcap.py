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
			#del packet[IP].chksum
			#del packet[IP].len
			#packet[IP].src = "192.168.49.1"
			packet[IP].dst = "192.168.49.2"
			packet[IP].proto = 17

			if TCP in packet:
				del packet[TCP]
				packet = packet[IP]/UDP(sport=80, dport=52148)

			# 	packet[TCP].sport = 80
			# 	packet[TCP].dport = 30006
			# 	#del packet[TCP].len
			# 	packet[TCP].options = [('Timestamp',(0,0))]
			#		elif UDP in packet:
			# 	del packet[UDP].len
			# 	del packet[UDP].chksum
			# 	packet[UDP].sport = 80
			# 	packet[UDP].dport = 30006
			#packet = Ether(packet.build())
			packet.show()	


	#wrpcap("workload.pcap", packets)

	#sendp(packets, iface="enp2s0f1")

if __name__ == '__main__':
	main()