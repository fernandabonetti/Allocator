from time import altzone
import matplotlib.pyplot as plt
from matplotlib.style import context
import numpy as np
import seaborn as sns

import pandas as pd

# f1 = "../evaluation/results/22-05/test-1-vnf-snort.txt"
# f2 = "../evaluation/results/22-05/test-2-vnf-snort.txt"
# f3 = "../evaluation/results/22-05/test-4-vnf-snort.txt"
# f4 = "../evaluation/results/22-05/test-8-vnf-snort.txt"

f1 = "../evaluation/scalability/teste1/test-1-vnf-snort.txt"
f2 = "../evaluation/scalability/teste1/test-2-vnf-snort.txt"
f3 = "../evaluation/scalability/teste1/test-4-vnf-snort.txt"
f4 = "../evaluation/scalability/teste1/test-8-vnf-snort.txt"

cpu = pd.DataFrame({})

with open(f1, 'r') as fp, open(f2, 'r') as fr, open(f3, 'r') as ft, open(f4, 'r') as fk:
	cpu['1'] = np.array([line.replace('\n', '').split(" ")[0] for line in fp.readlines()], dtype=float)
	cpu['2'] = np.array([line.replace('\n', '').split(" ")[0] for line in fr.readlines()], dtype=float)
	cpu['3'] = np.array([line.replace('\n', '').split(" ")[0] for line in ft.readlines()], dtype=float)
	cpu['4'] = np.array([line.replace('\n', '').split(" ")[0] for line in fk.readlines()], dtype=float)

cpu['steps'] = np.arange(0, 200, 1)
cpu.set_index('steps')

sns.set(font_scale=1)
sns.set_style("ticks")

fig, axs = plt.subplots(4, sharex=True, sharey=True, gridspec_kw={'hspace': 0})

ci = 1.96 * np.std(cpu['1'])/np.sqrt(len(cpu['steps']))
p = sns.lineplot(x=cpu['steps'], y=cpu['1'], ci=95, data=cpu['1'], linewidth=0.4, color='#404040', ax=axs[0])
p.fill_between(cpu['steps'], (cpu['1']-ci), (cpu['1']+ci), alpha=.4, color="purple")
p.margins(x=0)

ci = 1.96 * np.std(cpu['2'])/np.sqrt(len(cpu['steps']))
p2 = sns.lineplot(x=cpu['steps'], y=cpu['2'], ci=95, data=cpu['2'], linewidth=0.4, color='#404040', ax=axs[1])
p2.fill_between(cpu['steps'], (cpu['2']-ci), (cpu['2']+ci), alpha=.5, color='orange')
p2.margins(x=0)

ci = 1.96 * np.std(cpu['3'])/np.sqrt(len(cpu['steps']))
p3 = sns.lineplot(x=cpu['steps'], y=cpu['3'], ci=95, data=cpu['3'], linewidth=0.4, color='#404040', ax=axs[2])
p3.fill_between(cpu['steps'], (cpu['3']-ci), (cpu['3']+ci), color='b', alpha=.3)
p3.margins(x=0)


ci = 1.96 * np.std(cpu['4'])/np.sqrt(len(cpu['steps']))
p4 = sns.lineplot(x=cpu['steps'], y=cpu['4'], ci=95, data=cpu['4'], color='#202020', linewidth=0.4, ax=axs[3])
p4.fill_between(cpu['steps'], (cpu['4']-ci), (cpu['4']+ci), color='red', alpha=.3)
p4.margins(x=0)
 
for ax in axs.flat:
	ax.set(xlabel='Steps', ylabel='CPU (m)')


# p.set_xlabel("Steps", fontsize = 12)
# p.set_ylabel("Memory (MiB)", fontsize = 12)
p.legend(loc='upper left', labels=['1 VNF'])
p2.legend(loc='upper left', labels=['2 VNF'])
p3.legend(loc='upper left', labels=['4 VNF'])
p4.legend(loc='upper left', labels=['8 VNF'])

plt.show()