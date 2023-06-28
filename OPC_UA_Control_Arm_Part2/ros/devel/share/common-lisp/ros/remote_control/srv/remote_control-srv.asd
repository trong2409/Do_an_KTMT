
(cl:in-package :asdf)

(defsystem "remote_control-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ChangePosition" :depends-on ("_package_ChangePosition"))
    (:file "_package_ChangePosition" :depends-on ("_package"))
    (:file "GoHome" :depends-on ("_package_GoHome"))
    (:file "_package_GoHome" :depends-on ("_package"))
    (:file "SetChuck" :depends-on ("_package_SetChuck"))
    (:file "_package_SetChuck" :depends-on ("_package"))
    (:file "SetPWMServo" :depends-on ("_package_SetPWMServo"))
    (:file "_package_SetPWMServo" :depends-on ("_package"))
    (:file "SetPosition" :depends-on ("_package_SetPosition"))
    (:file "_package_SetPosition" :depends-on ("_package"))
    (:file "SetServo" :depends-on ("_package_SetServo"))
    (:file "_package_SetServo" :depends-on ("_package"))
  ))