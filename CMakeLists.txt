cmake_minimum_required(VERSION 3.9.1)
project(setup)
set(CMAKE_CXX_STANDARD 11)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall -Wextra -Werror")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g -O0")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")

# set the include path
include_directories(include)

# get all cpp files in src
file(GLOB_RECURSE sources src/*.cpp)
set(sources ${sources} src/main.cpp)
add_executable(setup ${sources})
