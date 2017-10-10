### kubelet start error

```shell
Failed to start cAdvisor inotify_add_watch /sys/fs/cgroup/cpu,cpuacct: no space left on device
tail: inotify resources exhausted
tail: inotify cannot be used, reverting to polling
```

maybe inotify resources exhausted: possible leak in cAdvisor

**How to fix:**

```shell
$ sudo echo 1048576 > /proc/sys/fs/inotify/max_user_watches
```

If you like to make your limit permanent, use:

```shell
$ echo fs.inotify.max_user_watches=1048576 | sudo tee -a /etc/sysctl.conf
$ sudo sysctl -p
```