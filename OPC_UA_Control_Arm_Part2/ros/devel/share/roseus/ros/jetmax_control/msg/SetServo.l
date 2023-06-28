;; Auto-generated. Do not edit!


(when (boundp 'jetmax_control::SetServo)
  (if (not (find-package "JETMAX_CONTROL"))
    (make-package "JETMAX_CONTROL"))
  (shadow 'SetServo (find-package "JETMAX_CONTROL")))
(unless (find-package "JETMAX_CONTROL::SETSERVO")
  (make-package "JETMAX_CONTROL::SETSERVO"))

(in-package "ROS")
;;//! \htmlinclude SetServo.msg.html


(defclass jetmax_control::SetServo
  :super ros::object
  :slots (_data _duration ))

(defmethod jetmax_control::SetServo
  (:init
   (&key
    ((:data __data) 0)
    ((:duration __duration) 0.0)
    )
   (send-super :init)
   (setq _data (round __data))
   (setq _duration (float __duration))
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:duration
   (&optional __duration)
   (if __duration (setq _duration __duration)) _duration)
  (:serialization-length
   ()
   (+
    ;; uint16 _data
    2
    ;; float32 _duration
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _data
       (write-word _data s)
     ;; float32 _duration
       (sys::poke _duration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _data
     (setq _data (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float32 _duration
     (setq _duration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get jetmax_control::SetServo :md5sum-) "b17bd22a947dc3333e94c2b1699db322")
(setf (get jetmax_control::SetServo :datatype-) "jetmax_control/SetServo")
(setf (get jetmax_control::SetServo :definition-)
      "uint16 data
float32 duration
")



(provide :jetmax_control/SetServo "b17bd22a947dc3333e94c2b1699db322")


