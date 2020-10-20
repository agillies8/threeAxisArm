#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32


class ControlValuePub(object):

    def __init__(self, kp=1, kd=0.1, dt=10):
        self._kp = kp
        self._kd = kd
        self._dt = dt
        self.pub = rospy.Publisher('controlvalue', Float32, queue_size=10) 

    def publish_controlvalue(self,desiredv, encoderv):

        PDvalue = self._kp * ( desiredv - encoderv ) + self._kd *( desiredv - encoderv ) / self._dt
        rospy.loginfo(PDvalue)
        self.pub.publish(PDvalue)
        rospy.logwarn("PUB Control Value="+str(PDvalue))

if __name__ == '__main__':
    rospy.init_node('controlvalue_node', anonymous=True, log_level=rospy.INFO)
    contr_obj = ControlValuePub()
    try:
        contr_obj.publish_controlvalue(desiredv=1.0, encoderv=2.0)
    except rospy.ROSInterruptException:
        pass