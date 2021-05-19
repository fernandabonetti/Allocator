#!/bin/sh
kubectl delete deployment sn-6 --namespace snort-6 --grace-period=0 --force
kubectl create -f deployment.yaml
