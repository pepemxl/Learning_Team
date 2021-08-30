FROM cpp_poco/cuda_base:latest

# Install POCO dependencies, 
# - iODBC library and header files.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git openssl libssl-dev \
    && apt-get -y install --no-install-recommends libiodbc2 libiodbc2-dev \
    && apt-get -y install --no-install-recommends libpq-dev
# clonnig POCO
RUN git clone -b master https://github.com/pocoproject/poco.git
# Using CMake to build project
WORKDIR /poco
RUN mkdir cmake-build
#RUN cd cmake-build
WORKDIR /poco/cmake-build
RUN cmake ..
RUN cmake --build . --config Release
RUN cmake --build . --target install
# Using Make
##WORKDIR /poco
##RUN ./configure
##RUN make CXXFLAGS+='-Wno-unused-but-set-variable -Wno-unused-parameter -Wno-unused-variable'
#CMD CXXFLAGS += -Wno-unused-but-set-variable -Wno-unused-parameter -Wno-unused-variable
#run make

# -Wno-unused-variable
# -Wno-unused-but-set-variable -Wno-unused-parameter -Wno-unused-variable

#RUN make CDBG=-w -s -j4
#RUN make install
