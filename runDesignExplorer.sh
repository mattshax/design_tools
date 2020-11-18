#!/bin/bash
PORT=$1
docker run -d --rm --name designExplorer -p $PORT:80 -v $PWD:/scratch -v $PWD/utils/nginx.conf:/etc/nginx/nginx.conf nginx