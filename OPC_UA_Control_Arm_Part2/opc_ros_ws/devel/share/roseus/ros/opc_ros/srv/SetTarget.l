;; Auto-generated. Do not edit!


(when (boundp 'opc_ros::SetTarget)
  (if (not (find-package "OPC_ROS"))
    (make-package "OPC_ROS"))
  (shadow 'SetTarget (find-package "OPC_ROS")))
(unless (find-package "OPC_ROS::SETTARGET")
  (make-package "OPC_ROS::SETTARGET"))
(unless (find-package "OPC_ROS::SETTARGETREQUEST")
  (make-package "OPC_ROS::SETTARGETREQUEST"))
(unless (find-package "OPC_ROS::SETTARGETRESPONSE")
  (make-package "OPC_ROS::SETTARGETRESPONSE"))

(in-package "ROS")





(defclass opc_ros::SetTargetRequest
  :super ros::object
  :slots (_color_name _is_enable ))

(defmethod opc_ros::SetTargetRequest
  (:init
   (&key
    ((:color_name __color_name) "")
    ((:is_enable __is_enable) nil)
    )
   (send-super :init)
   (setq _color_name (string __color_name))
   (setq _is_enable __is_enable)
   self)
  (:color_name
   (&optional __color_name)
   (if __color_name (setq _color_name __color_name)) _color_name)
  (:is_enable
   (&optional __is_enable)
   (if __is_enable (setq _is_enable __is_enable)) _is_enable)
  (:serialization-length
   ()
   (+
    ;; string _color_name
    4 (length _color_name)
    ;; bool _is_enable
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _color_name
       (write-long (length _color_name) s) (princ _color_name s)
     ;; bool _is_enable
       (if _is_enable (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _color_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _color_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _is_enable
     (setq _is_enable (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass opc_ros::SetTargetResponse
  :super ros::object
  :slots (_success _message ))

(defmethod opc_ros::SetTargetResponse
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

(defclass opc_ros::SetTarget
  :super ros::object
  :slots ())

(setf (get opc_ros::SetTarget :md5sum-) "d59dc51bea53a4877185283f71dbf83c")
(setf (get opc_ros::SetTarget :datatype-) "opc_ros/SetTarget")
(setf (get opc_ros::SetTarget :request) opc_ros::SetTargetRequest)
(setf (get opc_ros::SetTarget :response) opc_ros::SetTargetResponse)

(defmethod opc_ros::SetTargetRequest
  (:response () (instance opc_ros::SetTargetResponse :init)))

(setf (get opc_ros::SetTargetRequest :md5sum-) "d59dc51bea53a4877185283f71dbf83c")
(setf (get opc_ros::SetTargetRequest :datatype-) "opc_ros/SetTargetRequest")
(setf (get opc_ros::SetTargetRequest :definition-)
      "string color_name
bool is_enable
---
bool success
string message
")

(setf (get opc_ros::SetTargetResponse :md5sum-) "d59dc51bea53a4877185283f71dbf83c")
(setf (get opc_ros::SetTargetResponse :datatype-) "opc_ros/SetTargetResponse")
(setf (get opc_ros::SetTargetResponse :definition-)
      "string color_name
bool is_enable
---
bool success
string message
")



(provide :opc_ros/SetTarget "d59dc51bea53a4877185283f71dbf83c")


