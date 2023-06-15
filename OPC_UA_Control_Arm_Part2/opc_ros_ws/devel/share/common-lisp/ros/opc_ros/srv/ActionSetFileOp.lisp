; Auto-generated. Do not edit!


(cl:in-package opc_ros-srv)


;//! \htmlinclude ActionSetFileOp-request.msg.html

(cl:defclass <ActionSetFileOp-request> (roslisp-msg-protocol:ros-message)
  ((file_name
    :reader file_name
    :initarg :file_name
    :type cl:string
    :initform "")
   (data
    :reader data
    :initarg :data
    :type cl:string
    :initform ""))
)

(cl:defclass ActionSetFileOp-request (<ActionSetFileOp-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActionSetFileOp-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActionSetFileOp-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name opc_ros-srv:<ActionSetFileOp-request> is deprecated: use opc_ros-srv:ActionSetFileOp-request instead.")))

(cl:ensure-generic-function 'file_name-val :lambda-list '(m))
(cl:defmethod file_name-val ((m <ActionSetFileOp-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-srv:file_name-val is deprecated.  Use opc_ros-srv:file_name instead.")
  (file_name m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <ActionSetFileOp-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-srv:data-val is deprecated.  Use opc_ros-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActionSetFileOp-request>) ostream)
  "Serializes a message object of type '<ActionSetFileOp-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'file_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'file_name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActionSetFileOp-request>) istream)
  "Deserializes a message object of type '<ActionSetFileOp-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'file_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'file_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'data) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'data) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActionSetFileOp-request>)))
  "Returns string type for a service object of type '<ActionSetFileOp-request>"
  "opc_ros/ActionSetFileOpRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionSetFileOp-request)))
  "Returns string type for a service object of type 'ActionSetFileOp-request"
  "opc_ros/ActionSetFileOpRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActionSetFileOp-request>)))
  "Returns md5sum for a message object of type '<ActionSetFileOp-request>"
  "272e984a50155b54f97a32954cf22782")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActionSetFileOp-request)))
  "Returns md5sum for a message object of type 'ActionSetFileOp-request"
  "272e984a50155b54f97a32954cf22782")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActionSetFileOp-request>)))
  "Returns full string definition for message of type '<ActionSetFileOp-request>"
  (cl:format cl:nil "string file_name~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActionSetFileOp-request)))
  "Returns full string definition for message of type 'ActionSetFileOp-request"
  (cl:format cl:nil "string file_name~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActionSetFileOp-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'file_name))
     4 (cl:length (cl:slot-value msg 'data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActionSetFileOp-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ActionSetFileOp-request
    (cl:cons ':file_name (file_name msg))
    (cl:cons ':data (data msg))
))
;//! \htmlinclude ActionSetFileOp-response.msg.html

(cl:defclass <ActionSetFileOp-response> (roslisp-msg-protocol:ros-message)
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

(cl:defclass ActionSetFileOp-response (<ActionSetFileOp-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActionSetFileOp-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActionSetFileOp-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name opc_ros-srv:<ActionSetFileOp-response> is deprecated: use opc_ros-srv:ActionSetFileOp-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <ActionSetFileOp-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-srv:success-val is deprecated.  Use opc_ros-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <ActionSetFileOp-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-srv:message-val is deprecated.  Use opc_ros-srv:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActionSetFileOp-response>) ostream)
  "Serializes a message object of type '<ActionSetFileOp-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActionSetFileOp-response>) istream)
  "Deserializes a message object of type '<ActionSetFileOp-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActionSetFileOp-response>)))
  "Returns string type for a service object of type '<ActionSetFileOp-response>"
  "opc_ros/ActionSetFileOpResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionSetFileOp-response)))
  "Returns string type for a service object of type 'ActionSetFileOp-response"
  "opc_ros/ActionSetFileOpResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActionSetFileOp-response>)))
  "Returns md5sum for a message object of type '<ActionSetFileOp-response>"
  "272e984a50155b54f97a32954cf22782")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActionSetFileOp-response)))
  "Returns md5sum for a message object of type 'ActionSetFileOp-response"
  "272e984a50155b54f97a32954cf22782")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActionSetFileOp-response>)))
  "Returns full string definition for message of type '<ActionSetFileOp-response>"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActionSetFileOp-response)))
  "Returns full string definition for message of type 'ActionSetFileOp-response"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActionSetFileOp-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActionSetFileOp-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ActionSetFileOp-response
    (cl:cons ':success (success msg))
    (cl:cons ':message (message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ActionSetFileOp)))
  'ActionSetFileOp-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ActionSetFileOp)))
  'ActionSetFileOp-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionSetFileOp)))
  "Returns string type for a service object of type '<ActionSetFileOp>"
  "opc_ros/ActionSetFileOp")