
(cl:in-package :asdf)

(defsystem "remote_control-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Mecanum" :depends-on ("_package_Mecanum"))
    (:file "_package_Mecanum" :depends-on ("_package"))
    (:file "Status" :depends-on ("_package_Status"))
    (:file "_package_Status" :depends-on ("_package"))
  ))