#!/usr/bin/env python3
import sys

sys.path.insert(1, '/home/hiwonder/ros/src/jetmax_buildin_funcs/remote_control/scripts')
sys.path.insert(2, '/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control/scripts')
import remote_control_joystick
import jetmax_control_main
import hiwonder
import traceback
import rospy
from threading import Thread

def thread_Joystick(js):
	while True:
		try:	
			js.update_buttons()
			rospy.sleep(0.05)
			if rospy.is_shutdown():
				sys.exit(0)
		except KeyboardInterrupt:
			sys.exit(0)

if __name__ == "__main__":
	
	jetmaxObj = hiwonder.JetMax()
	suckerObj = hiwonder.Sucker()
	rospy.init_node("very_main", anonymous=False)
	try:
		jetmax = jetmax_control_main.JetMaxControl(hiwonder, jetmaxObj, suckerObj)
		js = remote_control_joystick.Joystick(hiwonder, jetmaxObj, suckerObj)
	except:
		traceback.print_exc()

	js.change_mode(0)  # Joint mode as the default mode

	thread1 = Thread(target = thread_Joystick, args = (js,))
	thread1.start()
	thread2 = Thread(target = jetmax.update)
	thread2.start()