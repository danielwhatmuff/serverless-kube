# Template for deploying an app to nuclio
[Nuclio](https://github.com/nuclio/nuclio)

## Pre-reqs
* Kube cluster with nuclio installed
* kubectl and [nuctl](https://github.com/nuclio/nuclio/releases) installed
* Prepared private docker registry with configured credentials secret. Nuclio need to push docker images into a repository. [see this](https://github.com/nuclio/nuclio/blob/master/docs/setup/k8s/getting-started-k8s.md#install-nuclio)

## Deploy to Nuclio
> Note: If you are using Docker Hub, the URL here includes your username - `docker.io/<username>`.
```
nuctl deploy helloworld -n nuclio -p https://raw.githubusercontent.com/appvia/serverless-kube/master/nuclio/app.py --registry <URL>
```

## Call the function from the CLI
```
$ nuctl invoke -n nuclio helloworld
```

## Call the function using http
```
$ kubectl port-forward --namespace nuclio $(kubectl get pod --namespace nuclio --selector="nuclio.io/app=functionres,nuclio.io/class=function,nuclio.io/function-name=helloworld,nuclio.io/function-version=latest,nuclio.io/project-name=default" --output jsonpath='{.items[0].metadata.name}') 8080:8080 &

$ curl localhost:8080
```