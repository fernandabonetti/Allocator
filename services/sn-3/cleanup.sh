#!/bin/sh
kubectl delete deployment sn-3 --namespace snort-3 --grace-period=0 --force
kubectl create -f deployment.yaml
