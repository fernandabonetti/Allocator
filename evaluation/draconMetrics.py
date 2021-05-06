from metricsAPI import Collector
from utils.logger import logger
from utils.parser import Props
from utils.CircularList import CircularList, Node
import time

container = "dracon"
namespace = "default"

props = Props()

collector = Collector(props.ip, props.port, container, namespaces)

for i in range(100):

	cpu_usage, mem_usage = collector.get_resource_usage()

	time.sleep(20)

	print(cpu_usage, mem_usage)