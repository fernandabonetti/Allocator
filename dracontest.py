from metricsAPI import Collector
from utils.logger import logger
from utils.parser import Props
import time

container = "dracon"
namespace = "default"

props = Props()

collector = Collector(props.ip, props.port, container, namespace)

for i in range(200):
	cpu_usage, mem_usage = collector.get_resource_usage()

	time.sleep(20)

	print(cpu_usage, mem_usage)
