;; Auto-generated. Do not edit!


(when (boundp 'jetmax_control::FK)
  (if (not (find-package "JETMAX_CONTROL"))
    (make-package "JETMAX_CONTROL"))
  (shadow 'FK (find-package "JETMAX_CONTROL")))
(unless (find-package "JETMAX_CONTROL::FK")
  (make-package "JETMAX_CONTROL::FK"))
(unless (find-package "JETMAX_CONTROL::FKREQUEST")
  (make-package "JETMAX_CONTROL::FKREQUEST"))
(unless (find-package "JETMAX_CONTROL::FKRESPONSE")
  (make-package "JETMAX_CONTROL::FKRESPONSE"))

(in-package "ROS")





(defclass jetmax_control::FKRequest
  :super ros::object
  :slots (_angle_rotate _angle_left _angle_right ))

(defmethod jetmax_control::FKRequest
  (:init
   (&key
    ((:angle_rotate __angle_rotate) 0.0)
    ((:angle_left __angle_left) 0.0)
    ((:angle_right __angle_right) 0.0)
    )
   (send-super :init)
   (setq _angle_rotate (float __angle_rotate))
   (setq _angle_left (float __angle_left))
   (setq _angle_right (float __angle_right))
   self)
  (:angle_rotate
   (&optional __angle_rotate)
   (if __angle_rotate (setq _angle_rotate __angle_rotate)) _angle_rotate)
  (:angle_left
   (&optional __angle_left)
   (if __angle_left (setq _angle_left __angle_left)) _angle_left)
  (:angle_right
   (&optional __angle_right)
   (if __angle_right (setq _angle_right __angle_right)) _angle_right)
  (:serialization-length
   ()
   (+
    ;; float64 _angle_rotate
    8
    ;; float64 _angle_left
    8
    ;; float64 _angle_right
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _angle_rotate
       (sys::poke _angle_rotate (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _angle_left
       (sys::poke _angle_left (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _angle_right
       (sys::poke _angle_right (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _angle_rotate
     (setq _angle_rotate (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _angle_left
     (setq _angle_left (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _angle_right
     (setq _angle_right (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass jetmax_control::FKResponse
  :super ros::object
  :slots (_success ))

(defmethod jetmax_control::FKResponse
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

(defclass jetmax_control::FK
  :super ros::object
  :slots ())

(setf (get jetmax_control::FK :md5sum-) "dc592708003b91537cff0bcafe06c7d7")
(setf (get jetmax_control::FK :datatype-) "jetmax_control/FK")
(setf (get jetmax_control::FK :request) jetmax_control::FKRequest)
(setf (get jetmax_control::FK :response) jetmax_control::FKResponse)

(defmethod jetmax_control::FKRequest
  (:response () (instance jetmax_control::FKResponse :init)))

(setf (get jetmax_control::FKRequest :md5sum-) "dc592708003b91537cff0bcafe06c7d7")
(setf (get jetmax_control::FKRequest :datatype-) "jetmax_control/FKRequest")
(setf (get jetmax_control::FKRequest :definition-)
      "float64 angle_rotate
float64 angle_left
float64 angle_right
---
bool success

")

(setf (get jetmax_control::FKResponse :md5sum-) "dc592708003b91537cff0bcafe06c7d7")
(setf (get jetmax_control::FKResponse :datatype-) "jetmax_control/FKResponse")
(setf (get jetmax_control::FKResponse :definition-)
      "float64 angle_rotate
float64 angle_left
float64 angle_right
---
bool success

")



(provide :jetmax_control/FK "dc592708003b91537cff0bcafe06c7d7")


