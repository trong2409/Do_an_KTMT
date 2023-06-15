; Auto-generated. Do not edit!


(cl:in-package opc_ros-srv)


;//! \htmlinclude ActionSetList-request.msg.html

(cl:defclass <ActionSetList-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass ActionSetList-request (<ActionSetList-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActionSetList-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActionSetList-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name opc_ros-srv:<ActionSetList-request> is deprecated: use opc_ros-srv:ActionSetList-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActionSetList-request>) ostream)
  "Serializes a message object of type '<ActionSetList-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActionSetList-request>) istream)
  "Deserializes a message object of type '<ActionSetList-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActionSetList-request>)))
  "Returns string type for a service object of type '<ActionSetList-request>"
  "opc_ros/ActionSetListRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionSetList-request)))
  "Returns string type for a service object of type 'ActionSetList-request"
  "opc_ros/ActionSetListRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActionSetList-request>)))
  "Returns md5sum for a message object of type '<ActionSetList-request>"
  "eef2f65442e5649b9b3489933fa21e88")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActionSetList-request)))
  "Returns md5sum for a message object of type 'ActionSetList-request"
  "eef2f65442e5649b9b3489933fa21e88")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActionSetList-request>)))
  "Returns full string definition for message of type '<ActionSetList-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActionSetList-request)))
  "Returns full string definition for message of type 'ActionSetList-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActionSetList-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActionSetList-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ActionSetList-request
))
;//! \htmlinclude ActionSetList-response.msg.html

(cl:defclass <ActionSetList-response> (roslisp-msg-protocol:ros-message)
  ((action_sets
    :reader action_sets
    :initarg :action_sets
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass ActionSetList-response (<ActionSetList-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActionSetList-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActionSetList-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name opc_ros-srv:<ActionSetList-response> is deprecated: use opc_ros-srv:ActionSetList-response instead.")))

(cl:ensure-generic-function 'action_sets-val :lambda-list '(m))
(cl:defmethod action_sets-val ((m <ActionSetList-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opc_ros-srv:action_sets-val is deprecated.  Use opc_ros-srv:action_sets instead.")
  (action_sets m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActionSetList-response>) ostream)
  "Serializes a message object of type '<ActionSetList-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'action_sets))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'action_sets))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActionSetList-response>) istream)
  "Deserializes a message object of type '<ActionSetList-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'action_sets) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'action_sets)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActionSetList-response>)))
  "Returns string type for a service object of type '<ActionSetList-response>"
  "opc_ros/ActionSetListResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionSetList-response)))
  "Returns string type for a service object of type 'ActionSetList-response"
  "opc_ros/ActionSetListResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActionSetList-response>)))
  "Returns md5sum for a message object of type '<ActionSetList-response>"
  "eef2f65442e5649b9b3489933fa21e88")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActionSetList-response)))
  "Returns md5sum for a message object of type 'ActionSetList-response"
  "eef2f65442e5649b9b3489933fa21e88")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActionSetList-response>)))
  "Returns full string definition for message of type '<ActionSetList-response>"
  (cl:format cl:nil "string[] action_sets~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActionSetList-response)))
  "Returns full string definition for message of type 'ActionSetList-response"
  (cl:format cl:nil "string[] action_sets~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActionSetList-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'action_sets) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActionSetList-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ActionSetList-response
    (cl:cons ':action_sets (action_sets msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ActionSetList)))
  'ActionSetList-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ActionSetList)))
  'ActionSetList-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionSetList)))
  "Returns string type for a service object of type '<ActionSetList>"
  "opc_ros/ActionSetList")