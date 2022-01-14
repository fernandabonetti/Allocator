import os
import time
from subprocess import run

command = "kubectl describe vpa vpa | tail -13"

for i in range(1440):
	run(command, shell=True)
	time.sleep(60)