// Generated by gencpp from file opc_ros/SetTarget.msg
// DO NOT EDIT!


#ifndef OPC_ROS_MESSAGE_SETTARGET_H
#define OPC_ROS_MESSAGE_SETTARGET_H

#include <ros/service_traits.h>


#include <opc_ros/SetTargetRequest.h>
#include <opc_ros/SetTargetResponse.h>


namespace opc_ros
{

struct SetTarget
{

typedef SetTargetRequest Request;
typedef SetTargetResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetTarget
} // namespace opc_ros


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::opc_ros::SetTarget > {
  static const char* value()
  {
    return "d59dc51bea53a4877185283f71dbf83c";
  }

  static const char* value(const ::opc_ros::SetTarget&) { return value(); }
};

template<>
struct DataType< ::opc_ros::SetTarget > {
  static const char* value()
  {
    return "opc_ros/SetTarget";
  }

  static const char* value(const ::opc_ros::SetTarget&) { return value(); }
};


// service_traits::MD5Sum< ::opc_ros::SetTargetRequest> should match
// service_traits::MD5Sum< ::opc_ros::SetTarget >
template<>
struct MD5Sum< ::opc_ros::SetTargetRequest>
{
  static const char* value()
  {
    return MD5Sum< ::opc_ros::SetTarget >::value();
  }
  static const char* value(const ::opc_ros::SetTargetRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::opc_ros::SetTargetRequest> should match
// service_traits::DataType< ::opc_ros::SetTarget >
template<>
struct DataType< ::opc_ros::SetTargetRequest>
{
  static const char* value()
  {
    return DataType< ::opc_ros::SetTarget >::value();
  }
  static const char* value(const ::opc_ros::SetTargetRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::opc_ros::SetTargetResponse> should match
// service_traits::MD5Sum< ::opc_ros::SetTarget >
template<>
struct MD5Sum< ::opc_ros::SetTargetResponse>
{
  static const char* value()
  {
    return MD5Sum< ::opc_ros::SetTarget >::value();
  }
  static const char* value(const ::opc_ros::SetTargetResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::opc_ros::SetTargetResponse> should match
// service_traits::DataType< ::opc_ros::SetTarget >
template<>
struct DataType< ::opc_ros::SetTargetResponse>
{
  static const char* value()
  {
    return DataType< ::opc_ros::SetTarget >::value();
  }
  static const char* value(const ::opc_ros::SetTargetResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // OPC_ROS_MESSAGE_SETTARGET_H
