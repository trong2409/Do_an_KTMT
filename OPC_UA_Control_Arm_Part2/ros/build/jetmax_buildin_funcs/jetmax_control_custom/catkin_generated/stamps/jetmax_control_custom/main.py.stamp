#!/usr/bin/env python3
import sys

sys.path.insert(1, '/home/hiwonder/ros/src/jetmax_buildin_funcs/remote_control/scripts')
sys.path.insert(2, '/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control/scripts')

import hiwonder
import traceback
import rospy
from threading import Thread


class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            cls._instance.jetmax = hiwonder.JetMax()
            cls._instance.sucker = hiwonder.Sucker()
        return cls._instance
    



if __name__ == "__main__":
	
	rospy.init_node("very_main", anonymous=False)
	
	import remote_control_joystick
	import jetmax_control_main
 
	def thread_Joystick(js):
		remote_control_joystick.change_mode(0)
		while True:
			try:	
				js.update_buttons()
				rospy.sleep(0.05)
				if rospy.is_shutdown():
					sys.exit(0)
			except KeyboardInterrupt:
				sys.exit(0)
    
	# remote_control_joystick.js.change_mode(0)  # Joint mode as the default mode
	try:
		thread1 = Thread(target = thread_Joystick, args = (remote_control_joystick.js,))
		thread1.start()
		thread2 = Thread(target = jetmax_control_main.jetmax.update)
		thread2.start()
	except KeyboardInterrupt:
		sys.exit(0)
