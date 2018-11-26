# Events

Events - Group 3
Built with
Python and mysql in docker
Only thing needed to download is docker:
https://www.docker.com/

Setting up Dev

git clone https://github.com/DAT210/Events.git

In cmd/terminal: cd into repository location
Run: "docker-compose up --build"
If you are using docker toolbox, the container should now be visible at

http://192.168.99.100:4000/

And if you are running "normal" docker, it should be visible at:
http://127.0.0.1:4000/

mySQL port:3306

Command to bash into the mysql server:
docker exec -it mysql /bin/bash