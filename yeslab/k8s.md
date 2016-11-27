##### kubernetes 原理解析

##### Q&A

**架构**

1. 访问的权限控制是谁做的？
2. 有几个 pod 正在运行，是 API Server 主动去获取的吗？
3. etcd 里面具体都存储了哪些信息?

**工作流程**

1. etcd 是不是公用的？除了 k8s，如果有别的组件还要用 etcd，可以公用吗？
2. 怎么知道一个 pod 有没有别调度？
3. 如果资源有限，调度不起来，怎么办？
4. 资源超限，谁来杀死 pod？
5. 为什么不通过重启 pod，来解决资源超限的问题？

**架构总结**

1. list-watch 的 TCP 长连接是哪边主动发起来的？
2. 除了 kubectl 命令，还有别的形式给出命令吗？HTTP API（GET/POST）?
3. 这两种形式本质上是一样的吗？
4. 我能通过网络抓包的形式，抓到这些命令吗？

**API Server list-watch**

1. 我直接向 etcd 里面写个数据，API Server 能知道吗？
2. watch 周期是多少？
3. etcd 本身是支持 watch 的？
4. 实际部署的时候，这些组件是以什么形式部署的？进程？容器？
5. 我要把一个新的 node 拉进一个集群，具体怎么部署？手动的安装？还是主动推送的形式？
6. API Server 既然是最新的数据，那么 etcd 为什么要主动向 API Server 推送信息？
7. 既然组件都可以放到容器里，本身 maser 节点的高可用是怎么做的？
8. 如果 kubelet 本身死掉了，那就没办法了？
9. 如果 etcd 通信有问题，那么 API Server 是不是不会响应请求了？
10. etcd 和 API Server 一般都是怎么部署的？放在一台机器上？还是多个机器上？

**网络模型**

1. 一台宿主机可否有多个 subnet？
2. kube-proxy 虚拟 IP 的每个端口，都会被映射到宿主机上？
3. iptables 是动态的吗？怎么实现负载均衡的？
4. 什么时候更新这个 iptables？
5. 怎么实现之前的访问，还继续导流到相同的 endpoint？
6. k8s 有关于 iptables 的校正机制吗？

**DNS**

1. DNS 的域名是 service 的什么？域名是怎么表示的？
2. 这里的数据为啥没存在 etcd 里面？
3. 集群内部的 DNS 服务怎么指定 DNS 服务器？

**Ingress**

1. 用了这个，是不是就不用 iptables?
2. 是不是每个 node 都要起一个？

记录于 "才云科技-Yeslab" 培训课程，2016年11月27号，北京中关村