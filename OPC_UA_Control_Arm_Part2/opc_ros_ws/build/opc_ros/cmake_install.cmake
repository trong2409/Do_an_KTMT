# Install script for directory: /home/hiwonder/opc_ros_ws/src/opc_ros

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/hiwonder/opc_ros_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opc_ros/msg" TYPE FILE FILES
    "/home/hiwonder/opc_ros_ws/src/opc_ros/msg/Mecanum.msg"
    "/home/hiwonder/opc_ros_ws/src/opc_ros/msg/JetMax.msg"
    "/home/hiwonder/opc_ros_ws/src/opc_ros/msg/SetServo.msg"
    "/home/hiwonder/opc_ros_ws/src/opc_ros/msg/SetJoint.msg"
    "/home/hiwonder/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opc_ros/srv" TYPE FILE FILES
    "/home/hiwonder/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv"
    "/home/hiwonder/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv"
    "/home/hiwonder/opc_ros_ws/src/opc_ros/srv/SetTarget.srv"
    "/home/hiwonder/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opc_ros/action" TYPE FILE FILES "/home/hiwonder/opc_ros_ws/src/opc_ros/action/ActionSetRaw.action")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opc_ros/msg" TYPE FILE FILES
    "/home/hiwonder/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg"
    "/home/hiwonder/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg"
    "/home/hiwonder/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg"
    "/home/hiwonder/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg"
    "/home/hiwonder/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg"
    "/home/hiwonder/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg"
    "/home/hiwonder/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opc_ros/cmake" TYPE FILE FILES "/home/hiwonder/opc_ros_ws/build/opc_ros/catkin_generated/installspace/opc_ros-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/hiwonder/opc_ros_ws/devel/include/opc_ros")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/hiwonder/opc_ros_ws/devel/share/roseus/ros/opc_ros")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/hiwonder/opc_ros_ws/devel/share/common-lisp/ros/opc_ros")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/hiwonder/opc_ros_ws/devel/share/gennodejs/ros/opc_ros")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/hiwonder/opc_ros_ws/devel/lib/python2.7/dist-packages/opc_ros")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/hiwonder/opc_ros_ws/devel/lib/python2.7/dist-packages/opc_ros")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/hiwonder/opc_ros_ws/build/opc_ros/catkin_generated/installspace/opc_ros.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opc_ros/cmake" TYPE FILE FILES "/home/hiwonder/opc_ros_ws/build/opc_ros/catkin_generated/installspace/opc_ros-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opc_ros/cmake" TYPE FILE FILES
    "/home/hiwonder/opc_ros_ws/build/opc_ros/catkin_generated/installspace/opc_rosConfig.cmake"
    "/home/hiwonder/opc_ros_ws/build/opc_ros/catkin_generated/installspace/opc_rosConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opc_ros" TYPE FILE FILES "/home/hiwonder/opc_ros_ws/src/opc_ros/package.xml")
endif()

