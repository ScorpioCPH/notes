#### Changing `locale` settings permanently

```
$ cat /etc/default/locale
LANG="en_US.UTF-8"
LC_ALL="en_US.UTF-8"
LC_CTYPE="en_US.UTF-8"

$ sudo locale-gen
```

#### Use mac keyboard on ubuntu (change key mapping)

```shell
$ sudo vim /usr/share/X11/xkb/symbols/pc

# looks like below
#      key <LCTL> {        [ Super_L               ]       };
#      key <LWIN> {        [ Control_L             ]       };
#
#      key <RTSH> {        [ Shift_R               ]       };
#      key <RCTL> {        [ Super_R               ]       };

```
