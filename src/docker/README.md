# Docker

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications.

**Docker keeps things organized** by isolating everything with containers and images.

Some of the classic componente are:

- **Base images** are images that have no parent image, usually images with an OS like ubuntu or debian.
- **Images** - The blueprints of our application which form the basis of containers. In the demo above, we used the docker pull command to download the busybox image.
- **Containers** - Created from Docker images and run the actual application. We create a container using docker run which we did using the busybox image that we downloaded. A list of running containers can be seen using the docker ps command.
- **Docker Daemon** - The background service running on the host that manages building, running and distributing Docker containers. The daemon is the process that runs in the operating system which clients talk to.
- **Docker Client** - The command line tool that allows the user to interact with the daemon. More generally, there can be other forms of clients too - such as Kitematic which provide a GUI to the users.
- **Docker Hub** - A registry of Docker images can in the machine, local, or remote in cloud environment. You can think of the registry as a directory of all available Docker images, usually associated with an artifactory. During development is usual to host their own Docker registries and can use them for pulling images.

## Isolated Resources

The containers that Docker builds are isolated with respect to eight aspects:
1. PID namespace—Process identifiers and capabilities
2. UTS namespace—Host and domain name
3. MNT namespace—File system access and structure
4. IPC namespace—Process communication over shared memory
5. NET namespace—Network access and structure
6. USR namespace—User names and identifiers
7. chroot()—Controls the location of the file system root
8. cgroups—Resource protection

## Usual commands and examples

Given a [Dockerfile](example_01/flask-app/Dockerfile) and an [application](example_01/flask-app/app.py) we can test the next common commands in docker:

- `docker build -t docker:example_01` [example](example_01/docker_build.bat)
    - `--tag , -t 		Name and optionally a tag in the 'name:tag' format`
- `docker ps` to list containers running
- `docker images` to list images locally available.
- `docker pull <image_name>` to retrieve remote images.
- `docker start <container_name>` start container.
- `docker stop <container_name>` stop container.
- `--rm` option tells Docker to remove the intermediate images.


## Base Image Container Creation

The first step in building a container is actually creating the container image.

To build an image, we need to run the docker build command, and tell it which base image to use and which additional packages to install. This is done by creating a Dockerfile. 

```docker
FROM ubuntu
RUN apt-get update && apt-get install gcc git -y
```

The corresponding image can be created with

```bash
docker build .
```
The `.` tells Docker to look for the Dockerfile in the current working directory.

This command will create a new container based on the latest stable image of Ubuntu and install git and gcc within that container `-y` automatically replies yes to any confirmation messages displayed by `apt-get`. 

## Data

By default all files created inside a container are stored on a writable container layer. 

This means that:

- The **data doesn’t persist when that container no longer exists**, and it can be difficult to get the data out of the container if another process needs it.
- A container’s **writable layer is tightly coupled to the host machine** where the container is running. You can’t easily move the data somewhere else.
Writing into a **container’s writable layer requires a storage driver to manage the filesystem**. The storage driver provides a union filesystem, using the Linux kernel. This extra abstraction reduces performance as compared to using data volumes, which write directly to the host filesystem.

- Docker has two options for containers to store files on the host machine, so that the files are persisted even after the container stops: 
    
    1. volumes, and 
    2. bind mounts.

- Docker also supports containers storing files in-memory on the host machine. 

    - If you’re running Docker on Linux, tmpfs mount is used to store files in the host’s system memory. 
    - If you’re running Docker on Windows, named pipe is used to store files in the host’s system memory.

### Volumes

Docker containers are used to run applications in an isolated environment. All the changes inside the container are lost when the container stops. If we want to keep data between runs, Docker volumes and bind mounts can help. 

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
