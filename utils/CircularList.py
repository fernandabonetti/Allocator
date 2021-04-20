class Node:
	def __init__(self, container_name, namespace, collector, next):
		self.container = container_name
		self.namespace = namespace
		self.collector = collector
		self.next = next

class CircularList:
	def __init__(self, head, tail, len=0):
		self.head = head
		self.tail = tail
		self.len = len

	def insert(self, node):
		if self.len < 1:
			node.next = node
			self.tail = node
			self.head = node
		node.next = self.head
		self.head = node
		self.tail.next = self.head
		self.len += 1

	def iterate(self):
		it = self.head
		for i in range(self.len):
			print(it.container)
			it = it.next	 
