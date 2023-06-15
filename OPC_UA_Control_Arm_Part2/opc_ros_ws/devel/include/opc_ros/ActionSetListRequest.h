// Generated by gencpp from file opc_ros/ActionSetListRequest.msg
// DO NOT EDIT!


#ifndef OPC_ROS_MESSAGE_ACTIONSETLISTREQUEST_H
#define OPC_ROS_MESSAGE_ACTIONSETLISTREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace opc_ros
{
template <class ContainerAllocator>
struct ActionSetListRequest_
{
  typedef ActionSetListRequest_<ContainerAllocator> Type;

  ActionSetListRequest_()
    {
    }
  ActionSetListRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::opc_ros::ActionSetListRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::opc_ros::ActionSetListRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ActionSetListRequest_

typedef ::opc_ros::ActionSetListRequest_<std::allocator<void> > ActionSetListRequest;

typedef boost::shared_ptr< ::opc_ros::ActionSetListRequest > ActionSetListRequestPtr;
typedef boost::shared_ptr< ::opc_ros::ActionSetListRequest const> ActionSetListRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::opc_ros::ActionSetListRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::opc_ros::ActionSetListRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace opc_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::opc_ros::ActionSetListRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::opc_ros::ActionSetListRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::opc_ros::ActionSetListRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::opc_ros::ActionSetListRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::opc_ros::ActionSetListRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::opc_ros::ActionSetListRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::opc_ros::ActionSetListRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::opc_ros::ActionSetListRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::opc_ros::ActionSetListRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "opc_ros/ActionSetListRequest";
  }

  static const char* value(const ::opc_ros::ActionSetListRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::opc_ros::ActionSetListRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::opc_ros::ActionSetListRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::opc_ros::ActionSetListRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ActionSetListRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::opc_ros::ActionSetListRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::opc_ros::ActionSetListRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // OPC_ROS_MESSAGE_ACTIONSETLISTREQUEST_H
