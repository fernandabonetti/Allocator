#!/bin/sh
kubectl delete deployment squid --namespace default --grace-period=0 --force
kubectl create -f deployment.yaml
kubectl apply -f service.yaml

