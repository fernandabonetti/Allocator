#!/bin/sh
kubectl delete deployment sn-7 --namespace snort-7 --grace-period=0 --force
kubectl create -f deployment.yaml
