## Sentiment Analysis API Deployment

A REST API that allow user to analyse the sentiment of a sentence.
[Original sentiment model](https://github.com/FelitaD/sentiment-analysis-notebook/blob/main/Reviews_Final.ipynb)

Users can access 2 versions of the sentence analyzer dependending on their authorization.<br>

[Full API documentation](https://documenter.getpostman.com/view/17951830/UVktpYz8)

## Tests

Basic tests using requests.

## Deployments

### Single-cluster deployment with Docker compose

2 containers :
- API
- Tests

### Multi-cluster deployment with Kubernetes
https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/

```kompose convert```

Modifier dans api-deployment.yaml ```replicas: 3```

``` kubectl apply -f api-deployment.yaml,api-service.yaml,api-network-networkpolicy.yaml,app-volume-persistentvolumeclaim.yaml,test-analyzer-1-deployment.yaml,test-analyzer-2-deployment.yaml, test-login-deployment.yaml,test-permissions-deployment.yaml,test-status-deployment.yaml**```

```minikube service api```
