# Allocator

Allocation Agent for Containerized NFs.


## Prerequisites

* Kubernetes v1.19 or greater
* Prometheus Deployment (see services/prometheus)

To install the project dependencies, run:

```sh
pip3 install -r requirements.txt
```

## Installation  

1. Clone the repo

```sh
git clone https://github.com/fernandabonetti/Allocator.git
```

2. Install Gym Environment

```sh
pip install -e AllocatorGym
```
## Usage

1. Create a `.env` file accordingly to `.env.example` with your custom values.

2. Execute the agent with `python3 main.py`

3. Training logs are stored in `logs/agent.log`

  
  
 

  