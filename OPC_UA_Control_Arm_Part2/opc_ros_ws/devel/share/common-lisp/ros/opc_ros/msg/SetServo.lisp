; Auto-generated. Do not edit!


(cl:in-package opc_ros-msg)


;//! \htmlinclude SetServo.msg.html

(cl:defclass <SetServo> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type cl:fixnum
    :initform 0)
   (duration
    :reader duration
    :initarg :duration
    :type cl:float
    :initform 0.0))
)

(cl:defclass SetServo (<SetServo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetServo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetServo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name opc_ros-msg:<SetServo> is deprecated: use opc_ros-msg:SetServo instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <SetServo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:data-val is deprecated.  Use opc_ros-msg:data instead.")
  (data m))

(cl:ensure-generic-function 'duration-val :lambda-list '(m))
(cl:defmethod duration-val ((m <SetServo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:duration-val is deprecated.  Use opc_ros-msg:duration instead.")
  (duration m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetServo>) ostream)
  "Serializes a message object of type '<SetServo>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'data)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'data)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'duration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetServo>) istream)
  "Deserializes a message object of type '<SetServo>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'data)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'data)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'duration) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetServo>)))
  "Returns string type for a message object of type '<SetServo>"
  "opc_ros/SetServo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetServo)))
  "Returns string type for a message object of type 'SetServo"
  "opc_ros/SetServo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetServo>)))
  "Returns md5sum for a message object of type '<SetServo>"
  "b17bd22a947dc3333e94c2b1699db322")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetServo)))
  "Returns md5sum for a message object of type 'SetServo"
  "b17bd22a947dc3333e94c2b1699db322")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetServo>)))
  "Returns full string definition for message of type '<SetServo>"
  (cl:format cl:nil "uint16 data~%float32 duration~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetServo)))
  "Returns full string definition for message of type 'SetServo"
  (cl:format cl:nil "uint16 data~%float32 duration~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetServo>))
  (cl:+ 0
     2
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetServo>))
  "Converts a ROS message object to a list"
  (cl:list 'SetServo
    (cl:cons ':data (data msg))
    (cl:cons ':duration (duration msg))
))
