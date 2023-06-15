// Generated by gencpp from file opc_ros/ActionSetFileOpRequest.msg
// DO NOT EDIT!


#ifndef OPC_ROS_MESSAGE_ACTIONSETFILEOPREQUEST_H
#define OPC_ROS_MESSAGE_ACTIONSETFILEOPREQUEST_H


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
struct ActionSetFileOpRequest_
{
  typedef ActionSetFileOpRequest_<ContainerAllocator> Type;

  ActionSetFileOpRequest_()
    : file_name()
    , data()  {
    }
  ActionSetFileOpRequest_(const ContainerAllocator& _alloc)
    : file_name(_alloc)
    , data(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _file_name_type;
  _file_name_type file_name;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _data_type;
  _data_type data;





  typedef boost::shared_ptr< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ActionSetFileOpRequest_

typedef ::opc_ros::ActionSetFileOpRequest_<std::allocator<void> > ActionSetFileOpRequest;

typedef boost::shared_ptr< ::opc_ros::ActionSetFileOpRequest > ActionSetFileOpRequestPtr;
typedef boost::shared_ptr< ::opc_ros::ActionSetFileOpRequest const> ActionSetFileOpRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator1> & lhs, const ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator2> & rhs)
{
  return lhs.file_name == rhs.file_name &&
    lhs.data == rhs.data;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator1> & lhs, const ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace opc_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6839f44290942d193717d03c0a9ccb99";
  }

  static const char* value(const ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6839f44290942d19ULL;
  static const uint64_t static_value2 = 0x3717d03c0a9ccb99ULL;
};

template<class ContainerAllocator>
struct DataType< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "opc_ros/ActionSetFileOpRequest";
  }

  static const char* value(const ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string file_name\n"
"string data\n"
;
  }

  static const char* value(const ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.file_name);
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ActionSetFileOpRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::opc_ros::ActionSetFileOpRequest_<ContainerAllocator>& v)
  {
    s << indent << "file_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.file_name);
    s << indent << "data: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.data);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OPC_ROS_MESSAGE_ACTIONSETFILEOPREQUEST_H
