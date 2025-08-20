Login to OpenShift:
oc login --token=YOUR_TOKEN

Verify login:
oc whoami

Build and push image:
docker build -t danielgevafisher/mongo-crud:latest .
docker push danielgevafisher/mongo-crud:latest

MongoDB:
oc apply -f infrastructure/k8s/mongo-deployment.yaml
oc apply -f infrastructure/k8s/mongo-service.yaml

FastAPI:
oc apply -f infrastructure/k8s/fastapi-deployment.yaml
oc apply -f infrastructure/k8s/fastapi-service.yaml
oc apply -f infrastructure/k8s/fastapi-route.yaml

Verify:
oc get all po
oc get all svc
oc get all deploy