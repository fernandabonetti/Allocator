import os
import time
from subprocess import run

command = "kubectl top pods"

for i in range(1440):
	run(command, shell=True)
	time.sleep(60)
