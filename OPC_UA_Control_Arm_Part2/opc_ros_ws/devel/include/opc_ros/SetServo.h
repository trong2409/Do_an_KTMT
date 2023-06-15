// Generated by gencpp from file opc_ros/SetServo.msg
// DO NOT EDIT!


#ifndef OPC_ROS_MESSAGE_SETSERVO_H
#define OPC_ROS_MESSAGE_SETSERVO_H


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
struct SetServo_
{
  typedef SetServo_<ContainerAllocator> Type;

  SetServo_()
    : data(0)
    , duration(0.0)  {
    }
  SetServo_(const ContainerAllocator& _alloc)
    : data(0)
    , duration(0.0)  {
  (void)_alloc;
    }



   typedef uint16_t _data_type;
  _data_type data;

   typedef float _duration_type;
  _duration_type duration;





  typedef boost::shared_ptr< ::opc_ros::SetServo_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::opc_ros::SetServo_<ContainerAllocator> const> ConstPtr;

}; // struct SetServo_

typedef ::opc_ros::SetServo_<std::allocator<void> > SetServo;

typedef boost::shared_ptr< ::opc_ros::SetServo > SetServoPtr;
typedef boost::shared_ptr< ::opc_ros::SetServo const> SetServoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::opc_ros::SetServo_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::opc_ros::SetServo_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::opc_ros::SetServo_<ContainerAllocator1> & lhs, const ::opc_ros::SetServo_<ContainerAllocator2> & rhs)
{
  return lhs.data == rhs.data &&
    lhs.duration == rhs.duration;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::opc_ros::SetServo_<ContainerAllocator1> & lhs, const ::opc_ros::SetServo_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace opc_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::opc_ros::SetServo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::opc_ros::SetServo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::opc_ros::SetServo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::opc_ros::SetServo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::opc_ros::SetServo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::opc_ros::SetServo_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::opc_ros::SetServo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b17bd22a947dc3333e94c2b1699db322";
  }

  static const char* value(const ::opc_ros::SetServo_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb17bd22a947dc333ULL;
  static const uint64_t static_value2 = 0x3e94c2b1699db322ULL;
};

template<class ContainerAllocator>
struct DataType< ::opc_ros::SetServo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "opc_ros/SetServo";
  }

  static const char* value(const ::opc_ros::SetServo_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::opc_ros::SetServo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint16 data\n"
"float32 duration\n"
;
  }

  static const char* value(const ::opc_ros::SetServo_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::opc_ros::SetServo_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.data);
      stream.next(m.duration);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetServo_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::opc_ros::SetServo_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::opc_ros::SetServo_<ContainerAllocator>& v)
  {
    s << indent << "data: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.data);
    s << indent << "duration: ";
    Printer<float>::stream(s, indent + "  ", v.duration);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OPC_ROS_MESSAGE_SETSERVO_H
