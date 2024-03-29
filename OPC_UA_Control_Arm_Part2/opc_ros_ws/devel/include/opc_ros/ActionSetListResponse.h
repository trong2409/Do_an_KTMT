// Generated by gencpp from file opc_ros/ActionSetListResponse.msg
// DO NOT EDIT!


#ifndef OPC_ROS_MESSAGE_ACTIONSETLISTRESPONSE_H
#define OPC_ROS_MESSAGE_ACTIONSETLISTRESPONSE_H


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
struct ActionSetListResponse_
{
  typedef ActionSetListResponse_<ContainerAllocator> Type;

  ActionSetListResponse_()
    : action_sets()  {
    }
  ActionSetListResponse_(const ContainerAllocator& _alloc)
    : action_sets(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> _action_sets_type;
  _action_sets_type action_sets;





  typedef boost::shared_ptr< ::opc_ros::ActionSetListResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::opc_ros::ActionSetListResponse_<ContainerAllocator> const> ConstPtr;

}; // struct ActionSetListResponse_

typedef ::opc_ros::ActionSetListResponse_<std::allocator<void> > ActionSetListResponse;

typedef boost::shared_ptr< ::opc_ros::ActionSetListResponse > ActionSetListResponsePtr;
typedef boost::shared_ptr< ::opc_ros::ActionSetListResponse const> ActionSetListResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::opc_ros::ActionSetListResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::opc_ros::ActionSetListResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::opc_ros::ActionSetListResponse_<ContainerAllocator1> & lhs, const ::opc_ros::ActionSetListResponse_<ContainerAllocator2> & rhs)
{
  return lhs.action_sets == rhs.action_sets;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::opc_ros::ActionSetListResponse_<ContainerAllocator1> & lhs, const ::opc_ros::ActionSetListResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace opc_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::opc_ros::ActionSetListResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::opc_ros::ActionSetListResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::opc_ros::ActionSetListResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::opc_ros::ActionSetListResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::opc_ros::ActionSetListResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::opc_ros::ActionSetListResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::opc_ros::ActionSetListResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "eef2f65442e5649b9b3489933fa21e88";
  }

  static const char* value(const ::opc_ros::ActionSetListResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xeef2f65442e5649bULL;
  static const uint64_t static_value2 = 0x9b3489933fa21e88ULL;
};

template<class ContainerAllocator>
struct DataType< ::opc_ros::ActionSetListResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "opc_ros/ActionSetListResponse";
  }

  static const char* value(const ::opc_ros::ActionSetListResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::opc_ros::ActionSetListResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string[] action_sets\n"
;
  }

  static const char* value(const ::opc_ros::ActionSetListResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::opc_ros::ActionSetListResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.action_sets);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ActionSetListResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::opc_ros::ActionSetListResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::opc_ros::ActionSetListResponse_<ContainerAllocator>& v)
  {
    s << indent << "action_sets[]" << std::endl;
    for (size_t i = 0; i < v.action_sets.size(); ++i)
    {
      s << indent << "  action_sets[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.action_sets[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // OPC_ROS_MESSAGE_ACTIONSETLISTRESPONSE_H
