#!/bin/sh
kubectl delete deployment sn-4 --namespace snort-4 --grace-period=0 --force
kubectl create -f deployment.yaml
