#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64, Float64MultiArray
from math import cos, sin

#rosrun rqt_ez_publisher rqt_ez_publisher  Run this command to bring up the joint commander and send commmands over the three axis

def joint():
    rospy.init_node('command', anonymous=True, log_level=rospy.WARN)
    commands = rospy.Publisher('axis_commands', Float64MultiArray, queue_size=10)

    rate = rospy.Rate(1) # 50hz
    while not rospy.is_shutdown():


        joint1v = cos(rospy.get_time())
        joint2v = cos(rospy.get_time())
        joint3v = sin(rospy.get_time())

        command_vals = Float64MultiArray()
        command_vals.data = [joint1v, joint2v, joint3v]

        rospy.loginfo(joint1v)
        rospy.loginfo(joint2v)
        rospy.loginfo(joint3v)

        commands.publish(command_vals)


        rate.sleep()

if __name__ == '__main__':
    try:
        joint()
    except rospy.ROSInterruptException:
        pass