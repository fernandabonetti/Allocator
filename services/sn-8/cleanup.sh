#!/bin/sh
kubectl delete deployment sn-8 --namespace snort-8 --grace-period=0 --force
kubectl create -f deployment.yaml
