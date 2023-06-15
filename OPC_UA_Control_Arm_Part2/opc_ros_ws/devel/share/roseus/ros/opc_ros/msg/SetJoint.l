;; Auto-generated. Do not edit!


(when (boundp 'opc_ros::SetJoint)
  (if (not (find-package "OPC_ROS"))
    (make-package "OPC_ROS"))
  (shadow 'SetJoint (find-package "OPC_ROS")))
(unless (find-package "OPC_ROS::SETJOINT")
  (make-package "OPC_ROS::SETJOINT"))

(in-package "ROS")
;;//! \htmlinclude SetJoint.msg.html


(defclass opc_ros::SetJoint
  :super ros::object
  :slots (_data _duration ))

(defmethod opc_ros::SetJoint
  (:init
   (&key
    ((:data __data) 0.0)
    ((:duration __duration) 0.0)
    )
   (send-super :init)
   (setq _data (float __data))
   (setq _duration (float __duration))
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:duration
   (&optional __duration)
   (if __duration (setq _duration __duration)) _duration)
  (:serialization-length
   ()
   (+
    ;; float32 _data
    4
    ;; float32 _duration
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _data
       (sys::poke _data (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _duration
       (sys::poke _duration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _data
     (setq _data (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _duration
     (setq _duration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get opc_ros::SetJoint :md5sum-) "d2a6e247129185fb38f8296bf00e1d24")
(setf (get opc_ros::SetJoint :datatype-) "opc_ros/SetJoint")
(setf (get opc_ros::SetJoint :definition-)
      "float32 data
float32 duration
")



(provide :opc_ros/SetJoint "d2a6e247129185fb38f8296bf00e1d24")


