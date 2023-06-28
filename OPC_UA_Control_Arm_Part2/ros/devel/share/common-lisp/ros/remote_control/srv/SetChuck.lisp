; Auto-generated. Do not edit!


(cl:in-package remote_control-srv)


;//! \htmlinclude SetChuck-request.msg.html

(cl:defclass <SetChuck-request> (roslisp-msg-protocol:ros-message)
  ((absorb
    :reader absorb
    :initarg :absorb
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SetChuck-request (<SetChuck-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetChuck-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetChuck-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name remote_control-srv:<SetChuck-request> is deprecated: use remote_control-srv:SetChuck-request instead.")))

(cl:ensure-generic-function 'absorb-val :lambda-list '(m))
(cl:defmethod absorb-val ((m <SetChuck-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:absorb-val is deprecated.  Use remote_control-srv:absorb instead.")
  (absorb m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetChuck-request>) ostream)
  "Serializes a message object of type '<SetChuck-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'absorb) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetChuck-request>) istream)
  "Deserializes a message object of type '<SetChuck-request>"
    (cl:setf (cl:slot-value msg 'absorb) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetChuck-request>)))
  "Returns string type for a service object of type '<SetChuck-request>"
  "remote_control/SetChuckRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetChuck-request)))
  "Returns string type for a service object of type 'SetChuck-request"
  "remote_control/SetChuckRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetChuck-request>)))
  "Returns md5sum for a message object of type '<SetChuck-request>"
  "be1a696a40f3aa3626e65e8ab32b15fa")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetChuck-request)))
  "Returns md5sum for a message object of type 'SetChuck-request"
  "be1a696a40f3aa3626e65e8ab32b15fa")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetChuck-request>)))
  "Returns full string definition for message of type '<SetChuck-request>"
  (cl:format cl:nil "bool absorb~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetChuck-request)))
  "Returns full string definition for message of type 'SetChuck-request"
  (cl:format cl:nil "bool absorb~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetChuck-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetChuck-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetChuck-request
    (cl:cons ':absorb (absorb msg))
))
;//! \htmlinclude SetChuck-response.msg.html

(cl:defclass <SetChuck-response> (roslisp-msg-protocol:ros-message)
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

(cl:defclass SetChuck-response (<SetChuck-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetChuck-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetChuck-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name remote_control-srv:<SetChuck-response> is deprecated: use remote_control-srv:SetChuck-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetChuck-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:success-val is deprecated.  Use remote_control-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <SetChuck-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-srv:message-val is deprecated.  Use remote_control-srv:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetChuck-response>) ostream)
  "Serializes a message object of type '<SetChuck-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetChuck-response>) istream)
  "Deserializes a message object of type '<SetChuck-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetChuck-response>)))
  "Returns string type for a service object of type '<SetChuck-response>"
  "remote_control/SetChuckResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetChuck-response)))
  "Returns string type for a service object of type 'SetChuck-response"
  "remote_control/SetChuckResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetChuck-response>)))
  "Returns md5sum for a message object of type '<SetChuck-response>"
  "be1a696a40f3aa3626e65e8ab32b15fa")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetChuck-response)))
  "Returns md5sum for a message object of type 'SetChuck-response"
  "be1a696a40f3aa3626e65e8ab32b15fa")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetChuck-response>)))
  "Returns full string definition for message of type '<SetChuck-response>"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetChuck-response)))
  "Returns full string definition for message of type 'SetChuck-response"
  (cl:format cl:nil "bool success~%string message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetChuck-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetChuck-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetChuck-response
    (cl:cons ':success (success msg))
    (cl:cons ':message (message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetChuck)))
  'SetChuck-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetChuck)))
  'SetChuck-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetChuck)))
  "Returns string type for a service object of type '<SetChuck>"
  "remote_control/SetChuck")