``podman pull docker.io/mysql:latest``
``podman network create #podman1 (1st time only)`` 
``# run server``
``./mysql-start.sh``
``# check if server started successfully``
``podman container logs --follow mysql-box``
``# run client``
``./mysql.sh``

todo:
  wait for container to become healthy
  populate ecorp_data.sql ddl
  import ecorp_data.sql
  as part as server creation
