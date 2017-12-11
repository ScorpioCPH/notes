# kube-dns debug

- get kubedns logs:

```sh
$ kubectl logs -f -n kube-system $(kubectl get pods -n kube-system -l k8s-app=kube-dns -o name) -c kubedns

I1211 08:14:14.464714       1 dns.go:173] Waiting for services and endpoints to be initialized from apiserver...
I1211 08:14:14.964719       1 dns.go:173] Waiting for services and endpoints to be initialized from apiserver...
F1211 08:14:15.464680       1 dns.go:167] Timeout waiting for initialization

```
- reset iptables and restart kube-dns:

```sh
$ iptables -P INPUT ACCEPT
$ iptables -P OUTPUT ACCEPT
$ iptables -P FORWARD ACCEPT
$ iptables -F INPUT
$ iptables -F OUTPUT
$ iptables -F FORWARD
```

```sh
$ kubectl logs -f -n kube-system $(kubectl get pods -n kube-system -l k8s-app=kube-dns -o name) -c kubedns

I1211 11:10:33.472165       1 server.go:194] Starting SkyDNS server (0.0.0.0:10053)
I1211 11:10:33.472299       1 server.go:213] Skydns metrics enabled (/metrics:10055)
I1211 11:10:33.472317       1 dns.go:146] Starting endpointsController
I1211 11:10:33.472320       1 dns.go:149] Starting serviceController
I1211 11:10:33.472490       1 logs.go:41] skydns: ready for queries on cluster.local. for tcp://0.0.0.0:10053 [rcache 0]
I1211 11:10:33.472496       1 logs.go:41] skydns: ready for queries on cluster.local. for udp://0.0.0.0:10053 [rcache 0]
I1211 11:10:33.972521       1 dns.go:170] Initialized services and endpoints from apiserver
I1211 11:10:33.972558       1 server.go:128] Setting up Healthz Handler (/readiness)
I1211 11:10:33.972586       1 server.go:133] Setting up cache handler (/cache)
I1211 11:10:33.972600       1 server.go:119] Status HTTP port 8081

```
