#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from math import sin

def desiredcounts():
    rospy.init_node('desiredcounts_node', anonymous=True, log_level=rospy.WARN)
    pub = rospy.Publisher('desiredcounts', Float32, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        desiredv = sin(rospy.get_time())
        rospy.loginfo(desiredv)
        pub.publish(desiredv)
        rate.sleep()

if __name__ == '__main__':
    try:
        desiredcounts()
    except rospy.ROSInterruptException:
        pass