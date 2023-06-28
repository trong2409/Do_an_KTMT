;; Auto-generated. Do not edit!


(when (boundp 'remote_control::SetPosition)
  (if (not (find-package "REMOTE_CONTROL"))
    (make-package "REMOTE_CONTROL"))
  (shadow 'SetPosition (find-package "REMOTE_CONTROL")))
(unless (find-package "REMOTE_CONTROL::SETPOSITION")
  (make-package "REMOTE_CONTROL::SETPOSITION"))
(unless (find-package "REMOTE_CONTROL::SETPOSITIONREQUEST")
  (make-package "REMOTE_CONTROL::SETPOSITIONREQUEST"))
(unless (find-package "REMOTE_CONTROL::SETPOSITIONRESPONSE")
  (make-package "REMOTE_CONTROL::SETPOSITIONRESPONSE"))

(in-package "ROS")





(defclass remote_control::SetPositionRequest
  :super ros::object
  :slots (_x _y _z _duration ))

(defmethod remote_control::SetPositionRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:duration __duration) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _duration (float __duration))
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
  (:duration
   (&optional __duration)
   (if __duration (setq _duration __duration)) _duration)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _z
    4
    ;; float32 _duration
    4
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
     ;; float32 _duration
       (sys::poke _duration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
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
   ;; float32 _duration
     (setq _duration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass remote_control::SetPositionResponse
  :super ros::object
  :slots (_success _message ))

(defmethod remote_control::SetPositionResponse
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

(defclass remote_control::SetPosition
  :super ros::object
  :slots ())

(setf (get remote_control::SetPosition :md5sum-) "b0eee1376ff6f9ce415abb3534488423")
(setf (get remote_control::SetPosition :datatype-) "remote_control/SetPosition")
(setf (get remote_control::SetPosition :request) remote_control::SetPositionRequest)
(setf (get remote_control::SetPosition :response) remote_control::SetPositionResponse)

(defmethod remote_control::SetPositionRequest
  (:response () (instance remote_control::SetPositionResponse :init)))

(setf (get remote_control::SetPositionRequest :md5sum-) "b0eee1376ff6f9ce415abb3534488423")
(setf (get remote_control::SetPositionRequest :datatype-) "remote_control/SetPositionRequest")
(setf (get remote_control::SetPositionRequest :definition-)
      "float32 x
float32 y
float32 z
float32 duration
---
bool success
string message
")

(setf (get remote_control::SetPositionResponse :md5sum-) "b0eee1376ff6f9ce415abb3534488423")
(setf (get remote_control::SetPositionResponse :datatype-) "remote_control/SetPositionResponse")
(setf (get remote_control::SetPositionResponse :definition-)
      "float32 x
float32 y
float32 z
float32 duration
---
bool success
string message
")



(provide :remote_control/SetPosition "b0eee1376ff6f9ce415abb3534488423")


