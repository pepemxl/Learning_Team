# Docker

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications.

Some of the classic componente are:

- Base images are images that have no parent image, usually images with an OS like ubuntu or debian.
- Images - The blueprints of our application which form the basis of containers. In the demo above, we used the docker pull command to download the busybox image.
- Containers - Created from Docker images and run the actual application. We create a container using docker run which we did using the busybox image that we downloaded. A list of running containers can be seen using the docker ps command.
- Docker Daemon - The background service running on the host that manages building, running and distributing Docker containers. The daemon is the process that runs in the operating system which clients talk to.
- Docker Client - The command line tool that allows the user to interact with the daemon. More generally, there can be other forms of clients too - such as Kitematic which provide a GUI to the users.
- Docker Hub - A registry of Docker images. You can think of the registry as a directory of all available Docker images. If required, one can host their own Docker registries and can use them for pulling images.


## Usual commands

`docker build -t docker:example_01`
`--tag , -t 		Name and optionally a tag in the 'name:tag' format`

- `docker ps`
- `docker images`
- `docker pull <image_name>`

## Volumes

Docker containers are used to run applications in an isolated environment. By default, all the changes inside the container are lost when the container stops. If we want to keep data between runs, Docker volumes and bind mounts can help. 

A docker container runs the software stack defined in an image. Images are made of a set of read-only layers that work on a file system called the Union File System. When we start a new container, Docker adds a read-write layer on the top of the image layers allowing the container to run as though on a standard Linux file system.

### Managing Volumes

Docker allows us to manage volumes via the docker volume set of commands. We can give a volume an explicit name (named volumes), or allow Docker to generate a random one (anonymous volumes).

#### Creating Volumes

We can create a volume by using the create subcommand and passing a name as an argument:

```bash
docker volume create data_volume
data_volume
```


# Python SDK

```bash
pip install docker.
```
