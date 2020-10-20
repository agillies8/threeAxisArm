#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from math import cos, sin

def joint():
    rospy.init_node('command', anonymous=True, log_level=rospy.WARN)
    pub1 = rospy.Publisher('command1', Float64, queue_size=10)
    pub2 = rospy.Publisher('command2', Float64, queue_size=10)


    rate = rospy.Rate(50) # 10hz
    while not rospy.is_shutdown():
        joint1v = cos(rospy.get_time())
        joint2v = sin(rospy.get_time())
        rospy.loginfo(joint1v)
        rospy.loginfo(joint2v)
        pub1.publish(joint1v)
        pub2.publish(joint2v)

        rate.sleep()

if __name__ == '__main__':
    try:
        joint()
    except rospy.ROSInterruptException:
        pass