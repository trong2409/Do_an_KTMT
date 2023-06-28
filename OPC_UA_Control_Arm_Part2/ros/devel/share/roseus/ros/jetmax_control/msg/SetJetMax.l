;; Auto-generated. Do not edit!


(when (boundp 'jetmax_control::SetJetMax)
  (if (not (find-package "JETMAX_CONTROL"))
    (make-package "JETMAX_CONTROL"))
  (shadow 'SetJetMax (find-package "JETMAX_CONTROL")))
(unless (find-package "JETMAX_CONTROL::SETJETMAX")
  (make-package "JETMAX_CONTROL::SETJETMAX"))

(in-package "ROS")
;;//! \htmlinclude SetJetMax.msg.html


(defclass jetmax_control::SetJetMax
  :super ros::object
  :slots (_x _y _z _duration ))

(defmethod jetmax_control::SetJetMax
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

(setf (get jetmax_control::SetJetMax :md5sum-) "19cc8078d43cb0cd983e9688d658cb05")
(setf (get jetmax_control::SetJetMax :datatype-) "jetmax_control/SetJetMax")
(setf (get jetmax_control::SetJetMax :definition-)
      "float32 x
float32 y
float32 z
float32 duration
")



(provide :jetmax_control/SetJetMax "19cc8078d43cb0cd983e9688d658cb05")


