FROM cpp_poco/ubuntu_base:latest

# Install CUDA SDK
RUN wget -nv https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin \
    && mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600 \
    && wget -nv https://developer.download.nvidia.com/compute/cuda/11.4.1/local_installers/cuda-repo-wsl-ubuntu-11-4-local_11.4.1-1_amd64.deb \
    && dpkg -i cuda-repo-wsl-ubuntu-11-4-local_11.4.1-1_amd64.deb \
    && apt-key add /var/cuda-repo-wsl-ubuntu-11-4-local/7fa2af80.pub \
    && apt-get update && export DEBIAN_FRONTEND=noninteractive  \
    && apt-get -y install cuda \
    && apt-get autoremove -y && apt-get clean -y \
    && rm -f cuda-repo-wsl-ubuntu-11-4-local_11.4.1-1_amd64.deb \
    && rm -f /etc/apt/sources.list.d/cuda-wsl-ubuntu-11-4-local.list \
    && rm -fr /var/cuda-repo-wsl-ubuntu-11-4-local