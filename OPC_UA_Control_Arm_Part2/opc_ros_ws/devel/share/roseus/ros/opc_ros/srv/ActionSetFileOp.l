;; Auto-generated. Do not edit!


(when (boundp 'opc_ros::ActionSetFileOp)
  (if (not (find-package "OPC_ROS"))
    (make-package "OPC_ROS"))
  (shadow 'ActionSetFileOp (find-package "OPC_ROS")))
(unless (find-package "OPC_ROS::ACTIONSETFILEOP")
  (make-package "OPC_ROS::ACTIONSETFILEOP"))
(unless (find-package "OPC_ROS::ACTIONSETFILEOPREQUEST")
  (make-package "OPC_ROS::ACTIONSETFILEOPREQUEST"))
(unless (find-package "OPC_ROS::ACTIONSETFILEOPRESPONSE")
  (make-package "OPC_ROS::ACTIONSETFILEOPRESPONSE"))

(in-package "ROS")





(defclass opc_ros::ActionSetFileOpRequest
  :super ros::object
  :slots (_file_name _data ))

(defmethod opc_ros::ActionSetFileOpRequest
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

(defclass opc_ros::ActionSetFileOpResponse
  :super ros::object
  :slots (_success _message ))

(defmethod opc_ros::ActionSetFileOpResponse
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

(defclass opc_ros::ActionSetFileOp
  :super ros::object
  :slots ())

(setf (get opc_ros::ActionSetFileOp :md5sum-) "272e984a50155b54f97a32954cf22782")
(setf (get opc_ros::ActionSetFileOp :datatype-) "opc_ros/ActionSetFileOp")
(setf (get opc_ros::ActionSetFileOp :request) opc_ros::ActionSetFileOpRequest)
(setf (get opc_ros::ActionSetFileOp :response) opc_ros::ActionSetFileOpResponse)

(defmethod opc_ros::ActionSetFileOpRequest
  (:response () (instance opc_ros::ActionSetFileOpResponse :init)))

(setf (get opc_ros::ActionSetFileOpRequest :md5sum-) "272e984a50155b54f97a32954cf22782")
(setf (get opc_ros::ActionSetFileOpRequest :datatype-) "opc_ros/ActionSetFileOpRequest")
(setf (get opc_ros::ActionSetFileOpRequest :definition-)
      "string file_name
string data
---
bool success
string message
")

(setf (get opc_ros::ActionSetFileOpResponse :md5sum-) "272e984a50155b54f97a32954cf22782")
(setf (get opc_ros::ActionSetFileOpResponse :datatype-) "opc_ros/ActionSetFileOpResponse")
(setf (get opc_ros::ActionSetFileOpResponse :definition-)
      "string file_name
string data
---
bool success
string message
")



(provide :opc_ros/ActionSetFileOp "272e984a50155b54f97a32954cf22782")


