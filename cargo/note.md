##### Prod cargo deploy

1. edit `harbor.cfg`, change `hostname`, `db_password`, `harbor_admin_password`,

   and turn on or off the `self-registration` feature:

   ```
   self_registration = off
   ```

2. add `cert` and `key` to the following files:

    ```
    make/cargo.caicloudprivatetest.com.crt
    make/cargo.caicloudprivatetest.com.key
    ```
3. run `./prepare` to gen config files.

4. config docker registry `oss` stroge.

	```
	storage:
    cache:
        layerinfo: inmemory
    oss:
        accesskeyid: XXXXX
        accesskeysecret: XXXXX
        region: oss-cn-hangzhou
        endpoint: cargo-registry.oss-internal.aliyuncs.com
        internal: true
        bucket: cargo-registry
        rootdirectory: /
    # filesystem:
    #    rootdirectory: /storage
    maintenance:
        uploadpurging:
            enabled: false
    delete:
        enabled: true
    ```

5. edit `docker-compose.yml` to open debug options if needed.

6. use `docker-compose build` && `docker-compose up -d` to deploy.
