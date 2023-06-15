;; Auto-generated. Do not edit!


(when (boundp 'opc_ros::Mecanum)
  (if (not (find-package "OPC_ROS"))
    (make-package "OPC_ROS"))
  (shadow 'Mecanum (find-package "OPC_ROS")))
(unless (find-package "OPC_ROS::MECANUM")
  (make-package "OPC_ROS::MECANUM"))

(in-package "ROS")
;;//! \htmlinclude Mecanum.msg.html


(defclass opc_ros::Mecanum
  :super ros::object
  :slots (_velocity _direction _angular_rate ))

(defmethod opc_ros::Mecanum
  (:init
   (&key
    ((:velocity __velocity) 0.0)
    ((:direction __direction) 0.0)
    ((:angular_rate __angular_rate) 0.0)
    )
   (send-super :init)
   (setq _velocity (float __velocity))
   (setq _direction (float __direction))
   (setq _angular_rate (float __angular_rate))
   self)
  (:velocity
   (&optional __velocity)
   (if __velocity (setq _velocity __velocity)) _velocity)
  (:direction
   (&optional __direction)
   (if __direction (setq _direction __direction)) _direction)
  (:angular_rate
   (&optional __angular_rate)
   (if __angular_rate (setq _angular_rate __angular_rate)) _angular_rate)
  (:serialization-length
   ()
   (+
    ;; float32 _velocity
    4
    ;; float32 _direction
    4
    ;; float32 _angular_rate
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _velocity
       (sys::poke _velocity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _direction
       (sys::poke _direction (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _angular_rate
       (sys::poke _angular_rate (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _velocity
     (setq _velocity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _direction
     (setq _direction (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _angular_rate
     (setq _angular_rate (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get opc_ros::Mecanum :md5sum-) "ac02d3f7aa8716c10f969453bc5f21a8")
(setf (get opc_ros::Mecanum :datatype-) "opc_ros/Mecanum")
(setf (get opc_ros::Mecanum :definition-)
      "float32 velocity
float32 direction
float32 angular_rate
")



(provide :opc_ros/Mecanum "ac02d3f7aa8716c10f969453bc5f21a8")


