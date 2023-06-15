// Generated by gencpp from file opc_ros/JetMax.msg
// DO NOT EDIT!


#ifndef OPC_ROS_MESSAGE_JETMAX_H
#define OPC_ROS_MESSAGE_JETMAX_H


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
struct JetMax_
{
  typedef JetMax_<ContainerAllocator> Type;

  JetMax_()
    : x(0.0)
    , y(0.0)
    , z(0.0)
    , joint1(0.0)
    , joint2(0.0)
    , joint3(0.0)
    , servo1(0.0)
    , servo2(0.0)
    , servo3(0.0)
    , pwm1(0.0)
    , pwm2(0.0)
    , sucker(false)  {
    }
  JetMax_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , z(0.0)
    , joint1(0.0)
    , joint2(0.0)
    , joint3(0.0)
    , servo1(0.0)
    , servo2(0.0)
    , servo3(0.0)
    , pwm1(0.0)
    , pwm2(0.0)
    , sucker(false)  {
  (void)_alloc;
    }



   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;

   typedef float _z_type;
  _z_type z;

   typedef float _joint1_type;
  _joint1_type joint1;

   typedef float _joint2_type;
  _joint2_type joint2;

   typedef float _joint3_type;
  _joint3_type joint3;

   typedef float _servo1_type;
  _servo1_type servo1;

   typedef float _servo2_type;
  _servo2_type servo2;

   typedef float _servo3_type;
  _servo3_type servo3;

   typedef float _pwm1_type;
  _pwm1_type pwm1;

   typedef float _pwm2_type;
  _pwm2_type pwm2;

   typedef uint8_t _sucker_type;
  _sucker_type sucker;





  typedef boost::shared_ptr< ::opc_ros::JetMax_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::opc_ros::JetMax_<ContainerAllocator> const> ConstPtr;

}; // struct JetMax_

typedef ::opc_ros::JetMax_<std::allocator<void> > JetMax;

typedef boost::shared_ptr< ::opc_ros::JetMax > JetMaxPtr;
typedef boost::shared_ptr< ::opc_ros::JetMax const> JetMaxConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::opc_ros::JetMax_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::opc_ros::JetMax_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::opc_ros::JetMax_<ContainerAllocator1> & lhs, const ::opc_ros::JetMax_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.z == rhs.z &&
    lhs.joint1 == rhs.joint1 &&
    lhs.joint2 == rhs.joint2 &&
    lhs.joint3 == rhs.joint3 &&
    lhs.servo1 == rhs.servo1 &&
    lhs.servo2 == rhs.servo2 &&
    lhs.servo3 == rhs.servo3 &&
    lhs.pwm1 == rhs.pwm1 &&
    lhs.pwm2 == rhs.pwm2 &&
    lhs.sucker == rhs.sucker;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::opc_ros::JetMax_<ContainerAllocator1> & lhs, const ::opc_ros::JetMax_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace opc_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::opc_ros::JetMax_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::opc_ros::JetMax_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::opc_ros::JetMax_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::opc_ros::JetMax_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::opc_ros::JetMax_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::opc_ros::JetMax_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::opc_ros::JetMax_<ContainerAllocator> >
{
  static const char* value()
  {
    return "98e79b4f27f832f857f4f7315fd89046";
  }

  static const char* value(const ::opc_ros::JetMax_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x98e79b4f27f832f8ULL;
  static const uint64_t static_value2 = 0x57f4f7315fd89046ULL;
};

template<class ContainerAllocator>
struct DataType< ::opc_ros::JetMax_<ContainerAllocator> >
{
  static const char* value()
  {
    return "opc_ros/JetMax";
  }

  static const char* value(const ::opc_ros::JetMax_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::opc_ros::JetMax_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 x\n"
"float32 y\n"
"float32 z\n"
"float32 joint1\n"
"float32 joint2\n"
"float32 joint3\n"
"float32 servo1\n"
"float32 servo2\n"
"float32 servo3\n"
"float32 pwm1\n"
"float32 pwm2\n"
"bool    sucker\n"
;
  }

  static const char* value(const ::opc_ros::JetMax_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::opc_ros::JetMax_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.z);
      stream.next(m.joint1);
      stream.next(m.joint2);
      stream.next(m.joint3);
      stream.next(m.servo1);
      stream.next(m.servo2);
      stream.next(m.servo3);
      stream.next(m.pwm1);
      stream.next(m.pwm2);
      stream.next(m.sucker);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct JetMax_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::opc_ros::JetMax_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::opc_ros::JetMax_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
    s << indent << "z: ";
    Printer<float>::stream(s, indent + "  ", v.z);
    s << indent << "joint1: ";
    Printer<float>::stream(s, indent + "  ", v.joint1);
    s << indent << "joint2: ";
    Printer<float>::stream(s, indent + "  ", v.joint2);
    s << indent << "joint3: ";
    Printer<float>::stream(s, indent + "  ", v.joint3);
    s << indent << "servo1: ";
    Printer<float>::stream(s, indent + "  ", v.servo1);
    s << indent << "servo2: ";
    Printer<float>::stream(s, indent + "  ", v.servo2);
    s << indent << "servo3: ";
    Printer<float>::stream(s, indent + "  ", v.servo3);
    s << indent << "pwm1: ";
    Printer<float>::stream(s, indent + "  ", v.pwm1);
    s << indent << "pwm2: ";
    Printer<float>::stream(s, indent + "  ", v.pwm2);
    s << indent << "sucker: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.sucker);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OPC_ROS_MESSAGE_JETMAX_H