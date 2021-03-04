#!/bin/bash

sudo add-apt-repository ppa:deadsnakes/ppa   
sudo apt-get update   
sudo apt install python3.6

sudo apt-get install python3.6-venv python3.6-dev
virtualenv --python python3.6 venv
source venv/bin/activate

#sudo pip3 install requirements.txt