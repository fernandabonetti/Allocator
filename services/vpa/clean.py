import yaml

with open('outputvpa2.yaml') as stream:
	data = list(yaml.safe_load_all(stream))

cleaned = []

for sample in data:
	print(sample)
	cpu_l = sample['Events']['Lower Bound']['Cpu'][:-1]
	cpu_t = sample['Events']['Target']['Cpu'][:-1]
	cpu_u = sample['Events']['Upper Bound']['Cpu'][:-1]
	mem_l = sample['Events']['Lower Bound']['Memory'][:-1]
	mem_t = sample['Events']['Target']['Memory'][:-1]
	mem_u = sample['Events']['Upper Bound']['Memory']

	s = f"{cpu_l},{cpu_t},{cpu_u},{mem_l},{mem_t},{mem_u}"
	cleaned.append(s)

for i in range(1, len(cleaned)-1):
		cleaned[i-1] = cleaned[i-1]+','+ cleaned[i]+'\n'

with open("predictions_2.csv", 'w') as fw:
	fw.writelines(cleaned)
