import os
import time
from subprocess import run

command = "kubectl describe vpa vpa | tail -13"

for i in range(720):
	run(command, shell=True)
	time.sleep(60)
