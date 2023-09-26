sudo docker build -t sshserver ./server
docker rmi `docker images --filter dangling=true -q`
sudo docker run --rm -it -p 22:22 sshserver