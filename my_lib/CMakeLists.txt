cmake_minimum_required(VERSION 2.6)
project(my_lib)

include_directories(algebra/)

add_executable(my_lib.out main.cpp algebra/matrika.cpp)

#install(TARGETS my_lib RUNTIME DESTINATION bin)
