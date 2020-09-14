#!/bin/sh
kubectl delete service resource-consumer
kubectl delete pods --namespace default --all
kubectl delete deployments.apps resource-consumer

kubectl create -f deployment.yaml
kubectl apply -f service.yaml