#!/bin/bash

exec 2>/dev/null

source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n superset python=3.11 -y
conda activate superset

function install_superset() {
    mkdir -p /home/user/projects && cd /home/user/projects
    git clone https://github.com/apache/superset.git
    cd superset
    # disable CSRF protection, secure cookie, and Talisman, to support easier evaluation
    touch docker/pythonpath_dev/superset_config_docker.py
    cat >> docker/pythonpath_dev/superset_config_docker.py <<EOF
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
WTF_CSRF_ENABLED = False
TALISMAN_ENABLED = False
EOF
    # fix the version of the pre-downloaded docker images
    TAG=3.1.1
    REDIS_VERSION=7
    POSTGRES_VERSION=16-alpine
    echo "TAG=3.1.1" >> .env
    sed -i "s/image: redis:.*$/image: redis:${REDIS_VERSION}/" docker-compose-image-tag.yml
    sed -i "s/image: postgres:.*$/image: postgres:${POSTGRES_VERSION}/" docker-compose-image-tag.yml
    declare -a image_list=(
        "redis:${REDIS_VERSION}"
        "postgres:${POSTGRES_VERSION}"
        "apachesuperset.docker.scarf.sh/apache/superset:${TAG}"
    )
    images=$(docker images | awk 'NR > 1 {if ($2 == "latest") print $1; else print $1 ":" $2}')
    for img in ${image_list[@]}; do
        echo ${images} | grep -Fiq -- "$img"
        if [ $? -ne 0 ]; then
            docker pull ${img}
        fi
    done
}
install_superset
