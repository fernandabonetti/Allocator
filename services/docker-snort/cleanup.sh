#!/bin/sh
kubectl delete deployment docker-snort --namespace snort-1 --grace-period=0 --force
kubectl create -f deployment.yaml
kubectl apply -f service.yaml
