#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState

#  0  base_axis1_joint - axis 1 pivot  n
#  1  base_link1_joint - axis 2 input n 
#  2  base_link3_joint - axis 3 input (secondary link) n
#  3  link1_trilink_joint - axis 2 to triangle y 
#  4  base_link6_joint y
#  5  link3_link4_joint  - axis 3 to secondary y 
#  6  tri_link5_joint - trinalge to top link y 
#  7  link5_end_joint y 
#  8  tri_link2_joint - lower link to ee

class JointPub:
    def __init__(self):
        self.joint_state = JointState()
        self.joint_state.name = ['base_axis1_joint', 'base_link1_joint','base_link3_joint', 'link1_trilink_joint', 'base_link6_joint', 'link3_link4_joint', 'tri_link5_joint', 'link5_end_joint', 'tri_link2_joint']
        self.joint_state.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] 
        self.joint_state.velocity = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] 
        self.joint_pub = rospy.Publisher("joint_states", JointState, queue_size=1)

    def Pub(self, joint1, joint2, joint3):
        self.joint_state.position[0] = joint1 
        self.joint_state.position[1] = joint2
        self.joint_state.position[2] = joint3
        self.joint_state.position[3] = - joint2
        self.joint_state.position[4] = joint2
        self.joint_state.position[5] =   joint2 - joint3
        self.joint_state.position[6] = self.joint_state.position[8]
        self.joint_state.position[7] = -joint3
        self.joint_state.position[8] =  joint3

        self.joint_state.header.stamp = rospy.Time.now()
        self.joint_pub.publish(self.joint_state)

class MySubscriber(object):

    def __init__(self):

        # TODO : do a wait topic        
        self.joint1 = 0.0
        self.joint2 = 0.0
        self.joint3 = 0.0
        self.jointpub = JointPub()

        rospy.Subscriber('command1', Float64, self.joint1_callback)
        rospy.Subscriber('command2', Float64, self.joint2_callback)
        rospy.Subscriber('command3', Float64, self.joint3_callback)

    def joint1_callback(self,msg):
        self.joint1 = msg.data
        self.jointpub.Pub(joint1=self.joint1, joint2=self.joint2, joint3=self.joint3)

    def joint2_callback(self,msg):
        # This callback is the boss, this one dictates the publish rate
        self.joint2 = msg.data
        self.jointpub.Pub(joint1=self.joint1, joint2=self.joint2, joint3=self.joint3)

    def joint3_callback(self,msg):
        # This callback is the boss, this one dictates the publish rate
        self.joint3 = msg.data
        self.jointpub.Pub(joint1=self.joint1, joint2=self.joint2, joint3=self.joint3)


    def loop(self):
        rospy.logwarn("Starting Loop...")
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('subscriber_node', anonymous=True, log_level=rospy.WARN)
    my_subs = MySubscriber()
    my_subs.loop()