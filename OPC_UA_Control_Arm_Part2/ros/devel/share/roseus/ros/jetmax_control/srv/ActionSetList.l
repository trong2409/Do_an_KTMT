;; Auto-generated. Do not edit!


(when (boundp 'jetmax_control::ActionSetList)
  (if (not (find-package "JETMAX_CONTROL"))
    (make-package "JETMAX_CONTROL"))
  (shadow 'ActionSetList (find-package "JETMAX_CONTROL")))
(unless (find-package "JETMAX_CONTROL::ACTIONSETLIST")
  (make-package "JETMAX_CONTROL::ACTIONSETLIST"))
(unless (find-package "JETMAX_CONTROL::ACTIONSETLISTREQUEST")
  (make-package "JETMAX_CONTROL::ACTIONSETLISTREQUEST"))
(unless (find-package "JETMAX_CONTROL::ACTIONSETLISTRESPONSE")
  (make-package "JETMAX_CONTROL::ACTIONSETLISTRESPONSE"))

(in-package "ROS")





(defclass jetmax_control::ActionSetListRequest
  :super ros::object
  :slots ())

(defmethod jetmax_control::ActionSetListRequest
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

(defclass jetmax_control::ActionSetListResponse
  :super ros::object
  :slots (_action_sets ))

(defmethod jetmax_control::ActionSetListResponse
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

(defclass jetmax_control::ActionSetList
  :super ros::object
  :slots ())

(setf (get jetmax_control::ActionSetList :md5sum-) "eef2f65442e5649b9b3489933fa21e88")
(setf (get jetmax_control::ActionSetList :datatype-) "jetmax_control/ActionSetList")
(setf (get jetmax_control::ActionSetList :request) jetmax_control::ActionSetListRequest)
(setf (get jetmax_control::ActionSetList :response) jetmax_control::ActionSetListResponse)

(defmethod jetmax_control::ActionSetListRequest
  (:response () (instance jetmax_control::ActionSetListResponse :init)))

(setf (get jetmax_control::ActionSetListRequest :md5sum-) "eef2f65442e5649b9b3489933fa21e88")
(setf (get jetmax_control::ActionSetListRequest :datatype-) "jetmax_control/ActionSetListRequest")
(setf (get jetmax_control::ActionSetListRequest :definition-)
      "---
string[] action_sets
")

(setf (get jetmax_control::ActionSetListResponse :md5sum-) "eef2f65442e5649b9b3489933fa21e88")
(setf (get jetmax_control::ActionSetListResponse :datatype-) "jetmax_control/ActionSetListResponse")
(setf (get jetmax_control::ActionSetListResponse :definition-)
      "---
string[] action_sets
")



(provide :jetmax_control/ActionSetList "eef2f65442e5649b9b3489933fa21e88")


