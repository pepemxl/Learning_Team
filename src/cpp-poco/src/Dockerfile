FROM cpp_poco/poco_base:latest

RUN mkdir -p /app
RUN mkdir -p /app/build
ADD src/main.cpp /app
ADD src/samples /app/samples
ADD src/CMakeLists.txt /app
WORKDIR /app/build

RUN cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release
RUN cmake --build .
ENTRYPOINT ["/app/bin/Poco_example"]