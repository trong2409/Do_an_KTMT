; Auto-generated. Do not edit!


(cl:in-package jetmax_control-msg)


;//! \htmlinclude SetJetMax.msg.html

(cl:defclass <SetJetMax> (roslisp-msg-protocol:ros-message)
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
   (duration
    :reader duration
    :initarg :duration
    :type cl:float
    :initform 0.0))
)

(cl:defclass SetJetMax (<SetJetMax>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetJetMax>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetJetMax)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name jetmax_control-msg:<SetJetMax> is deprecated: use jetmax_control-msg:SetJetMax instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <SetJetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jetmax_control-msg:x-val is deprecated.  Use jetmax_control-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <SetJetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jetmax_control-msg:y-val is deprecated.  Use jetmax_control-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <SetJetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jetmax_control-msg:z-val is deprecated.  Use jetmax_control-msg:z instead.")
  (z m))

(cl:ensure-generic-function 'duration-val :lambda-list '(m))
(cl:defmethod duration-val ((m <SetJetMax>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader jetmax_control-msg:duration-val is deprecated.  Use jetmax_control-msg:duration instead.")
  (duration m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetJetMax>) ostream)
  "Serializes a message object of type '<SetJetMax>"
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
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'duration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetJetMax>) istream)
  "Deserializes a message object of type '<SetJetMax>"
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
    (cl:setf (cl:slot-value msg 'duration) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetJetMax>)))
  "Returns string type for a message object of type '<SetJetMax>"
  "jetmax_control/SetJetMax")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetJetMax)))
  "Returns string type for a message object of type 'SetJetMax"
  "jetmax_control/SetJetMax")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetJetMax>)))
  "Returns md5sum for a message object of type '<SetJetMax>"
  "19cc8078d43cb0cd983e9688d658cb05")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetJetMax)))
  "Returns md5sum for a message object of type 'SetJetMax"
  "19cc8078d43cb0cd983e9688d658cb05")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetJetMax>)))
  "Returns full string definition for message of type '<SetJetMax>"
  (cl:format cl:nil "float32 x~%float32 y~%float32 z~%float32 duration~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetJetMax)))
  "Returns full string definition for message of type 'SetJetMax"
  (cl:format cl:nil "float32 x~%float32 y~%float32 z~%float32 duration~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetJetMax>))
  (cl:+ 0
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetJetMax>))
  "Converts a ROS message object to a list"
  (cl:list 'SetJetMax
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':z (z msg))
    (cl:cons ':duration (duration msg))
))
