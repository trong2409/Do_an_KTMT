# Install script for directory: /home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/hiwonder/ros/install")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/jetmax_control/msg" TYPE FILE FILES
    "/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control/msg/Mecanum.msg"
    "/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control/msg/JetMax.msg"
    "/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control/msg/SetServo.msg"
    "/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control/msg/SetJoint.msg"
    "/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control/msg/SetJetMax.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/jetmax_control/srv" TYPE FILE FILES
    "/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control/srv/ActionSetList.srv"
    "/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control/srv/ActionSetFileOp.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/jetmax_control/action" TYPE FILE FILES "/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control/action/ActionSetRaw.action")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/jetmax_control/msg" TYPE FILE FILES
    "/home/hiwonder/ros/devel/share/jetmax_control/msg/ActionSetRawAction.msg"
    "/home/hiwonder/ros/devel/share/jetmax_control/msg/ActionSetRawActionGoal.msg"
    "/home/hiwonder/ros/devel/share/jetmax_control/msg/ActionSetRawActionResult.msg"
    "/home/hiwonder/ros/devel/share/jetmax_control/msg/ActionSetRawActionFeedback.msg"
    "/home/hiwonder/ros/devel/share/jetmax_control/msg/ActionSetRawGoal.msg"
    "/home/hiwonder/ros/devel/share/jetmax_control/msg/ActionSetRawResult.msg"
    "/home/hiwonder/ros/devel/share/jetmax_control/msg/ActionSetRawFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/jetmax_control/cmake" TYPE FILE FILES "/home/hiwonder/ros/build/jetmax_buildin_funcs/jetmax_control/catkin_generated/installspace/jetmax_control-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/hiwonder/ros/devel/include/jetmax_control")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/hiwonder/ros/devel/share/roseus/ros/jetmax_control")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/hiwonder/ros/devel/share/common-lisp/ros/jetmax_control")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/hiwonder/ros/devel/share/gennodejs/ros/jetmax_control")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/hiwonder/ros/devel/lib/python2.7/dist-packages/jetmax_control")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/hiwonder/ros/devel/lib/python2.7/dist-packages/jetmax_control")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/hiwonder/ros/build/jetmax_buildin_funcs/jetmax_control/catkin_generated/installspace/jetmax_control.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/jetmax_control/cmake" TYPE FILE FILES "/home/hiwonder/ros/build/jetmax_buildin_funcs/jetmax_control/catkin_generated/installspace/jetmax_control-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/jetmax_control/cmake" TYPE FILE FILES
    "/home/hiwonder/ros/build/jetmax_buildin_funcs/jetmax_control/catkin_generated/installspace/jetmax_controlConfig.cmake"
    "/home/hiwonder/ros/build/jetmax_buildin_funcs/jetmax_control/catkin_generated/installspace/jetmax_controlConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/jetmax_control" TYPE FILE FILES "/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control/package.xml")
endif()

