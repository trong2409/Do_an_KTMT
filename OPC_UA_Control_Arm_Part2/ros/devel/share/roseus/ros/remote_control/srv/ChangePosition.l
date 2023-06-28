;; Auto-generated. Do not edit!


(when (boundp 'remote_control::ChangePosition)
  (if (not (find-package "REMOTE_CONTROL"))
    (make-package "REMOTE_CONTROL"))
  (shadow 'ChangePosition (find-package "REMOTE_CONTROL")))
(unless (find-package "REMOTE_CONTROL::CHANGEPOSITION")
  (make-package "REMOTE_CONTROL::CHANGEPOSITION"))
(unless (find-package "REMOTE_CONTROL::CHANGEPOSITIONREQUEST")
  (make-package "REMOTE_CONTROL::CHANGEPOSITIONREQUEST"))
(unless (find-package "REMOTE_CONTROL::CHANGEPOSITIONRESPONSE")
  (make-package "REMOTE_CONTROL::CHANGEPOSITIONRESPONSE"))

(in-package "ROS")





(defclass remote_control::ChangePositionRequest
  :super ros::object
  :slots (_axis_name _change_value _duration ))

(defmethod remote_control::ChangePositionRequest
  (:init
   (&key
    ((:axis_name __axis_name) "")
    ((:change_value __change_value) 0.0)
    ((:duration __duration) 0.0)
    )
   (send-super :init)
   (setq _axis_name (string __axis_name))
   (setq _change_value (float __change_value))
   (setq _duration (float __duration))
   self)
  (:axis_name
   (&optional __axis_name)
   (if __axis_name (setq _axis_name __axis_name)) _axis_name)
  (:change_value
   (&optional __change_value)
   (if __change_value (setq _change_value __change_value)) _change_value)
  (:duration
   (&optional __duration)
   (if __duration (setq _duration __duration)) _duration)
  (:serialization-length
   ()
   (+
    ;; string _axis_name
    4 (length _axis_name)
    ;; float32 _change_value
    4
    ;; float32 _duration
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _axis_name
       (write-long (length _axis_name) s) (princ _axis_name s)
     ;; float32 _change_value
       (sys::poke _change_value (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _duration
       (sys::poke _duration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _axis_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _axis_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _change_value
     (setq _change_value (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _duration
     (setq _duration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass remote_control::ChangePositionResponse
  :super ros::object
  :slots (_success _message ))

(defmethod remote_control::ChangePositionResponse
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

(defclass remote_control::ChangePosition
  :super ros::object
  :slots ())

(setf (get remote_control::ChangePosition :md5sum-) "792555415d8fe5c4e60a69456efc5174")
(setf (get remote_control::ChangePosition :datatype-) "remote_control/ChangePosition")
(setf (get remote_control::ChangePosition :request) remote_control::ChangePositionRequest)
(setf (get remote_control::ChangePosition :response) remote_control::ChangePositionResponse)

(defmethod remote_control::ChangePositionRequest
  (:response () (instance remote_control::ChangePositionResponse :init)))

(setf (get remote_control::ChangePositionRequest :md5sum-) "792555415d8fe5c4e60a69456efc5174")
(setf (get remote_control::ChangePositionRequest :datatype-) "remote_control/ChangePositionRequest")
(setf (get remote_control::ChangePositionRequest :definition-)
      "string axis_name
float32 change_value
float32 duration
---
bool success
string message
")

(setf (get remote_control::ChangePositionResponse :md5sum-) "792555415d8fe5c4e60a69456efc5174")
(setf (get remote_control::ChangePositionResponse :datatype-) "remote_control/ChangePositionResponse")
(setf (get remote_control::ChangePositionResponse :definition-)
      "string axis_name
float32 change_value
float32 duration
---
bool success
string message
")



(provide :remote_control/ChangePosition "792555415d8fe5c4e60a69456efc5174")


