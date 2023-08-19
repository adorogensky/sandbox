```
# pull image (use 1st time only)
podman pull docker.io/mysql:latest
# create network (defaults to podman1 -- use 1st time only)
podman network create #podman1 (1st time only)
# run server
./mysql-start.sh
# check if server started successfully
podman container logs --follow mysql-box
# run client
./mysql.sh

todo:
  refactor mysql.sh to
   - pull image if it wasnt pulled -- error if image cant be pulled
   - check if network podman1 exists -- if not create it
   - run mysql server and query healthy container status until it becomes healthy.. or timeout
   - run mysql client
  populate estore_data.sql ddl -- catalog items, item location, orders, cart, payments
  import ecorp_data.sql
  as part as server creation

 
wait for container to become healthy
  
