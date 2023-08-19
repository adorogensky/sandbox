``podman pull docker.io/mysql:latest``
``podman network create #podman1``
``# run server``
``podman run --name mysql-box -e MYSQL_ROOT_PASSWORD=test -d --network podman1 docker.io/mysql:latest``
``# check if server started successfully``
``podman container logs --follow mysql-box``
``# run client``
``podman run -it --rm --network podman1 docker.io/mysql:latest mysql -h mysql-box -uroot -p``
