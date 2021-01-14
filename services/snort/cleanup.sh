#!/bin/sh
kubectl delete deployment docker-snort --namespace default --grace-period=0 --force
kubectl create -f deployment.yaml
