FROM python:3.7-slim-buster

WORKDIR /project

COPY setup_baselines/requirements.txt requirements.txt

RUN apt-get update && \
		apt-get install -y libgl1-mesa-dev libglib2.0-0 libsm6 libxrender1 libxext6 jq apt-transport-https gnupg2 curl && \
		pip3 install -r requirements.txt && \
		curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
		echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list && \
		apt-get update && apt-get install -y kubectl

COPY . .

#CMD ["bash", "-c", "python3 baselinesAgent.py AllocatorGym/envs/AllocatorEnv/AllocatorEnv.py"]