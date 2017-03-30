#### Changing `locale` settings permanently

```
$ cat /etc/default/locale
LANG="en_US.UTF-8"
LC_ALL="en_US.UTF-8"
LC_CTYPE="en_US.UTF-8"

$ sudo locale-gen
```
