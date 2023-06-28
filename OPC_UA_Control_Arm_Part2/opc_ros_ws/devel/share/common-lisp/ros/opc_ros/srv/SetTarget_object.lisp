; Auto-generated. Do not edit!


(cl:in-package opc_ros-srv)


;//! \htmlinclude SetTarget_object-request.msg.html

(cl:defclass <SetTarget_object-request> (roslisp-msg-protocol:ros-message)
  ((color_name
    :reader color_name
    :initarg :color_name
    :type cl:string
    :initform ""))
)

(cl:defclass SetTarget_object-request (<SetTarget_object-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetTarget_object-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetTarget_object-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name opc_ros-srv:<SetTarget_object-request> is deprecated: use opc_ros-srv:SetTarget_object-request instead.")))

(cl:ensure-generic-function 'color_name-val :lambda-list '(m))
(cl:defmethod color_name-val ((m <SetTarget_object-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-srv:color_name-val is deprecated.  Use opc_ros-srv:color_name instead.")
  (color_name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetTarget_object-request>) ostream)
  "Serializes a message object of type '<SetTarget_object-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'color_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'color_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetTarget_object-request>) istream)
  "Deserializes a message object of type '<SetTarget_object-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'color_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'color_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetTarget_object-request>)))
  "Returns string type for a service object of type '<SetTarget_object-request>"
  "opc_ros/SetTarget_objectRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetTarget_object-request)))
  "Returns string type for a service object of type 'SetTarget_object-request"
  "opc_ros/SetTarget_objectRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetTarget_object-request>)))
  "Returns md5sum for a message object of type '<SetTarget_object-request>"
  "b043027b67620a7221fbfd7733360ab7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetTarget_object-request)))
  "Returns md5sum for a message object of type 'SetTarget_object-request"
  "b043027b67620a7221fbfd7733360ab7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetTarget_object-request>)))
  "Returns full string definition for message of type '<SetTarget_object-request>"
  (cl:format cl:nil "string color_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetTarget_object-request)))
  "Returns full string definition for message of type 'SetTarget_object-request"
  (cl:format cl:nil "string color_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetTarget_object-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'color_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetTarget_object-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetTarget_object-request
    (cl:cons ':color_name (color_name msg))
))
;//! \htmlinclude SetTarget_object-response.msg.html

(cl:defclass <SetTarget_object-response> (roslisp-msg-protocol:ros-message)
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

(cl:defclass SetTarget_object-response (<SetTarget_object-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetTarget_object-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetTarget_object-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name opc_ros-srv:<SetTarget_object-response> is deprecated: use opc_ros-srv:SetTarget_object-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetTarget_object-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-srv:success-val is deprecated.  Use opc_ros-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <SetTarget_object-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-srv:message-val is deprecated.  Use opc_ros-srv:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetTarget_object-response>) ostream)
  "Serializes a message object of type '<SetTarget_object-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetTarget_object-response>) istream)
  "Deserializes a message object of type '<SetTarget_object-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetTarget_object-response>)))
  "Returns string type for a service object of type '<SetTarget_object-response>"
  "opc_ros/SetTarget_objectResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetTarget_object-response)))
  "Returns string type for a service object of type 'SetTarget_object-response"
  "opc_ros/SetTarget_objectResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetTarget_object-response>)))
  "Returns md5sum for a message object of type '<SetTarget_object-response>"
  "b043027b67620a7221fbfd7733360ab7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetTarget_object-response)))
  "Returns md5sum for a message object of type 'SetTarget_object-response"
  "b043027b67620a7221fbfd7733360ab7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetTarget_object-response>)))
  "Returns full string definition for message of type '<SetTarget_object-response>"
  (cl:format cl:nil "bool success~%string message~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetTarget_object-response)))
  "Returns full string definition for message of type 'SetTarget_object-response"
  (cl:format cl:nil "bool success~%string message~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetTarget_object-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetTarget_object-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetTarget_object-response
    (cl:cons ':success (success msg))
    (cl:cons ':message (message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetTarget_object)))
  'SetTarget_object-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetTarget_object)))
  'SetTarget_object-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetTarget_object)))
  "Returns string type for a service object of type '<SetTarget_object>"
  "opc_ros/SetTarget_object")