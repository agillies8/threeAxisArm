#!/usr/bin/env python

import rospy  
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64

#base_axis1_joint
#base_link3_joint
#link3_link4_joint
#base_link1_joint
#link1_trilink_joint
#tri_link5_joint
#link5_end_joint
#tri_link2_joint
#base_link6_joint

class CommandToJointState:
    def __init__(self):
        self.joint_name = "base_link1_joint"
        self.joint_state = JointState()
        self.joint_state.name.append(self.joint_name)
        self.joint_state.position.append(0.0)
        self.joint_state.velocity.append(0.0)
        self.joint_pub = rospy.Publisher("joint_states", JointState, queue_size=1)
        self.command_sub = rospy.Subscriber("command2", Float64,
                                            self.command_callback, queue_size=1)

    def command_callback(self, msg):
        self.joint_state.position[0] = msg.data
        self.joint_state.header.stamp = rospy.Time.now()
        self.joint_pub.publish(self.joint_state)

if __name__ == '__main__':
    rospy.init_node('command_to_joint_state')
    command_to_joint_state = CommandToJointState()
    rospy.spin()