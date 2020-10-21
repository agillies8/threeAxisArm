#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from math import cos, sin

#rosrun rqt_ez_publisher rqt_ez_publisher  Run this command to bring up the joint commander and send commmands over the three axis

def joint():
    rospy.init_node('command', anonymous=True, log_level=rospy.WARN)
    pub1 = rospy.Publisher('command1', Float64, queue_size=10)
    pub2 = rospy.Publisher('command2', Float64, queue_size=10)
    pub3 = rospy.Publisher('command3', Float64, queue_size=10)


    rate = rospy.Rate(50) # 50hz
    while not rospy.is_shutdown():


        joint1v = cos(rospy.get_time())
        joint2v = cos(rospy.get_time())
        joint3v = sin(rospy.get_time())

        rospy.loginfo(joint1v)
        rospy.loginfo(joint2v)
        rospy.loginfo(joint3v)

        pub1.publish(joint1v)
        pub2.publish(joint2v)
        pub3.publish(joint3v)

        rate.sleep()

if __name__ == '__main__':
    try:
        joint()
    except rospy.ROSInterruptException:
        pass