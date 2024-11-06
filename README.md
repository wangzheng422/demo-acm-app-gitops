# demo-acm-app-gitops

```bash

# for build the uplaod.server
podman build -t quay.io/wangzheng422/qimgs:uplaod.server-v1.0.1 -f upload.server/rocky.dockerfile upload.server

podman push quay.io/wangzheng422/qimgs:uplaod.server-v1.0.1

podman run --rm -p 18080:8080 quay.io/wangzheng422/qimgs:uplaod.server-v1.0.0

# Use curl to upload the file
curl -F "file=@list" http://127.0.0.1:18080/upload


```