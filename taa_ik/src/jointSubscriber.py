#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState

class CommandToJointState:
    def __init__(self):
        self.joint_name = "link5_end_joint"
        self.joint_state = JointState()
        self.joint_state.name.append(self.joint_name)
        self.joint_state.position.append(0.0)
        self.joint_state.velocity.append(0.0)
        self.joint_pub = rospy.Publisher("joint_states", JointState, queue_size=1)

    def Pub(self, joint1, joint2):
        self.joint_state.position[0] = joint1 +joint2
        self.joint_state.header.stamp = rospy.Time.now()
        self.joint_pub.publish(self.joint_state)

class MySubscriber(object):

    def __init__(self):

        # TODO : do a wait topic        
        self.joint1 = 0.0
        self.joint2 = 0.0
        self.joint3Pub = CommandToJointState()

        rospy.Subscriber('command1', Float64, self.joint1_callback)
        rospy.Subscriber('command2', Float64, self.joint2_callback)

    def joint1_callback(self,msg):
        rospy.loginfo('got encoder %f', msg.data)
        self.joint1 = msg.data

    def joint2_callback(self,msg):
        # This callback is the boss, this one dictates the publish rate
        rospy.loginfo('got joint2 position %f', msg.data)
        self.joint2 = msg.data
        self.joint3Pub.Pub(joint1=self.joint1,
                                            joint2=self.joint2)


    def loop(self):
        rospy.logwarn("Starting Loop...")
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('subscriber_node', anonymous=True, log_level=rospy.WARN)
    my_subs = MySubscriber()
    my_subs.loop()