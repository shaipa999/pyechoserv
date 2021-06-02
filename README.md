# pyechoservshay1


Build Image:
```
cd build
docker build -t pyechoservshay .
```

return to the previous folder
```
cd ..
```

Run the webServer
```
cd yamls
kubectl apply -f ./Deployment.yaml
kubectl apply -f ./Service.yaml
kubectl apply -f ./Ingress.yaml
```
