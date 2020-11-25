#!/bin/sh
kubectl delete deployment snort --namespace default
kubectl create -f deployment.yaml
