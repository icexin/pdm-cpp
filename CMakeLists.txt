cmake_minimum_required(VERSION 2.8.12)
project(MD5Encrypter)

add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(md5 cpp/main.cc)
target_link_libraries(md5 ${CONAN_LIBS})
install(TARGETS md5 DESTINATION ${CMAKE_INSTALL_PREFIX}/pylib/bin)