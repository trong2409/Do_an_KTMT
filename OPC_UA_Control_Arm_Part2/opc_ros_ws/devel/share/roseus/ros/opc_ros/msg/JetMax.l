;; Auto-generated. Do not edit!


(when (boundp 'opc_ros::JetMax)
  (if (not (find-package "OPC_ROS"))
    (make-package "OPC_ROS"))
  (shadow 'JetMax (find-package "OPC_ROS")))
(unless (find-package "OPC_ROS::JETMAX")
  (make-package "OPC_ROS::JETMAX"))

(in-package "ROS")
;;//! \htmlinclude JetMax.msg.html


(defclass opc_ros::JetMax
  :super ros::object
  :slots (_x _y _z _joint1 _joint2 _joint3 _servo1 _servo2 _servo3 _pwm1 _pwm2 _sucker ))

(defmethod opc_ros::JetMax
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:joint1 __joint1) 0.0)
    ((:joint2 __joint2) 0.0)
    ((:joint3 __joint3) 0.0)
    ((:servo1 __servo1) 0.0)
    ((:servo2 __servo2) 0.0)
    ((:servo3 __servo3) 0.0)
    ((:pwm1 __pwm1) 0.0)
    ((:pwm2 __pwm2) 0.0)
    ((:sucker __sucker) nil)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _joint1 (float __joint1))
   (setq _joint2 (float __joint2))
   (setq _joint3 (float __joint3))
   (setq _servo1 (float __servo1))
   (setq _servo2 (float __servo2))
   (setq _servo3 (float __servo3))
   (setq _pwm1 (float __pwm1))
   (setq _pwm2 (float __pwm2))
   (setq _sucker __sucker)
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:joint1
   (&optional __joint1)
   (if __joint1 (setq _joint1 __joint1)) _joint1)
  (:joint2
   (&optional __joint2)
   (if __joint2 (setq _joint2 __joint2)) _joint2)
  (:joint3
   (&optional __joint3)
   (if __joint3 (setq _joint3 __joint3)) _joint3)
  (:servo1
   (&optional __servo1)
   (if __servo1 (setq _servo1 __servo1)) _servo1)
  (:servo2
   (&optional __servo2)
   (if __servo2 (setq _servo2 __servo2)) _servo2)
  (:servo3
   (&optional __servo3)
   (if __servo3 (setq _servo3 __servo3)) _servo3)
  (:pwm1
   (&optional __pwm1)
   (if __pwm1 (setq _pwm1 __pwm1)) _pwm1)
  (:pwm2
   (&optional __pwm2)
   (if __pwm2 (setq _pwm2 __pwm2)) _pwm2)
  (:sucker
   (&optional __sucker)
   (if __sucker (setq _sucker __sucker)) _sucker)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _z
    4
    ;; float32 _joint1
    4
    ;; float32 _joint2
    4
    ;; float32 _joint3
    4
    ;; float32 _servo1
    4
    ;; float32 _servo2
    4
    ;; float32 _servo3
    4
    ;; float32 _pwm1
    4
    ;; float32 _pwm2
    4
    ;; bool _sucker
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _z
       (sys::poke _z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _joint1
       (sys::poke _joint1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _joint2
       (sys::poke _joint2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _joint3
       (sys::poke _joint3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _servo1
       (sys::poke _servo1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _servo2
       (sys::poke _servo2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _servo3
       (sys::poke _servo3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pwm1
       (sys::poke _pwm1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pwm2
       (sys::poke _pwm2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _sucker
       (if _sucker (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _z
     (setq _z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _joint1
     (setq _joint1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _joint2
     (setq _joint2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _joint3
     (setq _joint3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _servo1
     (setq _servo1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _servo2
     (setq _servo2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _servo3
     (setq _servo3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pwm1
     (setq _pwm1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pwm2
     (setq _pwm2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _sucker
     (setq _sucker (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get opc_ros::JetMax :md5sum-) "98e79b4f27f832f857f4f7315fd89046")
(setf (get opc_ros::JetMax :datatype-) "opc_ros/JetMax")
(setf (get opc_ros::JetMax :definition-)
      "float32 x
float32 y
float32 z
float32 joint1
float32 joint2
float32 joint3
float32 servo1
float32 servo2
float32 servo3
float32 pwm1
float32 pwm2
bool    sucker

")



(provide :opc_ros/JetMax "98e79b4f27f832f857f4f7315fd89046")


