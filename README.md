# Docker tutorial

This is a tutorial on both how to set up docker as well as how basic ML ops programs work. 

Apologies for the fact that this works primarily on Linux. This is both because I'm much more familiar with Linux than I am with Windows based systems, but also because docker generally works better on a UNIX based system than it does on a Windows based system. That being said the Windows Subsystem Linux (WSL) system works as a reasonable facsimile of Linux. However, I'm not familiar with any of the gotchas in that system. 

# Prequisites

As mentioned above, pre-reqs are given only for linux based systems

```bash
sudo yum install docker.x86_64
sudo systemctl enable docker.service
sudo systemctl start docker.service

sudo usermod -a -G docker [your-account-name]
newgrp docker
```

To build your docker image:

```bash
docker build --network=host . -t test
```

To run:

```bash
# the volume mounts a local drive. This is a runtime thing so we
# don't have to rebuild the docker container each time we want to run a new
# model

docker run --volume /home/eyang/code/ml_engine/basic_ml_model:/model -it test:latest -p 5000:5000```

Normally you don't need to use the network, but for whatever reason the docker package that comes with our EC2 instances don't have network enabled properly by default.

# Calling the Service

```bash
curl localhost:5000/predict -X POST -H 'Content-Type: application/json' -d '{"hello": "world"}'
```