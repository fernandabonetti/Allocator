FROM python:3.8-slim-buster

WORKDIR /project

COPY requirements.txt requirements.txt

RUN apt-get update && \
		pip3 install -r requirements.txt

COPY . .

RUN cd AllocatorGym/ && pip install -e .

CMD ["bash", "-c", "python3 main.py"]