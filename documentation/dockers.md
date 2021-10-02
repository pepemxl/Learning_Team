# Dockers


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
