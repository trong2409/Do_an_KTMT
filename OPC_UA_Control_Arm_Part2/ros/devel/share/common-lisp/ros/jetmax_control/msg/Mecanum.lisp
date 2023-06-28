; Auto-generated. Do not edit!


(cl:in-package jetmax_control-msg)


;//! \htmlinclude Mecanum.msg.html

(cl:defclass <Mecanum> (roslisp-msg-protocol:ros-message)
  ((velocity
    :reader velocity
    :initarg :velocity
    :type cl:float
    :initform 0.0)
   (direction
    :reader direction
    :initarg :direction
    :type cl:float
    :initform 0.0)
   (angular_rate
    :reader angular_rate
    :initarg :angular_rate
    :type cl:float
    :initform 0.0))
)

(cl:defclass Mecanum (<Mecanum>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Mecanum>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Mecanum)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name jetmax_control-msg:<Mecanum> is deprecated: use jetmax_control-msg:Mecanum instead.")))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <Mecanum>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jetmax_control-msg:velocity-val is deprecated.  Use jetmax_control-msg:velocity instead.")
  (velocity m))

(cl:ensure-generic-function 'direction-val :lambda-list '(m))
(cl:defmethod direction-val ((m <Mecanum>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jetmax_control-msg:direction-val is deprecated.  Use jetmax_control-msg:direction instead.")
  (direction m))

(cl:ensure-generic-function 'angular_rate-val :lambda-list '(m))
(cl:defmethod angular_rate-val ((m <Mecanum>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jetmax_control-msg:angular_rate-val is deprecated.  Use jetmax_control-msg:angular_rate instead.")
  (angular_rate m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Mecanum>) ostream)
  "Serializes a message object of type '<Mecanum>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'direction))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angular_rate))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Mecanum>) istream)
  "Deserializes a message object of type '<Mecanum>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'velocity) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'direction) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angular_rate) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Mecanum>)))
  "Returns string type for a message object of type '<Mecanum>"
  "jetmax_control/Mecanum")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Mecanum)))
  "Returns string type for a message object of type 'Mecanum"
  "jetmax_control/Mecanum")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Mecanum>)))
  "Returns md5sum for a message object of type '<Mecanum>"
  "ac02d3f7aa8716c10f969453bc5f21a8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Mecanum)))
  "Returns md5sum for a message object of type 'Mecanum"
  "ac02d3f7aa8716c10f969453bc5f21a8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Mecanum>)))
  "Returns full string definition for message of type '<Mecanum>"
  (cl:format cl:nil "float32 velocity~%float32 direction~%float32 angular_rate~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Mecanum)))
  "Returns full string definition for message of type 'Mecanum"
  (cl:format cl:nil "float32 velocity~%float32 direction~%float32 angular_rate~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Mecanum>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Mecanum>))
  "Converts a ROS message object to a list"
  (cl:list 'Mecanum
    (cl:cons ':velocity (velocity msg))
    (cl:cons ':direction (direction msg))
    (cl:cons ':angular_rate (angular_rate msg))
))
