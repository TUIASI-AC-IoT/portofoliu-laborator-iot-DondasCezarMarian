cmake_minimum_required(VERSION 3.16.0)
include($ENV{IDF_PATH}/tools/cmake/project.cmake)
idf_build_set_property(MINIMAL_BUILD ON)
list(APPEND EXTRA_COMPONENT_DIRS mdns)
project(Lab4_IoT)

