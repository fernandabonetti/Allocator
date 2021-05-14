#!/bin/sh
kubectl delete service resource-consumer
kubectl delete deployment resource-consumer --namespace default

kubectl create -f deployment.yaml
kubectl apply -f service.yaml