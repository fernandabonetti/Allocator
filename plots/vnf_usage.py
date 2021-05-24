import matplotlib.pyplot as plt
import numpy as np

f1 = "../evaluation/results/22-05/test-1-vnf-snort.txt"
f2 = "../evaluation/results/22-05/test-2-vnf-snort.txt"
f3 = "../evaluation/results/22-05/test-4-vnf-snort.txt"
f4 = "../evaluation/results/22-05/test-8-vnf-snort.txt"

with open(f1, 'r') as fp, open(f2, 'r') as fr, open(f3, 'r') as ft, open(f4, 'r') as fk:
	t1 = [line.replace('\n', '').split(" ") for line in fp.readlines()]
	t2 = [line.replace('\n', '').split(" ") for line in fr.readlines()]
	t3 = [line.replace('\n', '').split(" ") for line in ft.readlines()]
	t4 = [line.replace('\n', '').split(" ") for line in fk.readlines()]

steps = np.arange(0, 200, 1)

mem = []
cpu = []
for i in range(0, len(t1)):
	cpu.append([t1[i][0], t2[i][0], t3[i][0], t4[i][0]])
	mem.append([t1[i][1], t2[i][1], t3[i][1], t4[i][1]])

mem = np.array(mem).astype(float)
cpu = np.array(cpu).astype(float)

mean_1 = np.median(mem[:,0])
mean_2 = np.median(mem[:,1])
mean_3 = np.median(mem[:,2])
mean_4 = np.median(mem[:,3])

print(mean_1, mean_2, mean_3, mean_4)
print(np.var(mem[:,0]))
print(np.var(mem[:,1]))
print(np.var(mem[:,2]))
print(np.var(mem[:,3]))
# plt.margins(x=0)

# for i in range(0, 4):
# 	plt.plot(steps, mem[:,i], linewidth=2)

# plt.xlabel(xlabel='Steps')
# plt.ylabel(ylabel='Memory (MiB)')
# plt.legend(loc="upper left", title="# of VNFs", labels=['1', '2', "4", "8"], bbox_to_anchor=[1, 1], ncol=1, fancybox=True)



# fig, (ax1, ax2) = plt.subplots(2, 1)
# ax1.margins(x=0)
# ax2.margins(x=0)

# for i in range(0, 4):
# 	ax1.plot(steps, cpu[:,i], linewidth=2)
# for i in range(0, 4):
# 	ax2.plot(steps, mem[:,i], linewidth=2)

# fig.tight_layout()

# ax1.set(xlabel='Steps', ylabel='CPU (m)')
# ax2.set(xlabel='Steps', ylabel='Memory (MiB)')
# ax1.legend(loc="upper left", title="# of VNFs", labels=['1', '2', "4", "8"], bbox_to_anchor=[1, 1], ncol=1, fancybox=True)

plt.show()