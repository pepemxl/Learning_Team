# Use an official Python runtime as a parent image
FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    cmake \
    g++ \
    build-essential \
    sudo \
    && rm -rf /var/lib/apt/lists/*


# Create a non-root user and switch to it
RUN groupadd -g 1000 appuser && \
    useradd -r -u 1000 -g appuser appuser && \
    mkdir -p /app && \
    mkdir -p /home/appuser && \
    chown appuser:appuser /app && \
    chown appuser:appuser /home/appuser

# Set the working directory
WORKDIR /app

# Copy the entire project (preserving file permissions)
COPY --chown=appuser:appuser . .

# RUN mkdir -p /app/cpp_libs/lib1/build && \
#     mkdir -p /app/cpp_libs/lib2/build && \
#     chmod -R 755 /app/cpp_libs/lib1/build && \
#     chmod -R 755 /app/cpp_libs/lib2/build


# Build C++ libraries as non-root user
#USER appuser
#RUN mkdir -p /app/cpp_libs/lib1/build && \
#    mkdir -p /app/cpp_libs/lib2/build && \
#    cd /app/cpp_libs/lib1/build && \
#    cmake .. && \
#    make && \
#    cd /app/cpp_libs/lib2/build && \
#    cmake .. && \
#    make

# Build C++ libraries as non-root user
USER appuser
RUN mkdir -p /app/cpp_libs/lib1/build && \
    mkdir -p /app/cpp_libs/lib2/build && \
    cd /app/cpp_libs/lib1/build && \
    cmake .. && \
    make && \
    cd /app/cpp_libs/lib2/build && \
    cmake .. && \
    # make && \
    make
    # Copiar las librerías a un directorio estándar
    #cp /app/cpp_libs/lib1/build/math_operations.so /usr/local/lib/
    #sudo cp /app/cpp_libs/lib1/build/math_operations.so /usr/local/lib/
    #sudo cp /app/cpp_libs/lib1/build/libmath_operations.so /usr/local/lib/ && \
    #cp /app/cpp_libs/lib1/build/libmath_operations.so /usr/local/lib/ && \
    #sudo cp /app/cpp_libs/lib2/build/libstring_operations.so /usr/local/lib/ && \
    #cp /app/cpp_libs/lib2/build/libstring_operations.so /usr/local/lib/ && \
    # Actualizar el cache de librerías
    #sudo ldconfig
    #ldconfig

# RUN ls -la /app/cpp_libs

# Install Python dependencies
RUN pip3 install --user -r /app/python_app/requirements.txt

# Set environment variables
ENV PATH="/home/appuser/.local/bin:${PATH}"
ENV LD_LIBRARY_PATH="/app/cpp_libs/lib1/build:/app/cpp_libs/lib2/build:${LD_LIBRARY_PATH}"

# Set the command to run the Python script
CMD ["python3", "/app/python_app/main.py"]