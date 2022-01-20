#!/bin/sh

# teste com uma VNF
kubectl apply -f services/docker-snort/deployment_old.yaml
kubectl apply -f evaluation/scalability/agent.yaml
sleep 4m
python3 dracontest.py > test-1-vnf-snort.txt
kubectl delete deployment -n snort-1 docker-snort
kubectl delete deployment dracon
sleep 10m

# # teste com 2 VNFs
kubectl apply -f services/docker-snort/deployment_old.yaml
kubectl apply -f services/snort-docker/deployment_old.yaml
kubectl apply -f evaluation/scalability/agent_2.yaml
sleep 4m
python3 dracontest.py > test-2-vnf-snort.txt
kubectl delete deployment -n snort-1 docker-snort
kubectl delete deployment -n snort-2 snort-docker
kubectl delete deployment dracon
sleep 10m

# # teste com 4 VNFs
kubectl apply -f services/docker-snort/deployment_old.yaml
kubectl apply -f services/snort-docker/deployment_old.yaml
kubectl apply -f services/sn-3/deployment_old.yaml
kubectl apply -f services/sn-4/deployment_old.yaml
kubectl apply -f evaluation/scalability/agent_4.yaml
sleep 4m
python3 dracontest.py > test-4-vnf-snort.txt
kubectl delete deployment -n snort-1 docker-snort
kubectl delete deployment -n snort-2 snort-docker
kubectl delete deployment -n snort-3 sn-3
kubectl delete deployment -n snort-4 sn-4
kubectl delete deployment dracon
sleep 10m

# # teste com 8 VNFs
kubectl apply -f services/docker-snort/deployment_old.yaml
kubectl apply -f services/snort-docker/deployment_old.yaml
kubectl apply -f services/sn-3/deployment_old.yaml
kubectl apply -f services/sn-4/deployment_old.yaml
kubectl apply -f services/sn-5/deployment_old.yaml
kubectl apply -f services/sn-6/deployment_old.yaml
kubectl apply -f services/sn-7/deployment_old.yaml
kubectl apply -f services/sn-8/deployment_old.yaml
kubectl apply -f evaluation/scalability/agent_8.yaml
sleep 4m
python3 dracontest.py > test-8-vnf-snort.txt
kubectl delete deployment -n snort-1 docker-snort
kubectl delete deployment -n snort-2 snort-docker
kubectl delete deployment -n snort-3 sn-3
kubectl delete deployment -n snort-4 sn-4
kubectl delete deployment -n snort-5 sn-5
kubectl delete deployment -n snort-6 sn-6
kubectl delete deployment -n snort-7 sn-7
kubectl delete deployment -n snort-8 sn-8
kubectl delete deployment dracon
sleep 10m
