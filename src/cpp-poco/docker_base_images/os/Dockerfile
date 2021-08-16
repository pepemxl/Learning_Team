FROM ubuntu:20.04

# Install basic utilities
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends sudo iproute2 gnupg2 ca-certificates apt-transport-https wget htop vim-tiny nano git \
    && apt-get autoremove -y && apt-get clean -y

# Install C++ toolchain
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends gcc g++ make autoconf automake libtool gdb \
    && apt-get autoremove -y && apt-get clean -y