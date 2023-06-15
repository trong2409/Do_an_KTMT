# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "opc_ros: 12 messages, 4 services")

set(MSG_I_FLAGS "-Iopc_ros:/home/kuzu/opc_ros_ws/src/opc_ros/msg;-Iopc_ros:/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/melodic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(opc_ros_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/Mecanum.msg" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/src/opc_ros/msg/Mecanum.msg" ""
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg" "actionlib_msgs/GoalID:opc_ros/ActionSetRawGoal:opc_ros/ActionSetRawActionFeedback:opc_ros/ActionSetRawActionResult:actionlib_msgs/GoalStatus:opc_ros/ActionSetRawActionGoal:opc_ros/ActionSetRawResult:std_msgs/Header:opc_ros/ActionSetRawFeedback"
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg" ""
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg" ""
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetServo.msg" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetServo.msg" ""
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv" ""
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv" ""
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg" ""
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/JetMax.msg" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/src/opc_ros/msg/JetMax.msg" ""
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJoint.msg" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJoint.msg" ""
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg" "actionlib_msgs/GoalID:opc_ros/ActionSetRawFeedback:actionlib_msgs/GoalStatus:std_msgs/Header"
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg" ""
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget.srv" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget.srv" ""
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg" "opc_ros/ActionSetRawResult:actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:std_msgs/Header"
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv" ""
)

get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg" NAME_WE)
add_custom_target(_opc_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "opc_ros" "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg" "actionlib_msgs/GoalID:opc_ros/ActionSetRawGoal:std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/Mecanum.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_msg_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_msg_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_msg_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_msg_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetServo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_msg_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_msg_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/JetMax.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_msg_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJoint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_msg_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_msg_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_msg_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_msg_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)

### Generating Services
_generate_srv_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_srv_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_srv_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)
_generate_srv_cpp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
)

### Generating Module File
_generate_module_cpp(opc_ros
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(opc_ros_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(opc_ros_generate_messages opc_ros_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/Mecanum.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetServo.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/JetMax.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJoint.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_cpp _opc_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(opc_ros_gencpp)
add_dependencies(opc_ros_gencpp opc_ros_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS opc_ros_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/Mecanum.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_msg_eus(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_msg_eus(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_msg_eus(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_msg_eus(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetServo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_msg_eus(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_msg_eus(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/JetMax.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_msg_eus(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJoint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_msg_eus(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_msg_eus(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_msg_eus(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_msg_eus(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)

### Generating Services
_generate_srv_eus(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_srv_eus(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_srv_eus(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)
_generate_srv_eus(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
)

### Generating Module File
_generate_module_eus(opc_ros
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(opc_ros_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(opc_ros_generate_messages opc_ros_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/Mecanum.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetServo.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/JetMax.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJoint.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_eus _opc_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(opc_ros_geneus)
add_dependencies(opc_ros_geneus opc_ros_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS opc_ros_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/Mecanum.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_msg_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_msg_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_msg_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_msg_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetServo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_msg_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_msg_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/JetMax.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_msg_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJoint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_msg_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_msg_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_msg_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_msg_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)

### Generating Services
_generate_srv_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_srv_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_srv_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)
_generate_srv_lisp(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
)

### Generating Module File
_generate_module_lisp(opc_ros
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(opc_ros_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(opc_ros_generate_messages opc_ros_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/Mecanum.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetServo.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/JetMax.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJoint.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_lisp _opc_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(opc_ros_genlisp)
add_dependencies(opc_ros_genlisp opc_ros_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS opc_ros_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/Mecanum.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_msg_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_msg_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_msg_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_msg_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetServo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_msg_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_msg_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/JetMax.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_msg_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJoint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_msg_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_msg_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_msg_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_msg_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)

### Generating Services
_generate_srv_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_srv_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_srv_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)
_generate_srv_nodejs(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
)

### Generating Module File
_generate_module_nodejs(opc_ros
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(opc_ros_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(opc_ros_generate_messages opc_ros_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/Mecanum.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetServo.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/JetMax.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJoint.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_nodejs _opc_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(opc_ros_gennodejs)
add_dependencies(opc_ros_gennodejs opc_ros_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS opc_ros_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/Mecanum.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_msg_py(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_msg_py(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_msg_py(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_msg_py(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetServo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_msg_py(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_msg_py(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/JetMax.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_msg_py(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJoint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_msg_py(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_msg_py(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_msg_py(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_msg_py(opc_ros
  "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)

### Generating Services
_generate_srv_py(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_srv_py(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_srv_py(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)
_generate_srv_py(opc_ros
  "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
)

### Generating Module File
_generate_module_py(opc_ros
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(opc_ros_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(opc_ros_generate_messages opc_ros_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/Mecanum.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawAction.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawResult.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJetMax.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetServo.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetFileOp.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget_object.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawGoal.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/JetMax.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/msg/SetJoint.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionFeedback.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawFeedback.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/SetTarget.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionResult.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/src/opc_ros/srv/ActionSetList.srv" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/kuzu/opc_ros_ws/devel/share/opc_ros/msg/ActionSetRawActionGoal.msg" NAME_WE)
add_dependencies(opc_ros_generate_messages_py _opc_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(opc_ros_genpy)
add_dependencies(opc_ros_genpy opc_ros_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS opc_ros_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/opc_ros
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(opc_ros_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(opc_ros_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/opc_ros
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(opc_ros_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(opc_ros_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/opc_ros
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(opc_ros_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(opc_ros_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/opc_ros
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(opc_ros_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(opc_ros_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2.7\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/opc_ros
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(opc_ros_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(opc_ros_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
