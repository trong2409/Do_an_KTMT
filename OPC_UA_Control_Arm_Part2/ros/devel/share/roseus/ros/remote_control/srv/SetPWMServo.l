;; Auto-generated. Do not edit!


(when (boundp 'remote_control::SetPWMServo)
  (if (not (find-package "REMOTE_CONTROL"))
    (make-package "REMOTE_CONTROL"))
  (shadow 'SetPWMServo (find-package "REMOTE_CONTROL")))
(unless (find-package "REMOTE_CONTROL::SETPWMSERVO")
  (make-package "REMOTE_CONTROL::SETPWMSERVO"))
(unless (find-package "REMOTE_CONTROL::SETPWMSERVOREQUEST")
  (make-package "REMOTE_CONTROL::SETPWMSERVOREQUEST"))
(unless (find-package "REMOTE_CONTROL::SETPWMSERVORESPONSE")
  (make-package "REMOTE_CONTROL::SETPWMSERVORESPONSE"))

(in-package "ROS")





(defclass remote_control::SetPWMServoRequest
  :super ros::object
  :slots (_servo_id _angle _duration ))

(defmethod remote_control::SetPWMServoRequest
  (:init
   (&key
    ((:servo_id __servo_id) 0)
    ((:angle __angle) 0.0)
    ((:duration __duration) 0.0)
    )
   (send-super :init)
   (setq _servo_id (round __servo_id))
   (setq _angle (float __angle))
   (setq _duration (float __duration))
   self)
  (:servo_id
   (&optional __servo_id)
   (if __servo_id (setq _servo_id __servo_id)) _servo_id)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:duration
   (&optional __duration)
   (if __duration (setq _duration __duration)) _duration)
  (:serialization-length
   ()
   (+
    ;; uint8 _servo_id
    1
    ;; float32 _angle
    4
    ;; float32 _duration
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _servo_id
       (write-byte _servo_id s)
     ;; float32 _angle
       (sys::poke _angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _duration
       (sys::poke _duration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _servo_id
     (setq _servo_id (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _angle
     (setq _angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _duration
     (setq _duration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass remote_control::SetPWMServoResponse
  :super ros::object
  :slots (_success _message ))

(defmethod remote_control::SetPWMServoResponse
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

(defclass remote_control::SetPWMServo
  :super ros::object
  :slots ())

(setf (get remote_control::SetPWMServo :md5sum-) "6e1eb645b22b8412b0f366c1854f41ef")
(setf (get remote_control::SetPWMServo :datatype-) "remote_control/SetPWMServo")
(setf (get remote_control::SetPWMServo :request) remote_control::SetPWMServoRequest)
(setf (get remote_control::SetPWMServo :response) remote_control::SetPWMServoResponse)

(defmethod remote_control::SetPWMServoRequest
  (:response () (instance remote_control::SetPWMServoResponse :init)))

(setf (get remote_control::SetPWMServoRequest :md5sum-) "6e1eb645b22b8412b0f366c1854f41ef")
(setf (get remote_control::SetPWMServoRequest :datatype-) "remote_control/SetPWMServoRequest")
(setf (get remote_control::SetPWMServoRequest :definition-)
      "uint8 servo_id
float32 angle
float32 duration
---
bool success
string message
")

(setf (get remote_control::SetPWMServoResponse :md5sum-) "6e1eb645b22b8412b0f366c1854f41ef")
(setf (get remote_control::SetPWMServoResponse :datatype-) "remote_control/SetPWMServoResponse")
(setf (get remote_control::SetPWMServoResponse :definition-)
      "uint8 servo_id
float32 angle
float32 duration
---
bool success
string message
")



(provide :remote_control/SetPWMServo "6e1eb645b22b8412b0f366c1854f41ef")


