#!/bin/sh
kubectl delete deployment docker-snort --namespace default
kubectl create -f deployment.yaml
