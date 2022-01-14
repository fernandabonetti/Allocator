#!/bin/sh
kubectl delete deployment haproxy-ingress  --grace-period=0 --force
kubectl create -f deployment.yaml
