; Auto-generated. Do not edit!


(cl:in-package jetmax_control-srv)


;//! \htmlinclude FK-request.msg.html

(cl:defclass <FK-request> (roslisp-msg-protocol:ros-message)
  ((angle_rotate
    :reader angle_rotate
    :initarg :angle_rotate
    :type cl:float
    :initform 0.0)
   (angle_left
    :reader angle_left
    :initarg :angle_left
    :type cl:float
    :initform 0.0)
   (angle_right
    :reader angle_right
    :initarg :angle_right
    :type cl:float
    :initform 0.0))
)

(cl:defclass FK-request (<FK-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FK-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FK-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name jetmax_control-srv:<FK-request> is deprecated: use jetmax_control-srv:FK-request instead.")))

(cl:ensure-generic-function 'angle_rotate-val :lambda-list '(m))
(cl:defmethod angle_rotate-val ((m <FK-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jetmax_control-srv:angle_rotate-val is deprecated.  Use jetmax_control-srv:angle_rotate instead.")
  (angle_rotate m))

(cl:ensure-generic-function 'angle_left-val :lambda-list '(m))
(cl:defmethod angle_left-val ((m <FK-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jetmax_control-srv:angle_left-val is deprecated.  Use jetmax_control-srv:angle_left instead.")
  (angle_left m))

(cl:ensure-generic-function 'angle_right-val :lambda-list '(m))
(cl:defmethod angle_right-val ((m <FK-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jetmax_control-srv:angle_right-val is deprecated.  Use jetmax_control-srv:angle_right instead.")
  (angle_right m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FK-request>) ostream)
  "Serializes a message object of type '<FK-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angle_rotate))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angle_left))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angle_right))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FK-request>) istream)
  "Deserializes a message object of type '<FK-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle_rotate) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle_left) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle_right) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FK-request>)))
  "Returns string type for a service object of type '<FK-request>"
  "jetmax_control/FKRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FK-request)))
  "Returns string type for a service object of type 'FK-request"
  "jetmax_control/FKRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FK-request>)))
  "Returns md5sum for a message object of type '<FK-request>"
  "dc592708003b91537cff0bcafe06c7d7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FK-request)))
  "Returns md5sum for a message object of type 'FK-request"
  "dc592708003b91537cff0bcafe06c7d7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FK-request>)))
  "Returns full string definition for message of type '<FK-request>"
  (cl:format cl:nil "float64 angle_rotate~%float64 angle_left~%float64 angle_right~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FK-request)))
  "Returns full string definition for message of type 'FK-request"
  (cl:format cl:nil "float64 angle_rotate~%float64 angle_left~%float64 angle_right~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FK-request>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FK-request>))
  "Converts a ROS message object to a list"
  (cl:list 'FK-request
    (cl:cons ':angle_rotate (angle_rotate msg))
    (cl:cons ':angle_left (angle_left msg))
    (cl:cons ':angle_right (angle_right msg))
))
;//! \htmlinclude FK-response.msg.html

(cl:defclass <FK-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass FK-response (<FK-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FK-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FK-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name jetmax_control-srv:<FK-response> is deprecated: use jetmax_control-srv:FK-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <FK-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jetmax_control-srv:success-val is deprecated.  Use jetmax_control-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FK-response>) ostream)
  "Serializes a message object of type '<FK-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FK-response>) istream)
  "Deserializes a message object of type '<FK-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FK-response>)))
  "Returns string type for a service object of type '<FK-response>"
  "jetmax_control/FKResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FK-response)))
  "Returns string type for a service object of type 'FK-response"
  "jetmax_control/FKResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FK-response>)))
  "Returns md5sum for a message object of type '<FK-response>"
  "dc592708003b91537cff0bcafe06c7d7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FK-response)))
  "Returns md5sum for a message object of type 'FK-response"
  "dc592708003b91537cff0bcafe06c7d7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FK-response>)))
  "Returns full string definition for message of type '<FK-response>"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FK-response)))
  "Returns full string definition for message of type 'FK-response"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FK-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FK-response>))
  "Converts a ROS message object to a list"
  (cl:list 'FK-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'FK)))
  'FK-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'FK)))
  'FK-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FK)))
  "Returns string type for a service object of type '<FK>"
  "jetmax_control/FK")