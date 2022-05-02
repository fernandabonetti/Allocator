#!/bin/sh
kubectl delete deployment nginx --grace-period=0 --force
kubectl create -f deployment.yaml
