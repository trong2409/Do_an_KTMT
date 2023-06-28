;; Auto-generated. Do not edit!


(when (boundp 'remote_control::Status)
  (if (not (find-package "REMOTE_CONTROL"))
    (make-package "REMOTE_CONTROL"))
  (shadow 'Status (find-package "REMOTE_CONTROL")))
(unless (find-package "REMOTE_CONTROL::STATUS")
  (make-package "REMOTE_CONTROL::STATUS"))

(in-package "ROS")
;;//! \htmlinclude Status.msg.html


(defclass remote_control::Status
  :super ros::object
  :slots (_x _y _z _id1 _id2 _id3 _id4 _pwm1 _motor1 _motor2 ))

(defmethod remote_control::Status
  (:init
   (&key
    ((:x __x) 0)
    ((:y __y) 0)
    ((:z __z) 0)
    ((:id1 __id1) 0)
    ((:id2 __id2) 0)
    ((:id3 __id3) 0)
    ((:id4 __id4) 0)
    ((:pwm1 __pwm1) 0)
    ((:motor1 __motor1) 0)
    ((:motor2 __motor2) 0)
    )
   (send-super :init)
   (setq _x (round __x))
   (setq _y (round __y))
   (setq _z (round __z))
   (setq _id1 (round __id1))
   (setq _id2 (round __id2))
   (setq _id3 (round __id3))
   (setq _id4 (round __id4))
   (setq _pwm1 (round __pwm1))
   (setq _motor1 (round __motor1))
   (setq _motor2 (round __motor2))
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
  (:id1
   (&optional __id1)
   (if __id1 (setq _id1 __id1)) _id1)
  (:id2
   (&optional __id2)
   (if __id2 (setq _id2 __id2)) _id2)
  (:id3
   (&optional __id3)
   (if __id3 (setq _id3 __id3)) _id3)
  (:id4
   (&optional __id4)
   (if __id4 (setq _id4 __id4)) _id4)
  (:pwm1
   (&optional __pwm1)
   (if __pwm1 (setq _pwm1 __pwm1)) _pwm1)
  (:motor1
   (&optional __motor1)
   (if __motor1 (setq _motor1 __motor1)) _motor1)
  (:motor2
   (&optional __motor2)
   (if __motor2 (setq _motor2 __motor2)) _motor2)
  (:serialization-length
   ()
   (+
    ;; int16 _x
    2
    ;; int16 _y
    2
    ;; int16 _z
    2
    ;; uint16 _id1
    2
    ;; uint16 _id2
    2
    ;; uint16 _id3
    2
    ;; uint16 _id4
    2
    ;; uint8 _pwm1
    1
    ;; uint8 _motor1
    1
    ;; uint8 _motor2
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _x
       (write-word _x s)
     ;; int16 _y
       (write-word _y s)
     ;; int16 _z
       (write-word _z s)
     ;; uint16 _id1
       (write-word _id1 s)
     ;; uint16 _id2
       (write-word _id2 s)
     ;; uint16 _id3
       (write-word _id3 s)
     ;; uint16 _id4
       (write-word _id4 s)
     ;; uint8 _pwm1
       (write-byte _pwm1 s)
     ;; uint8 _motor1
       (write-byte _motor1 s)
     ;; uint8 _motor2
       (write-byte _motor2 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _x
     (setq _x (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _y
     (setq _y (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _z
     (setq _z (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _id1
     (setq _id1 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _id2
     (setq _id2 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _id3
     (setq _id3 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _id4
     (setq _id4 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint8 _pwm1
     (setq _pwm1 (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _motor1
     (setq _motor1 (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _motor2
     (setq _motor2 (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get remote_control::Status :md5sum-) "590d96bbbe0686d00dc0bf91b47e905e")
(setf (get remote_control::Status :datatype-) "remote_control/Status")
(setf (get remote_control::Status :definition-)
      "int16 x
int16 y
int16 z
uint16 id1
uint16 id2
uint16 id3
uint16 id4
uint8 pwm1
uint8 motor1
uint8 motor2


")



(provide :remote_control/Status "590d96bbbe0686d00dc0bf91b47e905e")


