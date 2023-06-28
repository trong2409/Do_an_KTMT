; Auto-generated. Do not edit!


(cl:in-package remote_control-srv)


;//! \htmlinclude ChangePosition-request.msg.html

(cl:defclass <ChangePosition-request> (roslisp-msg-protocol:ros-message)
  ((axis_name
    :reader axis_name
    :initarg :axis_name
    :type cl:string
    :initform "")
   (change_value
    :reader change_value
    :initarg :change_value
    :type cl:float
    :initform 0.0)
   (duration
    :reader duration
    :initarg :duration
    :type cl:float
    :initform 0.0))
)

(cl:defclass ChangePosition-request (<ChangePosition-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ChangePosition-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ChangePosition-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name remote_control-srv:<ChangePosition-request> is deprecated: use remote_control-srv:ChangePosition-request instead.")))

(cl:ensure-generic-function 'axis_name-val :lambda-list '(m))
(cl:defmethod axis_name-val ((m <ChangePosition-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:axis_name-val is deprecated.  Use remote_control-srv:axis_name instead.")
  (axis_name m))

(cl:ensure-generic-function 'change_value-val :lambda-list '(m))
(cl:defmethod change_value-val ((m <ChangePosition-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:change_value-val is deprecated.  Use remote_control-srv:change_value instead.")
  (change_value m))

(cl:ensure-generic-function 'duration-val :lambda-list '(m))
(cl:defmethod duration-val ((m <ChangePosition-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:duration-val is deprecated.  Use remote_control-srv:duration instead.")
  (duration m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ChangePosition-request>) ostream)
  "Serializes a message object of type '<ChangePosition-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'axis_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'axis_name))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'change_value))))
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ChangePosition-request>) istream)
  "Deserializes a message object of type '<ChangePosition-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'axis_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'axis_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'change_value) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'duration) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ChangePosition-request>)))
  "Returns string type for a service object of type '<ChangePosition-request>"
  "remote_control/ChangePositionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangePosition-request)))
  "Returns string type for a service object of type 'ChangePosition-request"
  "remote_control/ChangePositionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ChangePosition-request>)))
  "Returns md5sum for a message object of type '<ChangePosition-request>"
  "792555415d8fe5c4e60a69456efc5174")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ChangePosition-request)))
  "Returns md5sum for a message object of type 'ChangePosition-request"
  "792555415d8fe5c4e60a69456efc5174")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ChangePosition-request>)))
  "Returns full string definition for message of type '<ChangePosition-request>"
  (cl:format cl:nil "string axis_name~%float32 change_value~%float32 duration~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ChangePosition-request)))
  "Returns full string definition for message of type 'ChangePosition-request"
  (cl:format cl:nil "string axis_name~%float32 change_value~%float32 duration~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ChangePosition-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'axis_name))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ChangePosition-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ChangePosition-request
    (cl:cons ':axis_name (axis_name msg))
    (cl:cons ':change_value (change_value msg))
    (cl:cons ':duration (duration msg))
))
;//! \htmlinclude ChangePosition-response.msg.html

(cl:defclass <ChangePosition-response> (roslisp-msg-protocol:ros-message)
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

(cl:defclass ChangePosition-response (<ChangePosition-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ChangePosition-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ChangePosition-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name remote_control-srv:<ChangePosition-response> is deprecated: use remote_control-srv:ChangePosition-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <ChangePosition-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:success-val is deprecated.  Use remote_control-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <ChangePosition-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:message-val is deprecated.  Use remote_control-srv:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ChangePosition-response>) ostream)
  "Serializes a message object of type '<ChangePosition-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ChangePosition-response>) istream)
  "Deserializes a message object of type '<ChangePosition-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ChangePosition-response>)))
  "Returns string type for a service object of type '<ChangePosition-response>"
  "remote_control/ChangePositionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangePosition-response)))
  "Returns string type for a service object of type 'ChangePosition-response"
  "remote_control/ChangePositionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ChangePosition-response>)))
  "Returns md5sum for a message object of type '<ChangePosition-response>"
  "792555415d8fe5c4e60a69456efc5174")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ChangePosition-response)))
  "Returns md5sum for a message object of type 'ChangePosition-response"
  "792555415d8fe5c4e60a69456efc5174")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ChangePosition-response>)))
  "Returns full string definition for message of type '<ChangePosition-response>"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ChangePosition-response)))
  "Returns full string definition for message of type 'ChangePosition-response"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ChangePosition-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ChangePosition-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ChangePosition-response
    (cl:cons ':success (success msg))
    (cl:cons ':message (message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ChangePosition)))
  'ChangePosition-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ChangePosition)))
  'ChangePosition-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangePosition)))
  "Returns string type for a service object of type '<ChangePosition>"
  "remote_control/ChangePosition")