; Auto-generated. Do not edit!


(cl:in-package opc_ros-msg)


;//! \htmlinclude SetJoint.msg.html

(cl:defclass <SetJoint> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type cl:float
    :initform 0.0)
   (duration
    :reader duration
    :initarg :duration
    :type cl:float
    :initform 0.0))
)

(cl:defclass SetJoint (<SetJoint>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetJoint>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetJoint)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name opc_ros-msg:<SetJoint> is deprecated: use opc_ros-msg:SetJoint instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <SetJoint>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:data-val is deprecated.  Use opc_ros-msg:data instead.")
  (data m))

(cl:ensure-generic-function 'duration-val :lambda-list '(m))
(cl:defmethod duration-val ((m <SetJoint>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:duration-val is deprecated.  Use opc_ros-msg:duration instead.")
  (duration m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetJoint>) ostream)
  "Serializes a message object of type '<SetJoint>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'duration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetJoint>) istream)
  "Deserializes a message object of type '<SetJoint>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'data) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'duration) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetJoint>)))
  "Returns string type for a message object of type '<SetJoint>"
  "opc_ros/SetJoint")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetJoint)))
  "Returns string type for a message object of type 'SetJoint"
  "opc_ros/SetJoint")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetJoint>)))
  "Returns md5sum for a message object of type '<SetJoint>"
  "d2a6e247129185fb38f8296bf00e1d24")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetJoint)))
  "Returns md5sum for a message object of type 'SetJoint"
  "d2a6e247129185fb38f8296bf00e1d24")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetJoint>)))
  "Returns full string definition for message of type '<SetJoint>"
  (cl:format cl:nil "float32 data~%float32 duration~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetJoint)))
  "Returns full string definition for message of type 'SetJoint"
  (cl:format cl:nil "float32 data~%float32 duration~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetJoint>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetJoint>))
  "Converts a ROS message object to a list"
  (cl:list 'SetJoint
    (cl:cons ':data (data msg))
    (cl:cons ':duration (duration msg))
))
