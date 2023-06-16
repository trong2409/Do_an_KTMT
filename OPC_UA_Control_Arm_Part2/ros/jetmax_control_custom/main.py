#!/usr/bin/env python3
import sys

sys.path.append('/home/hiwonder/ros/src/jetmax_buildin_funcs/remote_control/scripts')
sys.path.append('/home/hiwonder/ros/src/jetmax_buildin_funcs/jetmax_control/scripts')
sys.path.append('/home/hiwonder/ros/src/jetmax_buildin_funcs/palletizing/scripts')
sys.path.append('/home/hiwonder/ros/src/jetmax_buildin_funcs/object_tracking/scripts')
sys.path.append('/home/hiwonder/ros/src/jetmax_buildin_funcs/color_sorting/scripts')
sys.path.append('/home/hiwonder/ros/src/jetmax_buildin_funcs/waste_classification/scripts')

import hiwonder
import traceback
import rospy
from threading import Thread
import asyncio


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            cls._instance.jetmax = hiwonder.JetMax()
            cls._instance.sucker = hiwonder.Sucker()
        return cls._instance


async def async_process():
    async def async_waste_classification():
        while True:
            try:
                waste_classification_main.image_proc()
                if rospy.is_shutdown():
                    break
            except Exception as e:
                rospy.logerr(e)
                break
            await asyncio.sleep(0.01)

    await asyncio.gather(async_waste_classification())


if __name__ == "__main__":

    rospy.init_node("very_main", anonymous=False)

    import remote_control_joystick
    import jetmax_control_main
    import palletizing_main
    #import object_tracking_main
    #import color_sorting_main
    #import waste_classification_main


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


    def thread_object_tracking():
        while True:
            try:
                object_tracking_main.image_proc()
                if rospy.is_shutdown():
                    break
            except KeyboardInterrupt:
                break


    # remote_control_joystick.js.change_mode(0)  # Joint mode as the default mode
    try:
        thread1 = Thread(target=thread_Joystick, args=(remote_control_joystick.js,))
        thread1.start()
        thread2 = Thread(target=jetmax_control_main.jetmax.update)
        thread2.start()
        thread3 = Thread(target=thread_object_tracking)
        thread3.start()
        # thread4 = Thread(target = thread_waste_classification)
        # thread4.start()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(async_process())
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        traceback.print_exc()
    finally:
        loop.stop()
        loop.close()
        exit()
