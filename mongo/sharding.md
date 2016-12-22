## Deploy a sharded MongoDB cluster

###config


**Ports:**

    mongos: 	27017
    primary: 	27027
    backup: 	27037
    arbiter: 	27047
    cfg: 		27057

**Replica Sets:**

    rs0: host1:27027, host5:27037, host6:27047
    rs1: host2:27027, host7:27037, host8:27047
    rs2: host3:27027, host6:27037, host7:27047
    rs3: host4:27027, host8:27037, host5:27047


**Hosts:**

| Hosts | Mongo | | Hosts | Mongo |
| --- | --- | --- | --- | --- |
| 1 | `mongos`:27017 <br> <br> rs0.primary:27027 <br> | | 5 | `mongos`:27017 <br> <br> rs0.back:27037 <br> <br> rs3.arbiter:27047 <br> <br> |
| 2 | `mongos`:27017 <br> <br> rs1.primary:27027 <br> | | 6 | `mongos`:27017 <br> <br> rs2.back:27037 <br> <br> rs0.arbiter:27047 <br> <br> |
| 3 | `mongos`:27017 <br> <br> rs2.primary:27027 <br> | | 7 | `mongos`:27017 <br> <br> rs1.back:27037 <br> <br> rs2.arbiter:27047 <br> <br> |
| 4 | `mongos`:27017 <br> <br> rs3.primary:27027 <br> | | 8 | `mongos`:27017 <br> <br> rs3.back:27037 <br> <br> rs1.arbiter:27047 <br> <br> |

###setup

[deploy-replica-set-with-auth](http://docs.mongodb.org/manual/tutorial/deploy-replica-set-with-auth/)

```
    > use admin
    > db.auth ("{rootname}", "{password}")

    > sh.addShard ("rs0/host1:27027,host5:27037,host6:27047")
    > sh.addShard ("rs1/host2:27027,host7:27037,host8:27047")
    > sh.addShard ("rs2/host3:27027,host6:27037,host7:27047")
    > sh.addShard ("rs3/host4:27027,host8:27037,host5:27047")
    > sh.enableSharding ("{dbname}")
    > sh.setBalancerState (true)
    > sh.startBalancer ()
```

###check status

```
    > sh.status ()
	  sharding version: {
	    "_id" : 1,
	    "minCompatibleVersion" : 5,
	    "currentVersion" : 6,
	    "clusterId" : ObjectId("555c9353b21a50716080287d")
	}
	  shards:
	    {  "_id" : "rs0",  "host" : "rs0/host1:27027,host5:27037" }
	    {  "_id" : "rs1",  "host" : "rs1/host2:27027,host7:27027" }
	    {  "_id" : "rs2",  "host" : "rs2/host3:27027,host6:27037" }
	    {  "_id" : "rs3",  "host" : "rs3/host4:27027,zeus8:27037" }
```

###monitor

**mongotop:**

```
    $ mongotop --port {port} -u {rootname} -p {password} --authenticationDatabase admin
    $ mongostat --port {port} -u {rootname} -p {password} --authenticationDatabase admin
```

**profiler:**

[manage-the-database-profiler](https://docs.mongodb.org/v3.0/tutorial/manage-the-database-profiler/)

```
	> db.setProfilingLevel (1, 700)
	> db.system.profile.find ({millis: {$gte: 700}}).limit (10).sort ({ts : -1}).pretty ()
```
