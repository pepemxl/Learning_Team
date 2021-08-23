FROM cpp_poco/cuda_base:latest

# Install POCO dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git openssl libssl-dev
# clonnig POCO
RUN git clone -b master https://github.com/pocoproject/poco.git
# Using CMake
#RUN mkdir cmake-build
#RUN cd cmake-build
#RUN cmake ..
#RUN cmake --build . --config Release
#RUN cmake --build . --target install
# Using Make
WORKDIR /poco
RUN ./configure
#RUN make CDBG=-w -s -j4
#RUN make install
