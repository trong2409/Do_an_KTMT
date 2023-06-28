; Auto-generated. Do not edit!


(cl:in-package remote_control-msg)


;//! \htmlinclude Status.msg.html

(cl:defclass <Status> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:fixnum
    :initform 0)
   (y
    :reader y
    :initarg :y
    :type cl:fixnum
    :initform 0)
   (z
    :reader z
    :initarg :z
    :type cl:fixnum
    :initform 0)
   (id1
    :reader id1
    :initarg :id1
    :type cl:fixnum
    :initform 0)
   (id2
    :reader id2
    :initarg :id2
    :type cl:fixnum
    :initform 0)
   (id3
    :reader id3
    :initarg :id3
    :type cl:fixnum
    :initform 0)
   (id4
    :reader id4
    :initarg :id4
    :type cl:fixnum
    :initform 0)
   (pwm1
    :reader pwm1
    :initarg :pwm1
    :type cl:fixnum
    :initform 0)
   (motor1
    :reader motor1
    :initarg :motor1
    :type cl:fixnum
    :initform 0)
   (motor2
    :reader motor2
    :initarg :motor2
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Status (<Status>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Status>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Status)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name remote_control-msg:<Status> is deprecated: use remote_control-msg:Status instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <Status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-msg:x-val is deprecated.  Use remote_control-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <Status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-msg:y-val is deprecated.  Use remote_control-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <Status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-msg:z-val is deprecated.  Use remote_control-msg:z instead.")
  (z m))

(cl:ensure-generic-function 'id1-val :lambda-list '(m))
(cl:defmethod id1-val ((m <Status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-msg:id1-val is deprecated.  Use remote_control-msg:id1 instead.")
  (id1 m))

(cl:ensure-generic-function 'id2-val :lambda-list '(m))
(cl:defmethod id2-val ((m <Status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-msg:id2-val is deprecated.  Use remote_control-msg:id2 instead.")
  (id2 m))

(cl:ensure-generic-function 'id3-val :lambda-list '(m))
(cl:defmethod id3-val ((m <Status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-msg:id3-val is deprecated.  Use remote_control-msg:id3 instead.")
  (id3 m))

(cl:ensure-generic-function 'id4-val :lambda-list '(m))
(cl:defmethod id4-val ((m <Status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-msg:id4-val is deprecated.  Use remote_control-msg:id4 instead.")
  (id4 m))

(cl:ensure-generic-function 'pwm1-val :lambda-list '(m))
(cl:defmethod pwm1-val ((m <Status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-msg:pwm1-val is deprecated.  Use remote_control-msg:pwm1 instead.")
  (pwm1 m))

(cl:ensure-generic-function 'motor1-val :lambda-list '(m))
(cl:defmethod motor1-val ((m <Status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-msg:motor1-val is deprecated.  Use remote_control-msg:motor1 instead.")
  (motor1 m))

(cl:ensure-generic-function 'motor2-val :lambda-list '(m))
(cl:defmethod motor2-val ((m <Status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader remote_control-msg:motor2-val is deprecated.  Use remote_control-msg:motor2 instead.")
  (motor2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Status>) ostream)
  "Serializes a message object of type '<Status>"
  (cl:let* ((signed (cl:slot-value msg 'x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'z)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id3)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id3)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id4)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id4)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'pwm1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'motor1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'motor2)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Status>) istream)
  "Deserializes a message object of type '<Status>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'z) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id3)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id3)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id4)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id4)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'pwm1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'motor1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'motor2)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Status>)))
  "Returns string type for a message object of type '<Status>"
  "remote_control/Status")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Status)))
  "Returns string type for a message object of type 'Status"
  "remote_control/Status")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Status>)))
  "Returns md5sum for a message object of type '<Status>"
  "590d96bbbe0686d00dc0bf91b47e905e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Status)))
  "Returns md5sum for a message object of type 'Status"
  "590d96bbbe0686d00dc0bf91b47e905e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Status>)))
  "Returns full string definition for message of type '<Status>"
  (cl:format cl:nil "int16 x~%int16 y~%int16 z~%uint16 id1~%uint16 id2~%uint16 id3~%uint16 id4~%uint8 pwm1~%uint8 motor1~%uint8 motor2~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Status)))
  "Returns full string definition for message of type 'Status"
  (cl:format cl:nil "int16 x~%int16 y~%int16 z~%uint16 id1~%uint16 id2~%uint16 id3~%uint16 id4~%uint8 pwm1~%uint8 motor1~%uint8 motor2~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Status>))
  (cl:+ 0
     2
     2
     2
     2
     2
     2
     2
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Status>))
  "Converts a ROS message object to a list"
  (cl:list 'Status
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':z (z msg))
    (cl:cons ':id1 (id1 msg))
    (cl:cons ':id2 (id2 msg))
    (cl:cons ':id3 (id3 msg))
    (cl:cons ':id4 (id4 msg))
    (cl:cons ':pwm1 (pwm1 msg))
    (cl:cons ':motor1 (motor1 msg))
    (cl:cons ':motor2 (motor2 msg))
))
