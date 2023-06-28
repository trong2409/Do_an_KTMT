; Auto-generated. Do not edit!


(cl:in-package color_sorting-srv)


;//! \htmlinclude SetTarget-request.msg.html

(cl:defclass <SetTarget-request> (roslisp-msg-protocol:ros-message)
  ((color_name
    :reader color_name
    :initarg :color_name
    :type cl:string
    :initform "")
   (is_enable
    :reader is_enable
    :initarg :is_enable
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SetTarget-request (<SetTarget-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetTarget-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetTarget-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name color_sorting-srv:<SetTarget-request> is deprecated: use color_sorting-srv:SetTarget-request instead.")))

(cl:ensure-generic-function 'color_name-val :lambda-list '(m))
(cl:defmethod color_name-val ((m <SetTarget-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader color_sorting-srv:color_name-val is deprecated.  Use color_sorting-srv:color_name instead.")
  (color_name m))

(cl:ensure-generic-function 'is_enable-val :lambda-list '(m))
(cl:defmethod is_enable-val ((m <SetTarget-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader color_sorting-srv:is_enable-val is deprecated.  Use color_sorting-srv:is_enable instead.")
  (is_enable m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetTarget-request>) ostream)
  "Serializes a message object of type '<SetTarget-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'color_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'color_name))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'is_enable) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetTarget-request>) istream)
  "Deserializes a message object of type '<SetTarget-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'color_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'color_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'is_enable) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetTarget-request>)))
  "Returns string type for a service object of type '<SetTarget-request>"
  "color_sorting/SetTargetRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetTarget-request)))
  "Returns string type for a service object of type 'SetTarget-request"
  "color_sorting/SetTargetRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetTarget-request>)))
  "Returns md5sum for a message object of type '<SetTarget-request>"
  "d59dc51bea53a4877185283f71dbf83c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetTarget-request)))
  "Returns md5sum for a message object of type 'SetTarget-request"
  "d59dc51bea53a4877185283f71dbf83c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetTarget-request>)))
  "Returns full string definition for message of type '<SetTarget-request>"
  (cl:format cl:nil "string color_name~%bool is_enable~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetTarget-request)))
  "Returns full string definition for message of type 'SetTarget-request"
  (cl:format cl:nil "string color_name~%bool is_enable~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetTarget-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'color_name))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetTarget-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetTarget-request
    (cl:cons ':color_name (color_name msg))
    (cl:cons ':is_enable (is_enable msg))
))
;//! \htmlinclude SetTarget-response.msg.html

(cl:defclass <SetTarget-response> (roslisp-msg-protocol:ros-message)
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

(cl:defclass SetTarget-response (<SetTarget-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetTarget-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetTarget-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name color_sorting-srv:<SetTarget-response> is deprecated: use color_sorting-srv:SetTarget-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetTarget-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader color_sorting-srv:success-val is deprecated.  Use color_sorting-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <SetTarget-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader color_sorting-srv:message-val is deprecated.  Use color_sorting-srv:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetTarget-response>) ostream)
  "Serializes a message object of type '<SetTarget-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetTarget-response>) istream)
  "Deserializes a message object of type '<SetTarget-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetTarget-response>)))
  "Returns string type for a service object of type '<SetTarget-response>"
  "color_sorting/SetTargetResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetTarget-response)))
  "Returns string type for a service object of type 'SetTarget-response"
  "color_sorting/SetTargetResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetTarget-response>)))
  "Returns md5sum for a message object of type '<SetTarget-response>"
  "d59dc51bea53a4877185283f71dbf83c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetTarget-response)))
  "Returns md5sum for a message object of type 'SetTarget-response"
  "d59dc51bea53a4877185283f71dbf83c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetTarget-response>)))
  "Returns full string definition for message of type '<SetTarget-response>"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetTarget-response)))
  "Returns full string definition for message of type 'SetTarget-response"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetTarget-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetTarget-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetTarget-response
    (cl:cons ':success (success msg))
    (cl:cons ':message (message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetTarget)))
  'SetTarget-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetTarget)))
  'SetTarget-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetTarget)))
  "Returns string type for a service object of type '<SetTarget>"
  "color_sorting/SetTarget")