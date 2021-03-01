FROM python:3.7-slim-buster

WORKDIR /project

COPY setup_baselines/requirements.txt requirements.txt

RUN apt-get update && \
		apt-get install -y libgl1-mesa-dev libglib2.0-0 libsm6 libxrender1 libxext6 && \
		pip3 install -r requirements.txt

COPY . .

CMD ["bash", "-c", "python3 baselinesAgent.py AllocatorGym/envs/AllocatorEnv/AllocatorEnv.py"]