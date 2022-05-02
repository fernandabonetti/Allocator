#!/bin/sh
kubectl delete deployment haproxy-ingress --namespace haproxy-controller --grace-period=0 --force
kubectl create -f deployment.yaml