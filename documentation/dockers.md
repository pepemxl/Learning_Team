# Dockers

## What is a Docker image?

**Images** are **read-only templates** containing instructions for creating a **container**. A Docker image creates containers to run on the Docker platform.

Think of an **image** like a **blueprint** or **snapshot** of what will be in a container when it runs.

- An **image** is composed of **multiple stacked layers**. 
- Images contain the code or binary, runtimes, dependencies, and other filesystem objects to run an application. 
- The image relies on the host operating system (OS) kernel.
- When a Docker user runs an image, it becomes one or multiple container instances.
- **Docker images are immutable**, so you cannot change them once they are created. If you need to change something, create another container with your changes, then save those as another image. Or, just run your new container using an existing image as a base and change that one.
- Images themselves **do not run**, but you can create and run containers from a Docker image.

## What is a container?

- A **container** is an **isolated place where an application runs** without affecting the rest of the system and without the system impacting the application.
- A container runs natively on Linux and shares the host machine’s kernel, it is lightweight, not using more memory than other executables.
- If you stop a container, it will not automatically restart unless you configure it that way. 
- Containers can be much more efficient than virtual machines.
- They share a single kernel with other containers and boot in seconds instead of minutes.
- Containers can package an application with all the components it needs, then ship it all out as one unit. 
- Containers can run on any infrastructure and in any cloud.

## Lifecycle of Containers

- Lifecycle of applications
- Lifecycle of data

When you deploy a new version of your app or apply a new operation systerm patch,
we DON'T connect to the container and run an update.

- We build a new container image with the latest software
- Kill the existing container and replace it with a new one.

Here the questionn is: what shoul be done with tha data written by my application inside of 
the container, when the container is replaced?

## How Docker builds the container filesystem

## How to run stateful apps

## How to build optimized Docker images

## How storage works across a range of setups
