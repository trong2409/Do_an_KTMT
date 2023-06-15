;; Auto-generated. Do not edit!


(when (boundp 'jetmax_control::IK)
  (if (not (find-package "JETMAX_CONTROL"))
    (make-package "JETMAX_CONTROL"))
  (shadow 'IK (find-package "JETMAX_CONTROL")))
(unless (find-package "JETMAX_CONTROL::IK")
  (make-package "JETMAX_CONTROL::IK"))
(unless (find-package "JETMAX_CONTROL::IKREQUEST")
  (make-package "JETMAX_CONTROL::IKREQUEST"))
(unless (find-package "JETMAX_CONTROL::IKRESPONSE")
  (make-package "JETMAX_CONTROL::IKRESPONSE"))

(in-package "ROS")





(defclass jetmax_control::IKRequest
  :super ros::object
  :slots (_x _y _z ))

(defmethod jetmax_control::IKRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
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
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass jetmax_control::IKResponse
  :super ros::object
  :slots (_success ))

(defmethod jetmax_control::IKResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass jetmax_control::IK
  :super ros::object
  :slots ())

(setf (get jetmax_control::IK :md5sum-) "14fb54e9e518f55d418823395ca25d0b")
(setf (get jetmax_control::IK :datatype-) "jetmax_control/IK")
(setf (get jetmax_control::IK :request) jetmax_control::IKRequest)
(setf (get jetmax_control::IK :response) jetmax_control::IKResponse)

(defmethod jetmax_control::IKRequest
  (:response () (instance jetmax_control::IKResponse :init)))

(setf (get jetmax_control::IKRequest :md5sum-) "14fb54e9e518f55d418823395ca25d0b")
(setf (get jetmax_control::IKRequest :datatype-) "jetmax_control/IKRequest")
(setf (get jetmax_control::IKRequest :definition-)
      "float64 x
float64 y
float64 z
---
bool success

")

(setf (get jetmax_control::IKResponse :md5sum-) "14fb54e9e518f55d418823395ca25d0b")
(setf (get jetmax_control::IKResponse :datatype-) "jetmax_control/IKResponse")
(setf (get jetmax_control::IKResponse :definition-)
      "float64 x
float64 y
float64 z
---
bool success

")



(provide :jetmax_control/IK "14fb54e9e518f55d418823395ca25d0b")


