from dotenv import load_dotenv
import os

class Props():
	def __init__(self):
		load_dotenv('.env')
		self.ip = os.getenv("IP")
		self.port = os.getenv("PORT")
		self.container = [os.getenv("CONTAINER").split(',')]
		self.namespaces = [os.getenv("NAMESPACE").split(',')]
		self.output_dir = os.getenv("OUTPUT_DIR")

		# a and b are 'boundness' parameters of each resource
		self.a = float(os.getenv("A"))
		self.b = float(os.getenv("B"))
		self.peak = int(os.getenv("PEAK"))