### E2E on local cluster

Testing against local clusters

**launch local cluster**

```shell
$ hack/local-up-cluster.sh
```

**build e2e test**

```shell
$ go run hack/e2e.go -- -v --build
```

**start e2e test**

In order to run an E2E test against a locally running cluster, point the tests at a custom host directly(in this case, we run `Feature:GPUDevicePlugin` e2e test only):

```shell
$ export KUBECONFIG=/var/run/kubernetes/admin.kubeconfig
$ export KUBE_MASTER_IP="127.0.0.1:6443"
$ export KUBE_MASTER=local
$ go run hack/e2e.go -- --provider=local -v --test --test_args="--ginkgo.focus=\[Feature:GPUDevicePlugin\]"
```