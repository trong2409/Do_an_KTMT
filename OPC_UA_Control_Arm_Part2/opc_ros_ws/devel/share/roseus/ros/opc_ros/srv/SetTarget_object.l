;; Auto-generated. Do not edit!


(when (boundp 'opc_ros::SetTarget_object)
  (if (not (find-package "OPC_ROS"))
    (make-package "OPC_ROS"))
  (shadow 'SetTarget_object (find-package "OPC_ROS")))
(unless (find-package "OPC_ROS::SETTARGET_OBJECT")
  (make-package "OPC_ROS::SETTARGET_OBJECT"))
(unless (find-package "OPC_ROS::SETTARGET_OBJECTREQUEST")
  (make-package "OPC_ROS::SETTARGET_OBJECTREQUEST"))
(unless (find-package "OPC_ROS::SETTARGET_OBJECTRESPONSE")
  (make-package "OPC_ROS::SETTARGET_OBJECTRESPONSE"))

(in-package "ROS")





(defclass opc_ros::SetTarget_objectRequest
  :super ros::object
  :slots (_color_name ))

(defmethod opc_ros::SetTarget_objectRequest
  (:init
   (&key
    ((:color_name __color_name) "")
    )
   (send-super :init)
   (setq _color_name (string __color_name))
   self)
  (:color_name
   (&optional __color_name)
   (if __color_name (setq _color_name __color_name)) _color_name)
  (:serialization-length
   ()
   (+
    ;; string _color_name
    4 (length _color_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _color_name
       (write-long (length _color_name) s) (princ _color_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _color_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _color_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass opc_ros::SetTarget_objectResponse
  :super ros::object
  :slots (_success _message ))

(defmethod opc_ros::SetTarget_objectResponse
  (:init
   (&key
    ((:success __success) nil)
    ((:message __message) "")
    )
   (send-super :init)
   (setq _success __success)
   (setq _message (string __message))
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass opc_ros::SetTarget_object
  :super ros::object
  :slots ())

(setf (get opc_ros::SetTarget_object :md5sum-) "b043027b67620a7221fbfd7733360ab7")
(setf (get opc_ros::SetTarget_object :datatype-) "opc_ros/SetTarget_object")
(setf (get opc_ros::SetTarget_object :request) opc_ros::SetTarget_objectRequest)
(setf (get opc_ros::SetTarget_object :response) opc_ros::SetTarget_objectResponse)

(defmethod opc_ros::SetTarget_objectRequest
  (:response () (instance opc_ros::SetTarget_objectResponse :init)))

(setf (get opc_ros::SetTarget_objectRequest :md5sum-) "b043027b67620a7221fbfd7733360ab7")
(setf (get opc_ros::SetTarget_objectRequest :datatype-) "opc_ros/SetTarget_objectRequest")
(setf (get opc_ros::SetTarget_objectRequest :definition-)
      "string color_name
---
bool success
string message
")

(setf (get opc_ros::SetTarget_objectResponse :md5sum-) "b043027b67620a7221fbfd7733360ab7")
(setf (get opc_ros::SetTarget_objectResponse :datatype-) "opc_ros/SetTarget_objectResponse")
(setf (get opc_ros::SetTarget_objectResponse :definition-)
      "string color_name
---
bool success
string message
")



(provide :opc_ros/SetTarget_object "b043027b67620a7221fbfd7733360ab7")


