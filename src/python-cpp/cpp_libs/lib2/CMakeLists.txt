cmake_minimum_required(VERSION 3.10)
project(StringOperations)

set(CMAKE_CXX_STANDARD 17)

add_library(string_operations SHARED string_operations.cpp)

set_target_properties(string_operations PROPERTIES PREFIX "" SUFFIX ".so")