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

Access the site:
We need to get the cluster Ip of the minikube
```
minikube ip
```

Then add to the hosts file:
```
<cluster_ip>       pyechoservshay-ingress.com
```

You can now Browse to the site:
```
http://pyechoservshay-ingress.com/test
```
