import logging

class Logger():
	def __init__(self):
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.INFO)
		handler = logging.FileHandler('dracon.log')

		file_formatter=logging.Formatter("{'time':'%(asctime)s','message': {'%(message)s'}}")
		handler.setFormatter(file_formatter)
		self.logger.addHandler(handler)