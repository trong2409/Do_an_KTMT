;; Auto-generated. Do not edit!


(when (boundp 'opc_ros::ActionSetList)
  (if (not (find-package "OPC_ROS"))
    (make-package "OPC_ROS"))
  (shadow 'ActionSetList (find-package "OPC_ROS")))
(unless (find-package "OPC_ROS::ACTIONSETLIST")
  (make-package "OPC_ROS::ACTIONSETLIST"))
(unless (find-package "OPC_ROS::ACTIONSETLISTREQUEST")
  (make-package "OPC_ROS::ACTIONSETLISTREQUEST"))
(unless (find-package "OPC_ROS::ACTIONSETLISTRESPONSE")
  (make-package "OPC_ROS::ACTIONSETLISTRESPONSE"))

(in-package "ROS")





(defclass opc_ros::ActionSetListRequest
  :super ros::object
  :slots ())

(defmethod opc_ros::ActionSetListRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass opc_ros::ActionSetListResponse
  :super ros::object
  :slots (_action_sets ))

(defmethod opc_ros::ActionSetListResponse
  (:init
   (&key
    ((:action_sets __action_sets) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _action_sets __action_sets)
   self)
  (:action_sets
   (&optional __action_sets)
   (if __action_sets (setq _action_sets __action_sets)) _action_sets)
  (:serialization-length
   ()
   (+
    ;; string[] _action_sets
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _action_sets)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _action_sets
     (write-long (length _action_sets) s)
     (dolist (elem _action_sets)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _action_sets
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _action_sets (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _action_sets i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(defclass opc_ros::ActionSetList
  :super ros::object
  :slots ())

(setf (get opc_ros::ActionSetList :md5sum-) "eef2f65442e5649b9b3489933fa21e88")
(setf (get opc_ros::ActionSetList :datatype-) "opc_ros/ActionSetList")
(setf (get opc_ros::ActionSetList :request) opc_ros::ActionSetListRequest)
(setf (get opc_ros::ActionSetList :response) opc_ros::ActionSetListResponse)

(defmethod opc_ros::ActionSetListRequest
  (:response () (instance opc_ros::ActionSetListResponse :init)))

(setf (get opc_ros::ActionSetListRequest :md5sum-) "eef2f65442e5649b9b3489933fa21e88")
(setf (get opc_ros::ActionSetListRequest :datatype-) "opc_ros/ActionSetListRequest")
(setf (get opc_ros::ActionSetListRequest :definition-)
      "---
string[] action_sets
")

(setf (get opc_ros::ActionSetListResponse :md5sum-) "eef2f65442e5649b9b3489933fa21e88")
(setf (get opc_ros::ActionSetListResponse :datatype-) "opc_ros/ActionSetListResponse")
(setf (get opc_ros::ActionSetListResponse :definition-)
      "---
string[] action_sets
")



(provide :opc_ros/ActionSetList "eef2f65442e5649b9b3489933fa21e88")


