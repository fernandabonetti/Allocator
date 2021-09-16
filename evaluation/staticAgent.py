from metricsAPI import Collector
from utils.logger import logger
from utils.parser import Props
from utils.CircularList import CircularList, Node
import time

num_episodes = 1000
props = Props()

vnfs = CircularList(None, None, 0)

for i in range(len(props.container)):
	collector = Collector(props.ip, props.port, props.container[i], props.namespaces[i])
	node = Node(props.container[i], props.namespaces[i], collector, None)
	vnfs.insert(node)

cpu_lower = 90
cpu_upper = 180
mem_lower = 90
mem_upper = 180

for i in range(num_episodes):
	vnf = vnfs.head

	cpu_usage, mem_usage = vnf.collector.get_resource_usage()

	logger.info("{}, {}, {}, {}, {}, {}".format(cpu_usage, cpu_lower, cpu_upper, mem_usage, mem_lower, mem_upper))
	
	if cpu_usage >= cpu_upper:
		cpu_upper += 0.1 * cpu_upper

	if cpu_usage <= cpu_lower:
		cpu_lower -= 0.1 * cpu_lower
		if cpu_lower < 0: cpu_lower = 0

	if mem_usage >= mem_upper:
		mem_upper += 244.14

	if mem_usage <= mem_lower:
		mem_lower -= 122.07	
		if mem_lower < 0: mem_lower = 0

	vnf.collector.change_allocation(cpu_upper, mem_upper, cpu_lower, mem_lower)

	vnf = vnf.next
	time.sleep(20)
	#logger.info("{}, {}, {}, {}, {}, {}".format(cpu_usage, cpu_lower, cpu_upper, mem_usage, mem_lower, mem_upper))
		

	
