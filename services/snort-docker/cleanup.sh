#!/bin/sh
kubectl delete deployment snort-docker --namespace snort-2 --grace-period=0 --force
kubectl create -f deployment.yaml
