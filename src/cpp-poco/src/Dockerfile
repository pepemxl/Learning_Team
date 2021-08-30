FROM cpp_poco/poco_base:latest

RUN mkdir -p /app
RUN mkdir -p /app/build
ADD src/main.cpp /app
ADD src/CMakeLists.txt /app
WORKDIR /app/build

RUN cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release
RUN cmake --build .