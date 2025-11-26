cmake_minimum_required(VERSION "3.12")

project("spackexample" VERSION 0.3.0)

# Define options for dependencies
option(USE_BOOST "Use Boost libraries" ON)
option(USE_YAML "Use yaml-cpp libraries" ON)

set(SRCS "")
set(LIBS "")
set(HDRS "")

# Handle Boost
if(USE_BOOST)
  find_package(Boost 1.65.1 REQUIRED filesystem)
  list(APPEND SRCS filesystem/filesystem.cpp flatset/flatset.cpp)
  list(APPEND HDRS filesystem/filesystem.hpp flatset/flatset.hpp)
  list(APPEND LIBS Boost::filesystem)
  add_compile_definitions(USE_BOOST)
endif()

# Handle yaml-cpp
if(USE_YAML)
  find_package(yaml-cpp 0.7.0 REQUIRED)
  list(APPEND SRCS yamlParser/yamlParser.cpp)
  list(APPEND HDRS yamlParser/yamlParser.hpp)
  list(APPEND LIBS yaml-cpp)
  add_compile_definitions(USE_YAML)
endif()

# Create the executable
add_executable(spackexample main.cpp)

# Only create the library if we have sources (dependencies are enabled)
if(SRCS)
  add_library(spackexamplelib ${SRCS})
  target_link_libraries(spackexamplelib ${LIBS})
  
  # Include directories
  target_include_directories(spackexamplelib
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/spackexamplelib
    PUBLIC
      $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/spackexamplelib>
      $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}/spackexamplelib>
  )
  
  # Link the executable to the library
  target_link_libraries(spackexample spackexamplelib)
  
  # Installation instructions for the library
  include(GNUInstallDirs)
  install(TARGETS spackexamplelib
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
  )
endif()

# Installation instructions for the executable
include(GNUInstallDirs)
install(TARGETS spackexample RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})