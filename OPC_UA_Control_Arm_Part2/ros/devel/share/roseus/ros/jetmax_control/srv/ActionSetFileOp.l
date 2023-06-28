;; Auto-generated. Do not edit!


(when (boundp 'jetmax_control::ActionSetFileOp)
  (if (not (find-package "JETMAX_CONTROL"))
    (make-package "JETMAX_CONTROL"))
  (shadow 'ActionSetFileOp (find-package "JETMAX_CONTROL")))
(unless (find-package "JETMAX_CONTROL::ACTIONSETFILEOP")
  (make-package "JETMAX_CONTROL::ACTIONSETFILEOP"))
(unless (find-package "JETMAX_CONTROL::ACTIONSETFILEOPREQUEST")
  (make-package "JETMAX_CONTROL::ACTIONSETFILEOPREQUEST"))
(unless (find-package "JETMAX_CONTROL::ACTIONSETFILEOPRESPONSE")
  (make-package "JETMAX_CONTROL::ACTIONSETFILEOPRESPONSE"))

(in-package "ROS")





(defclass jetmax_control::ActionSetFileOpRequest
  :super ros::object
  :slots (_file_name _data ))

(defmethod jetmax_control::ActionSetFileOpRequest
  (:init
   (&key
    ((:file_name __file_name) "")
    ((:data __data) "")
    )
   (send-super :init)
   (setq _file_name (string __file_name))
   (setq _data (string __data))
   self)
  (:file_name
   (&optional __file_name)
   (if __file_name (setq _file_name __file_name)) _file_name)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; string _file_name
    4 (length _file_name)
    ;; string _data
    4 (length _data)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _file_name
       (write-long (length _file_name) s) (princ _file_name s)
     ;; string _data
       (write-long (length _data) s) (princ _data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _file_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _file_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass jetmax_control::ActionSetFileOpResponse
  :super ros::object
  :slots (_success _message ))

(defmethod jetmax_control::ActionSetFileOpResponse
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

(defclass jetmax_control::ActionSetFileOp
  :super ros::object
  :slots ())

(setf (get jetmax_control::ActionSetFileOp :md5sum-) "272e984a50155b54f97a32954cf22782")
(setf (get jetmax_control::ActionSetFileOp :datatype-) "jetmax_control/ActionSetFileOp")
(setf (get jetmax_control::ActionSetFileOp :request) jetmax_control::ActionSetFileOpRequest)
(setf (get jetmax_control::ActionSetFileOp :response) jetmax_control::ActionSetFileOpResponse)

(defmethod jetmax_control::ActionSetFileOpRequest
  (:response () (instance jetmax_control::ActionSetFileOpResponse :init)))

(setf (get jetmax_control::ActionSetFileOpRequest :md5sum-) "272e984a50155b54f97a32954cf22782")
(setf (get jetmax_control::ActionSetFileOpRequest :datatype-) "jetmax_control/ActionSetFileOpRequest")
(setf (get jetmax_control::ActionSetFileOpRequest :definition-)
      "string file_name
string data
---
bool success
string message
")

(setf (get jetmax_control::ActionSetFileOpResponse :md5sum-) "272e984a50155b54f97a32954cf22782")
(setf (get jetmax_control::ActionSetFileOpResponse :datatype-) "jetmax_control/ActionSetFileOpResponse")
(setf (get jetmax_control::ActionSetFileOpResponse :definition-)
      "string file_name
string data
---
bool success
string message
")



(provide :jetmax_control/ActionSetFileOp "272e984a50155b54f97a32954cf22782")


