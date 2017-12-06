

#### show all keys (etcd3)

```sh
$ ETCDCTL_API=3 etcdctl get / --prefix --keys-only

/registry/apiregistration.k8s.io/apiservices/v1.

/registry/apiregistration.k8s.io/apiservices/v1.apps

/registry/apiregistration.k8s.io/apiservices/v1.authentication.k8s.io

/registry/apiregistration.k8s.io/apiservices/v1.authorization.k8s.io

/registry/apiregistration.k8s.io/apiservices/v1.autoscaling

/registry/apiregistration.k8s.io/apiservices/v1.batch

/registry/apiregistration.k8s.io/apiservices/v1.networking.k8s.io
```

#### get key value

```
$ ETCDCTL_API=3 etcdctl --debug get /registry/apiregistration.k8s.io/apiservices/v1beta1.apiextensions.k8s.io -w fields
"ClusterID" : 14841639068965178418
"MemberID" : 10276657743932975437
"Revision" : 1960
"RaftTerm" : 2
"Key" : "/registry/apiregistration.k8s.io/apiservices/v1beta1.apiextensions.k8s.io"
"CreateRevision" : 14
"ModRevision" : 14
"Version" : 1
"Value" : "{\"kind\":\"APIService\",\"apiVersion\":\"apiregistration.k8s.io/v1beta1\",\"metadata\":{\"name\":\"v1beta1.apiextensions.k8s.io\",\"uid\":\"482de8c8-da5f-11e7-a69d-1c1b0d037779\",\"creationTimestamp\":\"2017-12-06T08:27:22Z\",\"labels\":{\"kube-aggregator.kubernetes.io/automanaged\":\"onstart\"}},\"spec\":{\"service\":null,\"group\":\"apiextensions.k8s.io\",\"version\":\"v1beta1\",\"caBundle\":null,\"groupPriorityMinimum\":16700,\"versionPriority\":9},\"status\":{\"conditions\":[{\"type\":\"Available\",\"status\":\"True\",\"lastTransitionTime\":\"2017-12-06T08:27:22Z\",\"reason\":\"Local\",\"message\":\"Local APIServices are always available\"}]}}\n"
"Lease" : 0
"More" : false
"Count" : 1

```
