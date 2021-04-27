from metricsAPI import Collector
from utils.logger import logger
from utils.parser import Props
from utils.CircularList import CircularList, Node

props = Props()

for i in range(len(props.container)):
	collector = Collector(props.ip, props.port, props.container[i], props.namespaces[i])
	node = Node(props.container[i], props.namespaces[i], collector, None)
	vnfs.insert(node)

cpu_threshold = 0
mem_threshold = 0	

for i in range(num_episodes):
	cpu_usage, mem_usage = collector.get_resource_usage()

	if cpu_usage >= cpu_upper:
		cpu_threshold += 0.1 * cpu_upper

	if cpu_usage <= cpu_lower:
		cpu_threshold -= 0.1 * cpu_lower
		

	
