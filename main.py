import resourceCollector as rc

ip = '192.168.39.87'
port = '32590'
container = 'resource-consumer'

collector = rc.Collector(ip, port)
collector.getMemory(container)
