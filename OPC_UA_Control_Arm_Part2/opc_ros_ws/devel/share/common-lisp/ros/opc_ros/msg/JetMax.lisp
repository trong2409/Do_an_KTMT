; Auto-generated. Do not edit!


(cl:in-package opc_ros-msg)


;//! \htmlinclude JetMax.msg.html

(cl:defclass <JetMax> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (z
    :reader z
    :initarg :z
    :type cl:float
    :initform 0.0)
   (joint1
    :reader joint1
    :initarg :joint1
    :type cl:float
    :initform 0.0)
   (joint2
    :reader joint2
    :initarg :joint2
    :type cl:float
    :initform 0.0)
   (joint3
    :reader joint3
    :initarg :joint3
    :type cl:float
    :initform 0.0)
   (servo1
    :reader servo1
    :initarg :servo1
    :type cl:float
    :initform 0.0)
   (servo2
    :reader servo2
    :initarg :servo2
    :type cl:float
    :initform 0.0)
   (servo3
    :reader servo3
    :initarg :servo3
    :type cl:float
    :initform 0.0)
   (pwm1
    :reader pwm1
    :initarg :pwm1
    :type cl:float
    :initform 0.0)
   (pwm2
    :reader pwm2
    :initarg :pwm2
    :type cl:float
    :initform 0.0)
   (sucker
    :reader sucker
    :initarg :sucker
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass JetMax (<JetMax>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <JetMax>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'JetMax)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name opc_ros-msg:<JetMax> is deprecated: use opc_ros-msg:JetMax instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <JetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:x-val is deprecated.  Use opc_ros-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <JetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:y-val is deprecated.  Use opc_ros-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <JetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:z-val is deprecated.  Use opc_ros-msg:z instead.")
  (z m))

(cl:ensure-generic-function 'joint1-val :lambda-list '(m))
(cl:defmethod joint1-val ((m <JetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:joint1-val is deprecated.  Use opc_ros-msg:joint1 instead.")
  (joint1 m))

(cl:ensure-generic-function 'joint2-val :lambda-list '(m))
(cl:defmethod joint2-val ((m <JetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:joint2-val is deprecated.  Use opc_ros-msg:joint2 instead.")
  (joint2 m))

(cl:ensure-generic-function 'joint3-val :lambda-list '(m))
(cl:defmethod joint3-val ((m <JetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:joint3-val is deprecated.  Use opc_ros-msg:joint3 instead.")
  (joint3 m))

(cl:ensure-generic-function 'servo1-val :lambda-list '(m))
(cl:defmethod servo1-val ((m <JetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:servo1-val is deprecated.  Use opc_ros-msg:servo1 instead.")
  (servo1 m))

(cl:ensure-generic-function 'servo2-val :lambda-list '(m))
(cl:defmethod servo2-val ((m <JetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:servo2-val is deprecated.  Use opc_ros-msg:servo2 instead.")
  (servo2 m))

(cl:ensure-generic-function 'servo3-val :lambda-list '(m))
(cl:defmethod servo3-val ((m <JetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:servo3-val is deprecated.  Use opc_ros-msg:servo3 instead.")
  (servo3 m))

(cl:ensure-generic-function 'pwm1-val :lambda-list '(m))
(cl:defmethod pwm1-val ((m <JetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:pwm1-val is deprecated.  Use opc_ros-msg:pwm1 instead.")
  (pwm1 m))

(cl:ensure-generic-function 'pwm2-val :lambda-list '(m))
(cl:defmethod pwm2-val ((m <JetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:pwm2-val is deprecated.  Use opc_ros-msg:pwm2 instead.")
  (pwm2 m))

(cl:ensure-generic-function 'sucker-val :lambda-list '(m))
(cl:defmethod sucker-val ((m <JetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-msg:sucker-val is deprecated.  Use opc_ros-msg:sucker instead.")
  (sucker m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <JetMax>) ostream)
  "Serializes a message object of type '<JetMax>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'joint1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'joint2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'joint3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'servo1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'servo2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'servo3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pwm1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pwm2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'sucker) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <JetMax>) istream)
  "Deserializes a message object of type '<JetMax>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'joint1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'joint2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'joint3) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'servo1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'servo2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'servo3) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pwm1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pwm2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'sucker) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<JetMax>)))
  "Returns string type for a message object of type '<JetMax>"
  "opc_ros/JetMax")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'JetMax)))
  "Returns string type for a message object of type 'JetMax"
  "opc_ros/JetMax")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<JetMax>)))
  "Returns md5sum for a message object of type '<JetMax>"
  "98e79b4f27f832f857f4f7315fd89046")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'JetMax)))
  "Returns md5sum for a message object of type 'JetMax"
  "98e79b4f27f832f857f4f7315fd89046")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<JetMax>)))
  "Returns full string definition for message of type '<JetMax>"
  (cl:format cl:nil "float32 x~%float32 y~%float32 z~%float32 joint1~%float32 joint2~%float32 joint3~%float32 servo1~%float32 servo2~%float32 servo3~%float32 pwm1~%float32 pwm2~%bool    sucker~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'JetMax)))
  "Returns full string definition for message of type 'JetMax"
  (cl:format cl:nil "float32 x~%float32 y~%float32 z~%float32 joint1~%float32 joint2~%float32 joint3~%float32 servo1~%float32 servo2~%float32 servo3~%float32 pwm1~%float32 pwm2~%bool    sucker~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <JetMax>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <JetMax>))
  "Converts a ROS message object to a list"
  (cl:list 'JetMax
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':z (z msg))
    (cl:cons ':joint1 (joint1 msg))
    (cl:cons ':joint2 (joint2 msg))
    (cl:cons ':joint3 (joint3 msg))
    (cl:cons ':servo1 (servo1 msg))
    (cl:cons ':servo2 (servo2 msg))
    (cl:cons ':servo3 (servo3 msg))
    (cl:cons ':pwm1 (pwm1 msg))
    (cl:cons ':pwm2 (pwm2 msg))
    (cl:cons ':sucker (sucker msg))
))
