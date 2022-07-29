#!/bin/bash

#deploy nginx
kubectl apply -f ../nginx/deployment.yaml
sleep 60s

# deploy the vertical pod autoscaler
kubectl apply -f deployment.yaml
sleep 30s

kubectl port-forward svc/nginx 5000:80

#periodically generate vpa reports
python3 parser.py >> outputvpa-26jul.txt
sleep 30

#cleanup
kubectl delete vpa vpa 
kubectl delete deployment nginx



