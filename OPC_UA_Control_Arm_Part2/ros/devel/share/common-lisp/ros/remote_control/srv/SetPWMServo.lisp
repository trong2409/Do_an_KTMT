; Auto-generated. Do not edit!


(cl:in-package remote_control-srv)


;//! \htmlinclude SetPWMServo-request.msg.html

(cl:defclass <SetPWMServo-request> (roslisp-msg-protocol:ros-message)
  ((servo_id
    :reader servo_id
    :initarg :servo_id
    :type cl:fixnum
    :initform 0)
   (angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0)
   (duration
    :reader duration
    :initarg :duration
    :type cl:float
    :initform 0.0))
)

(cl:defclass SetPWMServo-request (<SetPWMServo-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetPWMServo-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetPWMServo-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name remote_control-srv:<SetPWMServo-request> is deprecated: use remote_control-srv:SetPWMServo-request instead.")))

(cl:ensure-generic-function 'servo_id-val :lambda-list '(m))
(cl:defmethod servo_id-val ((m <SetPWMServo-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:servo_id-val is deprecated.  Use remote_control-srv:servo_id instead.")
  (servo_id m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <SetPWMServo-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:angle-val is deprecated.  Use remote_control-srv:angle instead.")
  (angle m))

(cl:ensure-generic-function 'duration-val :lambda-list '(m))
(cl:defmethod duration-val ((m <SetPWMServo-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:duration-val is deprecated.  Use remote_control-srv:duration instead.")
  (duration m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetPWMServo-request>) ostream)
  "Serializes a message object of type '<SetPWMServo-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'servo_id)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle))))
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetPWMServo-request>) istream)
  "Deserializes a message object of type '<SetPWMServo-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'servo_id)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'duration) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetPWMServo-request>)))
  "Returns string type for a service object of type '<SetPWMServo-request>"
  "remote_control/SetPWMServoRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetPWMServo-request)))
  "Returns string type for a service object of type 'SetPWMServo-request"
  "remote_control/SetPWMServoRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetPWMServo-request>)))
  "Returns md5sum for a message object of type '<SetPWMServo-request>"
  "6e1eb645b22b8412b0f366c1854f41ef")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetPWMServo-request)))
  "Returns md5sum for a message object of type 'SetPWMServo-request"
  "6e1eb645b22b8412b0f366c1854f41ef")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetPWMServo-request>)))
  "Returns full string definition for message of type '<SetPWMServo-request>"
  (cl:format cl:nil "uint8 servo_id~%float32 angle~%float32 duration~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetPWMServo-request)))
  "Returns full string definition for message of type 'SetPWMServo-request"
  (cl:format cl:nil "uint8 servo_id~%float32 angle~%float32 duration~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetPWMServo-request>))
  (cl:+ 0
     1
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetPWMServo-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetPWMServo-request
    (cl:cons ':servo_id (servo_id msg))
    (cl:cons ':angle (angle msg))
    (cl:cons ':duration (duration msg))
))
;//! \htmlinclude SetPWMServo-response.msg.html

(cl:defclass <SetPWMServo-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil)
   (message
    :reader message
    :initarg :message
    :type cl:string
    :initform ""))
)

(cl:defclass SetPWMServo-response (<SetPWMServo-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetPWMServo-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetPWMServo-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name remote_control-srv:<SetPWMServo-response> is deprecated: use remote_control-srv:SetPWMServo-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetPWMServo-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:success-val is deprecated.  Use remote_control-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <SetPWMServo-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:message-val is deprecated.  Use remote_control-srv:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetPWMServo-response>) ostream)
  "Serializes a message object of type '<SetPWMServo-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetPWMServo-response>) istream)
  "Deserializes a message object of type '<SetPWMServo-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetPWMServo-response>)))
  "Returns string type for a service object of type '<SetPWMServo-response>"
  "remote_control/SetPWMServoResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetPWMServo-response)))
  "Returns string type for a service object of type 'SetPWMServo-response"
  "remote_control/SetPWMServoResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetPWMServo-response>)))
  "Returns md5sum for a message object of type '<SetPWMServo-response>"
  "6e1eb645b22b8412b0f366c1854f41ef")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetPWMServo-response)))
  "Returns md5sum for a message object of type 'SetPWMServo-response"
  "6e1eb645b22b8412b0f366c1854f41ef")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetPWMServo-response>)))
  "Returns full string definition for message of type '<SetPWMServo-response>"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetPWMServo-response)))
  "Returns full string definition for message of type 'SetPWMServo-response"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetPWMServo-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetPWMServo-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetPWMServo-response
    (cl:cons ':success (success msg))
    (cl:cons ':message (message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetPWMServo)))
  'SetPWMServo-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetPWMServo)))
  'SetPWMServo-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetPWMServo)))
  "Returns string type for a service object of type '<SetPWMServo>"
  "remote_control/SetPWMServo")