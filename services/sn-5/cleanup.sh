#!/bin/sh
kubectl delete deployment sn-5 --namespace snort-5 --grace-period=0 --force
kubectl create -f deployment.yaml
