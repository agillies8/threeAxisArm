#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from math import cos

def encoder():
    rospy.init_node('encoder_node', anonymous=True, log_level=rospy.WARN)
    pub = rospy.Publisher('encoder', Float32, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        encoderv = cos(rospy.get_time())
        rospy.loginfo(encoderv)
        pub.publish(encoderv)
        rate.sleep()

if __name__ == '__main__':
    try:
        encoder()
    except rospy.ROSInterruptException:
        pass