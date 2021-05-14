import matplotlib.pyplot as plt
import numpy as np

f1 = "../evaluation/results/test-1-vnf-snort.txt"
f2 = "../evaluation/results/test-2-vnfs-time.txt"
f3 = "../evaluation/results/test-4-time.txt"


with open(f1, 'r') as fp, open(f2, 'r') as fr, open(f3, 'r') as ft:
	t1 = [line.replace('\n', '').split(" ") for line in fp.readlines()]
	t2 = [line.replace('\n', '').split(" ") for line in fr.readlines()]
	t3 = [line.replace('\n', '').split(" ") for line in ft.readlines()]

steps = np.arange(0, 100, 1)

mem = []
cpu = []
for i in range(0, len(t1)):
	cpu.append([t1[i][0], t2[i][0], t3[i][0]])
	mem.append([t1[i][1], t2[i][1], t3[i][1]])

mem = np.array(mem).astype(float)
cpu = np.array(cpu).astype(float)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.margins(x=0)
ax2.margins(x=0)

for i in range(0, 3):
	ax1.plot(steps, cpu[:,i], linewidth=2)
for i in range(0, 3):
	ax2.plot(steps, mem[:,i], linewidth=2)

ax1.set(xlabel='Steps', ylabel='CPU (m)')
ax2.set(xlabel='Steps', ylabel='Memory (MiB)')
ax2.legend(loc="upper left", title="# of VNFs", labels=['1', '2', "4"], bbox_to_anchor=[1, 1], ncol=1, fancybox=True)

plt.show()