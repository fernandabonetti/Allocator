from metricsAPI import Collector
from utils.logger import logger
from utils.parser import Props
from utils.CircularList import CircularList, Node


num_episodes = 100 
props = Props()

for i in range(len(props.container)):
	collector = Collector(props.ip, props.port, props.container[i], props.namespaces[i])
	node = Node(props.container[i], props.namespaces[i], collector, None)
	vnfs.insert(node)

cpu_lower = 90
cpu_upper = 180
mem_lower = 90
mem_upper = 180

for i in range(num_episodes):
	cpu_usage, mem_usage = collector.get_resource_usage()

	if cpu_usage >= cpu_upper:
		cpu_upper += 0.1 * cpu_upper

	if cpu_usage <= cpu_lower:
		cpu_lower -= 0.1 * cpu_lower

	if mem_usage >= mem_upper:
		mem_upper += 244.141

	if mem_usage <= mem_lower:
		mem_lower -= 122.07	

	collector.change_allocation(cpu_lower, cpu_upper, mem_lower, mem_upper)

	logger.info("{},{},{},{},{},{}".format(cpu_usage, cpu_lower, cpu_upper, cpu_usage, mem_lower, mem_upper))	
		

	
