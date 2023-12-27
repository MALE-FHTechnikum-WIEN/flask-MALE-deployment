#!/bin/sh

SHARED_DIR=/home/flask_user/flask-app
HOST_DIR=$(pwd)/flask-app

echo -e "\e[32mMounting fodler:
    $HOST_DIR    to
    $SHARED_DIR\e[0m"

docker run \
    -it --rm \
	-p 5000:5000 \
    --volume=$HOST_DIR:$SHARED_DIR:rw \
    --name "1.0" \
    flask-male-deployment:latest bash
