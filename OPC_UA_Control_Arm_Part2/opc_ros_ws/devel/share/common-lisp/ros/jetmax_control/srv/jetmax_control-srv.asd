
(cl:in-package :asdf)

(defsystem "jetmax_control-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "FK" :depends-on ("_package_FK"))
    (:file "_package_FK" :depends-on ("_package"))
    (:file "IK" :depends-on ("_package_IK"))
    (:file "_package_IK" :depends-on ("_package"))
  ))