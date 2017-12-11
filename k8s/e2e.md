### E2E on local cluster

Testing against local clusters

**launch local cluster**

```shell
$ hack/local-up-cluster.sh
```

If you want enable `DevicePlugin` (with log level = 2):

```shell
$ export KUBERNETES_PROVIDER=local
$ export API_HOST=`ifconfig docker0 | grep "inet addr" | awk -F'[: ]+' '{ print $4 }'`
$ FEATURE_GATES=DevicePlugins=true ALLOW_PRIVILEGED=true LOG_LEVEL=2 hack/local-up-cluster.sh
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

go run hack/e2e.go -- --provider=local -v --test --test_args="--ginkgo.focus=\[Feature:DevicePlugin\]"

### build e2e test only (linux platform)

```shell
$ make all WHAT=test/e2e/e2e.test KUBE_BUILD_PLATFORMS=linux/amd64
```


### device plugin for e2e test

```shell
$ make test-e2e-node FOCUS="\[Feature:DevicePlugin\]" PARALLELISM=1 TEST_ARGS='--ginkgo.skip= --feature-gates=DynamicKubeletConfig=true'
```

```shell
kubernetes/test/images# make all-push WHAT=stub-device-plugin

docker run -v /var/lib/kubelet/device-plugins:/var/lib/kubelet/device-plugins -v /tmp/dummy-device:/tmp/dummy-device cargo.caicloud.io/cenph/stub-device-plugin-amd64:1.0
```

