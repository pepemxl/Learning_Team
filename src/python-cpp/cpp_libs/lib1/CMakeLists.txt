cmake_minimum_required(VERSION 3.10)
project(MathOperations)

set(CMAKE_CXX_STANDARD 17)

add_library(math_operations SHARED math_operations.cpp)

set_target_properties(math_operations PROPERTIES PREFIX "" SUFFIX ".so")