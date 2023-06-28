;; Auto-generated. Do not edit!


(when (boundp 'remote_control::SetChuck)
  (if (not (find-package "REMOTE_CONTROL"))
    (make-package "REMOTE_CONTROL"))
  (shadow 'SetChuck (find-package "REMOTE_CONTROL")))
(unless (find-package "REMOTE_CONTROL::SETCHUCK")
  (make-package "REMOTE_CONTROL::SETCHUCK"))
(unless (find-package "REMOTE_CONTROL::SETCHUCKREQUEST")
  (make-package "REMOTE_CONTROL::SETCHUCKREQUEST"))
(unless (find-package "REMOTE_CONTROL::SETCHUCKRESPONSE")
  (make-package "REMOTE_CONTROL::SETCHUCKRESPONSE"))

(in-package "ROS")





(defclass remote_control::SetChuckRequest
  :super ros::object
  :slots (_absorb ))

(defmethod remote_control::SetChuckRequest
  (:init
   (&key
    ((:absorb __absorb) nil)
    )
   (send-super :init)
   (setq _absorb __absorb)
   self)
  (:absorb
   (&optional __absorb)
   (if __absorb (setq _absorb __absorb)) _absorb)
  (:serialization-length
   ()
   (+
    ;; bool _absorb
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _absorb
       (if _absorb (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _absorb
     (setq _absorb (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass remote_control::SetChuckResponse
  :super ros::object
  :slots (_success _message ))

(defmethod remote_control::SetChuckResponse
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

(defclass remote_control::SetChuck
  :super ros::object
  :slots ())

(setf (get remote_control::SetChuck :md5sum-) "be1a696a40f3aa3626e65e8ab32b15fa")
(setf (get remote_control::SetChuck :datatype-) "remote_control/SetChuck")
(setf (get remote_control::SetChuck :request) remote_control::SetChuckRequest)
(setf (get remote_control::SetChuck :response) remote_control::SetChuckResponse)

(defmethod remote_control::SetChuckRequest
  (:response () (instance remote_control::SetChuckResponse :init)))

(setf (get remote_control::SetChuckRequest :md5sum-) "be1a696a40f3aa3626e65e8ab32b15fa")
(setf (get remote_control::SetChuckRequest :datatype-) "remote_control/SetChuckRequest")
(setf (get remote_control::SetChuckRequest :definition-)
      "bool absorb
---
bool success
string message
")

(setf (get remote_control::SetChuckResponse :md5sum-) "be1a696a40f3aa3626e65e8ab32b15fa")
(setf (get remote_control::SetChuckResponse :datatype-) "remote_control/SetChuckResponse")
(setf (get remote_control::SetChuckResponse :definition-)
      "bool absorb
---
bool success
string message
")



(provide :remote_control/SetChuck "be1a696a40f3aa3626e65e8ab32b15fa")


