
(cl:in-package :asdf)

(defsystem "opc_ros-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ActionSetFileOp" :depends-on ("_package_ActionSetFileOp"))
    (:file "_package_ActionSetFileOp" :depends-on ("_package"))
    (:file "ActionSetList" :depends-on ("_package_ActionSetList"))
    (:file "_package_ActionSetList" :depends-on ("_package"))
    (:file "SetTarget" :depends-on ("_package_SetTarget"))
    (:file "_package_SetTarget" :depends-on ("_package"))
    (:file "SetTarget_object" :depends-on ("_package_SetTarget_object"))
    (:file "_package_SetTarget_object" :depends-on ("_package"))
  ))